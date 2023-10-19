#! /usr/bin/env python3

import requests
from Modifying_Images import get_image_path
import os

url = "http://website.com/fruits/"    # Website endpoint which will receive the information.
text_path = "/home/directory/supplier-data/descriptions/"    # This is the file path which the description of each image
# must be, so it can be processed and later on sent to the website.
text_extension = ".txt"    # Extension of the description files.
image_path = "/home/directory/supplier-data/images/"    # This is the file path which the images must be present to
# match the description files.
image_extension = ".jpeg"   # The file extension of each image.


def writing_dictionary(text_file_path=text_path, image_file_path=image_path):
    """Generating a list of dictionaries containing all the processed information from each file description."""
    dictionary = []
    text_files = get_image_path(text_file_path, text_extension)    # Retrieving a list of paths for each description
    # file.
    image_files = get_image_path(image_file_path, image_extension)  # Retrieving a list of paths for each image file.

    for text in text_files:    # Going through each text file:
        current_image = ""

        for image in image_files:   # For each image path:
            image_name = os.path.basename(image).lower().strip(image_extension)    # Store the name of the image file
            # without the extension.
            text_name = os.path.basename(text).lower().strip(text_extension)    # Store the name of the text file
            # without the extension.

            if image_name == text_name:    # if the name of the text file matches the name of the image file:
                current_image = os.path.basename(image)    # Store the name of the file. Which will be the same name of
                # the file already uploaded to the website's server.

        with open(text, 'r') as f:  # Opening the description file on read mode:
            data = f.read()    # Storing the contents of the file.
            infos = data.strip().split("\n")    # Removing break characters from the text.

            info = {    # Generating a dictionary which will contain all the information from the description file.
                "name": infos[0],   # Name of the product.
                "weight": int(infos[1].strip(' lbs')),  # Weight of the product.
                "description": infos[2],    # Products description.
                "image_name": current_image    # The image name corresponding to the product.
            }

            dictionary.append(info)    # Adding the dictionary to the variable that will be returned.

    return dictionary   # Returning list of dictionaries.


def main():
    dictionaries = writing_dictionary()    # Storing the list of dictionaries.

    for dictionary in dictionaries:    # For each dictionary within the list of dictionaries:
        r = requests.post(url, json=dictionary)    # Uploading each dictionary using HTTP POST request.

        if r.status_code == 201:    # If the upload was successful, a message will be printed with the status code for
            # the request.
            print(f"Successful HTTP POST: status code {r.status_code}")

        else:   # If the upload failed, a message will be printed with the error status code for the request.
            print(f"Failed HTTP POST: status code {r.status_code}")


if __name__ == "__main__":
    main()
