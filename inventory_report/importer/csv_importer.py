import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_path):
        if file_path.lower().endswith(".csv"):
            product_list = []
            with open(file_path) as file:
                dicts = csv.DictReader(file, delimiter=",", quotechar='"')
                for row in dicts:
                    product_list.append(row)
            return product_list
        raise ValueError("Arquivo inválido")
