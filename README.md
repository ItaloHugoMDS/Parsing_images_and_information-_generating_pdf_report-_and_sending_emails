# Parsing_images_and_information-_generating_pdf_report-_and_sending_emails

This is a skill showcase from a prompt exercise during the "Google IT Automation with Python" certificate.

In one the final projects, a file containing information and data was provided. The goal of the project was:

1 - Modify the a set of images and convert them into a new format.

2 - Upload those images to a webserver using webservice API endpoint and HTTP requests methods.

3 - Go through a set of files extracting information and generating a JSON file which would then be uploaded to another endpoint of a website, containing the informations and the images previously uploaded to the server.

4 - Generate a PDF report file and send it through email using SMTP connection.

Some of the files present in this repository, such as the data sets, are from the Google platform on Coursera. But the implementation of the concepts and the python codes are original solutions created, tested and implement by the owner of the repository.

The steps which the project was executed were:

1 - Modifying the images \(images present in the "suplier_data" directory, within the directory "images"\) by changing the dimensions, converting from "RGBA" to "RGB" and converting from ".tiff" format to ".jpeg". The script used for that is present on the "Modifying_Images.py" file;

2 - After the modifications, the images were sent to a webserve API endpoint via HTTP POST method. This can be seen within the "Sending_Images.py" file;

3 - Following the process, a set of '.txt' files were provided \(files present in the "suplier_data" directory, within the directory "descriptions"\) containing descriptions to each of the images previouly uploaded to the server. Those description files were processed and their informations were stored into python dictionaries, which were then uploaded to another endpoint of the website, via HTTP POST method. The website then processed the information, displaying the images together with their repective descriptions. This script can be seen into the "Sending_Image_and_Description.py" file.

4 - Finishing the project, after uploading the contents to the website, a report stating which files were uploaded to the website, in a PDF format \(report can be seen by the name of "processed.pdf"\) was sent through email via SMTP connection. The script of the processed data, generation of report and email sending can be seen into "Sending_Report_through_Email.py", this script use functions for generating the report \(present in "Generating_PDF_Report.py"\) and sending the email \(present in Emails.py\).
