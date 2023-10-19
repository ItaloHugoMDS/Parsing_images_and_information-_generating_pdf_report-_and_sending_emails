#! /usr/bin/env python3

from datetime import date
from Generating_PDF_Report import generate_report
from Sending_Image_and_Description import writing_dictionary
from Emails import generate_email, send_email

file_path = "/home/directory/supplier-data/descriptions/"    # This is the file path which the description of each image
# must be, so it can be processed and used as data to generate the PDF report.


def processing_data(file):
    """Processing the data which will the used as the content of the PDF report file."""
    report_data = ""    # This string will contain the message that will be the body of the pdf file.
    dictionaries = writing_dictionary(file)    # Retrieving a list of dictionary, which will contain the data to be
    # extracted and used as content of the PDF file.

    for dictionary in dictionaries:    # Going through each dictionary on the list:
        report_data += f"name: {dictionary['name']}<br/>weight: {dictionary['weight']} lbs<br/><br/>"   # Extracting
        # product's name as well as the product's weight and adding to the variable that will contain all the
        # information.

    return report_data  # Returning the string with all the extracted data.


def main():
    report_data = processing_data(file_path)    # Storing the string data to be used as content of the PDF file.
    title = "Processed Update on " + str(date.today().strftime("%B %d, %Y"))    # The string which will be the title of
    # the report file.
    dest_path = "/tmp/processed.pdf"  # Destiny path which also contains the name of the report file to be generated.
    host = "localhost"   # This is the host which will create SMTP connection to send the email.
    message_sender = "automation@example.com"   # The email address from which the message will be sent from.
    message_receiver = "student-04-330ff6fc5950@example.com"    # The email address from which the message
    # will be sent to.
    message_subject = "Upload Completed - Online Fruit Store"   # The subject of the email message.
    message_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    # The content of the email message.

    generate_report(dest_path, title, report_data)  # Generating the report.
    message = generate_email(message_sender, message_receiver, message_subject, message_body, dest_path)    # Creating
    # the email message to be sent.
    send_email(message, host)   # Sending the message via SMTP connection.


if __name__ == "__main__":
    main()
