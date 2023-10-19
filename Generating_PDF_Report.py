#! /usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(filepath_name, title, body):
    """This function will generate a simple PDF file"""

    style = getSampleStyleSheet()   # Creating an instance with the standard layout for the PDF file.
    report = SimpleDocTemplate(filepath_name)   # Assigning the name and path which the file will be created.
    report_title = Paragraph(title, style['h1'])    # Defining the content and style for the title of the file.
    report_body = Paragraph(body, style['BodyText'])    # Defining the content and style for the body of the file.
    empty_line = Spacer(1, 20)  # Creating a space instance to be included in the file.

    report.build([report_title, empty_line, report_body])   # Generating the PDF using the previous information.
