import os
import json
import tensorflow as tf

from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint


TRAIN_DIR = "data/train_split"
VALIDATION_DIR = "data/validation"

MODEL_DIR = "model"

MODEL_PATH = os.path.join(MODEL_DIR, "plant_disease_model.keras")
CLASS_PATH = os.path.join(MODEL_DIR, "class_names.json")

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 16
EPOCHS = 15


def main():

    print("===================================")
    print("     AI PLANT DISEASE TRAINING")
    print("===================================")

    os.makedirs(MODEL_DIR, exist_ok=True)

    print("\nLoading training images...")

    train_data = tf.keras.utils.image_dataset_from_directory(
        TRAIN_DIR,
        image_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        shuffle=True,
        seed=42
    )

    print("\nLoading validation images...")

    validation_data = tf.keras.utils.image_dataset_from_directory(
        VALIDATION_DIR,
        image_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        shuffle=False
    )

    # IMPORTANT: class_names must be captured BEFORE any .map()/.cache()
    # transformations are applied to train_data, otherwise this can fail
    # or return an empty list on some TF versions.
    class_names = train_data.class_names

    print("\nClasses:")
    for i, name in enumerate(class_names):
        print(f"{i}: {name}")

    print(f"\nTotal classes: {len(class_names)}")

    # Save class names in the exact order used by the model's output layer.
    # predict.py / app.py MUST load this same file to map predictions back
    # to class names correctly.
    with open(CLASS_PATH, "w") as file:
        json.dump(class_names, file, indent=4)

    # Improve performance
    AUTOTUNE = tf.data.AUTOTUNE
    train_data = train_data.prefetch(AUTOTUNE)
    validation_data = validation_data.prefetch(AUTOTUNE)

    # Data augmentation
    data_augmentation = tf.keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.15),
        layers.RandomZoom(0.15),
        layers.RandomContrast(0.1)
    ])

    # MobileNetV2 base
    base_model = MobileNetV2(
        input_shape=(224, 224, 3),
        include_top=False,
        weights="imagenet"
    )

    # Freeze pretrained layers
    base_model.trainable = False

    inputs = layers.Input(shape=(224, 224, 3))

    x = data_augmentation(inputs)

    # MobileNetV2 preprocessing is applied INSIDE the model graph.
    # This means predict.py / app.py must feed RAW 0-255 pixel values,
    # NOT manually rescaled (e.g. no dividing by 255).
    x = tf.keras.applications.mobilenet_v2.preprocess_input(x)

    x = base_model(x, training=False)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dropout(0.3)(x)

    outputs = layers.Dense(len(class_names), activation="softmax")(x)

    model = models.Model(inputs, outputs)

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    print("\nModel created.")
    model.summary()

    callbacks = [
        EarlyStopping(
            monitor="val_accuracy",
            patience=4,
            restore_best_weights=True
        ),
        ModelCheckpoint(
            MODEL_PATH,
            monitor="val_accuracy",
            save_best_only=True
        )
    ]

    print("\n===================================")
    print("       STARTING TRAINING")
    print("===================================\n")

    history = model.fit(
        train_data,
        validation_data=validation_data,
        epochs=EPOCHS,
        callbacks=callbacks
    )

    best_accuracy = max(history.history["val_accuracy"])

    print("\n===================================")
    print("       TRAINING COMPLETED")
    print("===================================")

    print(f"Best validation accuracy: {best_accuracy * 100:.2f}%")

    print("\nModel saved to:")
    print(MODEL_PATH)

    print("\nClass names saved to:")
    print(CLASS_PATH)


if __name__ == "__main__":
    main()