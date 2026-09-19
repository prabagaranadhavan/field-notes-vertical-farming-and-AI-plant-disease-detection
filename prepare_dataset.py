import os
import random
import shutil

SOURCE_DIR = "data/train"
TRAIN_DIR = "data/train_split"
VAL_DIR = "data/validation"

TRAIN_RATIO = 0.8

random.seed(42)


def main():

    print("Preparing dataset...")

    if not os.path.exists(SOURCE_DIR):
        print("ERROR: data/train folder not found.")
        return

    classes = [
        folder
        for folder in os.listdir(SOURCE_DIR)
        if os.path.isdir(os.path.join(SOURCE_DIR, folder))
    ]

    print(f"Found {len(classes)} classes.")

    for class_name in classes:

        source_folder = os.path.join(
            SOURCE_DIR,
            class_name
        )

        images = [
            image
            for image in os.listdir(source_folder)
            if image.lower().endswith(
                (".jpg", ".jpeg", ".png", ".webp")
            )
        ]

        random.shuffle(images)

        split_index = int(
            len(images) * TRAIN_RATIO
        )

        train_images = images[:split_index]
        validation_images = images[split_index:]

        train_folder = os.path.join(
            TRAIN_DIR,
            class_name
        )

        validation_folder = os.path.join(
            VAL_DIR,
            class_name
        )

        os.makedirs(
            train_folder,
            exist_ok=True
        )

        os.makedirs(
            validation_folder,
            exist_ok=True
        )

        for image in train_images:

            shutil.copy2(
                os.path.join(
                    source_folder,
                    image
                ),
                os.path.join(
                    train_folder,
                    image
                )
            )

        for image in validation_images:

            shutil.copy2(
                os.path.join(
                    source_folder,
                    image
                ),
                os.path.join(
                    validation_folder,
                    image
                )
            )

        print(
            f"{class_name}: "
            f"{len(train_images)} training, "
            f"{len(validation_images)} validation"
        )

    print("\nDataset preparation completed!")


if __name__ == "__main__":
    main()