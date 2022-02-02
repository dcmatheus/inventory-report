from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(file_path, report_type):
        product_list = []
        if file_path.lower().endswith(".json"):
            product_list.extend(JsonImporter.import_data(file_path))
        elif file_path.lower().endswith(".csv"):
            product_list.extend(CsvImporter.import_data(file_path))
        else:
            product_list.extend(XmlImporter.import_data(file_path))
        if report_type == "simples":
            return SimpleReport.generate(product_list)
        elif report_type == "completo":
            # return CompleteReport.generate(product_list)
            return "teste"
        raise ValueError("Tipo de relatório inválido")
