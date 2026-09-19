import os
import tensorflow as tf

FOLDERS = [
    "data/train",
    "data/train_split",
    "data/validation"
]

EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")


def check_image(path):

    try:
        data = tf.io.read_file(path)

        image = tf.io.decode_image(
            data,
            channels=3,
            expand_animations=False
        )

        _ = image.numpy()

        return True

    except Exception as error:

        print("\nBAD IMAGE:")
        print(path)
        print("ERROR:")
        print(error)
        print("-" * 60)

        return False


total = 0
bad = 0

print("===================================")
print("   TENSORFLOW IMAGE CHECKER")
print("===================================")

for folder in FOLDERS:

    if not os.path.exists(folder):
        print(f"\nSkipping: {folder}")
        continue

    print(f"\nChecking: {folder}")

    for root, dirs, files in os.walk(folder):

        for filename in files:

            if filename.lower().endswith(EXTENSIONS):

                filepath = os.path.join(
                    root,
                    filename
                )

                total += 1

                if not check_image(filepath):
                    bad += 1


print("\n===================================")
print("CHECK COMPLETED")
print("===================================")

print(f"Total images checked: {total}")
print(f"Bad images found: {bad}")

if bad == 0:
    print("\nAll images passed TensorFlow decoding.")
else:
    print("\nRemove or replace the BAD images listed above.")