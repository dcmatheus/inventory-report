import json
import csv
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def readJSON(file_path):
    product_list = []
    with open(file_path) as file:
        content = file.read()
        product_list.extend(json.loads(content))
    return product_list


def readCSV(file_path):
    product_list = []
    with open(file_path) as file:
        dicts = csv.DictReader(file, delimiter=",", quotechar='"')
        for row in dicts:
            product_list.append(row)
    return product_list


def readXML(file_path):
    product_list = []
    with open(file_path) as file:
        for record in ET.parse(file).getroot():
            obj = {}
            for key in record:
                obj[key.tag] = key.text
            product_list.append(obj)
    return product_list


class Inventory:
    @staticmethod
    def import_data(file_path, report_type):
        product_list = []
        if file_path.lower().endswith(".json"):
            product_list.extend(readJSON(file_path))
        elif file_path.lower().endswith(".csv"):
            product_list.extend(readCSV(file_path))
        elif file_path.lower().endswith(".xml"):
            product_list.extend(readXML(file_path))
        if report_type == "simples":
            return SimpleReport.generate(product_list)
        return CompleteReport.generate(product_list)
