import os
import sys
import json

import numpy as np
import tensorflow as tf
from PIL import Image


MODEL_DIR = "model"

MODEL_PATH = os.path.join(MODEL_DIR, "plant_disease_model.keras")
CLASS_PATH = os.path.join(MODEL_DIR, "class_names.json")

IMAGE_SIZE = (224, 224)


def load_class_names():
    """
    Load class names in the EXACT order they were saved during training.
    This order must match the model's output index order.
    """
    with open(CLASS_PATH, "r") as file:
        class_names = json.load(file)

    return class_names


def load_model():
    model = tf.keras.models.load_model(MODEL_PATH)
    return model


def preprocess_image(image_path):
    """
    Load and prepare a single image for prediction. Mirrors the exact
    preprocessing used in pages/1_Analyser.py so the CLI tool and the
    Streamlit app never disagree on a prediction for the same image.

    - Transparent PNGs are composited onto a white background first.
      Converting straight to RGB would silently turn transparent areas
      BLACK, which looks nothing like the photographed leaves the
      model trained on and produces scattered, low-confidence results.
    - No manual rescaling (e.g. dividing by 255): the training model
      has tf.keras.applications.mobilenet_v2.preprocess_input built
      into the model graph itself, so this hands the model raw pixel
      values in the 0-255 range, resized to IMAGE_SIZE.
    """
    raw_img = Image.open(image_path)

    if raw_img.mode in ("RGBA", "LA") or (
        raw_img.mode == "P" and "transparency" in raw_img.info
    ):
        raw_img = raw_img.convert("RGBA")
        white_bg = Image.new("RGBA", raw_img.size, (255, 255, 255, 255))
        raw_img = Image.alpha_composite(white_bg, raw_img).convert("RGB")
    else:
        raw_img = raw_img.convert("RGB")

    img = raw_img.resize(IMAGE_SIZE)
    img_array = tf.keras.utils.img_to_array(img)

    # Add batch dimension: (224, 224, 3) -> (1, 224, 224, 3)
    img_array = np.expand_dims(img_array, axis=0)

    return img_array


def predict_image(model, class_names, image_path, top_k=3):
    """
    Run prediction on a single image and return the top_k
    (class_name, confidence) results sorted by confidence.
    """
    img_array = preprocess_image(image_path)

    predictions = model.predict(img_array, verbose=0)[0]

    # Sanity check: predictions length must match number of classes
    if len(predictions) != len(class_names):
        raise ValueError(
            f"Model output size ({len(predictions)}) does not match "
            f"number of class names ({len(class_names)}). "
            f"Your class_names.json is out of sync with the model."
        )

    top_indices = predictions.argsort()[::-1][:top_k]

    results = [
        (class_names[i], float(predictions[i]) * 100)
        for i in top_indices
    ]

    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python predict.py <path_to_image>")
        sys.exit(1)

    image_path = sys.argv[1]

    if not os.path.exists(image_path):
        print(f"Image not found: {image_path}")
        sys.exit(1)

    print("Loading model...")
    model = load_model()

    print("Loading class names...")
    class_names = load_class_names()
    print(f"Loaded {len(class_names)} classes.")

    print(f"\nPredicting: {image_path}\n")

    results = predict_image(model, class_names, image_path, top_k=3)

    print("Top predictions:")
    for name, confidence in results:
        print(f"  {name}: {confidence:.2f}%")


if __name__ == "__main__":
    main()