import os
import re
from os import listdir
from os.path import isfile, join

import pdfkit

basedir = os.path.abspath(os.path.dirname(__file__))
reports_dir = os.path.abspath(os.path.join(basedir, os.pardir, "reports"))

pattern = "bericht_(\d+).pdf"


def save_report(rendered_template: str) -> str:
    reports = [f for f in listdir(reports_dir) if isfile(join(reports_dir, f))]

    filename = "bericht_0001.pdf"

    if len(reports) > 0:
        reports.sort(reverse=True)
        filename = reports[0]
        new_number = int(re.search(pattern, filename).group(1)) + 1

        filename = "bericht_" + str(new_number).zfill(4) + ".pdf"

    try:
        pdfkit.from_string(rendered_template, resolve_report_file(filename))
    except IOError as e:
        # wkhtmltopdf and pdfkit are so broken... Works anyway
        print("pdfkit failed: ", e)
    return filename


def resolve_report_file(filename):
    return os.path.join(reports_dir, filename)
