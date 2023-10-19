#! /usr/bin/env python3

import requests
from Modifying_Images import get_image_path

url = "http://website.com/upload/"    # Website/Server endpoint to which the images will be sent.
file_path = "/home/directory/supplier-data/images/"  # This is the file path which the images must be present to be sent.


def main():
    images = get_image_path(file_path, ".jpeg")    # Retrieving the list of path for each image.

    for image in images:    # For each path in the list of paths:
        with open(image, "rb") as opened:   # Opening the images as binary files.
            r = requests.post(url, files={"file": opened})  # Sending the image via HTTP POST method.

            if r.status_code == 201:    # If the upload was done successfully, and message will be printed showing the
                # status code of the request.
                print(f"Successful HTTP POST: Status code {r.status_code}")

            else:   # If the upload failed, and message will be printed showing the error status code of the request.
                print(f"Failed HTTP POST: Status code {r.status_code}")

        opened.close()  # Closing the image to preserve memory.


if __name__ == "__main__":
    main()
