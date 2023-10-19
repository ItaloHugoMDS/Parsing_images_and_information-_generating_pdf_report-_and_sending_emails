#! /usr/bin/env python3

from PIL import Image
import os

file_path = "/home/directory/supplier-data/images/"  # This is the file path which the images must be present to be
# modified. This is also the directory in which the new modified images will be stored.
size = (600, 400)   # New dimension for the image.
extension = "jpeg"  # New image extension


def get_image_path(image_path, image_extension=".tiff"):
    """Returning a list with the path for all the images to be modified. The images that have the '.tiff' extension
    will be modified by default."""
    return [os.path.join(image_path, file_path) for file_path in os.listdir(image_path) if file_path.endswith(image_extension)]
    # Using list comprehension to return a list containing all the path for each image.


def main():
    images = get_image_path(file_path)  # Receiving a list containing the file path for each image.

    for image in images:    # For each image path:
        current_image = Image.open(image)   # Opening the image.

        modified_image = current_image.convert("RGB").resize(size)  # Converting the image from "RGBA", which contain
        # transparent background, to "RGB". And resizing the image according to the provided dimension.

        modified_image.save(image.replace(".tiff", ".jpeg"), format=extension)  # Saving the modified image
        # with a new extension.

        current_image.close()   # Closing the image to preserve memory.


if __name__ == "__main__":
    main()
