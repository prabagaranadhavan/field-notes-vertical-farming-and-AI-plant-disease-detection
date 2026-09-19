import os
from PIL import Image

DATASET_DIR = "data/train"

bad_images = []

print("Checking images...\n")

for root, dirs, files in os.walk(DATASET_DIR):

    for filename in files:

        if filename.lower().endswith(
            (".jpg", ".jpeg", ".png", ".webp")
        ):

            filepath = os.path.join(
                root,
                filename
            )

            try:

                with Image.open(filepath) as img:
                    img.verify()

            except Exception as error:

                bad_images.append(filepath)

                print("BAD IMAGE:")
                print(filepath)
                print("ERROR:", error)
                print()

print("==============================")

if bad_images:

    print(
        f"Found {len(bad_images)} corrupted images."
    )

else:

    print(
        "All images are valid!"
    )

print("==============================")