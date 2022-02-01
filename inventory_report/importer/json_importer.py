import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_path):
        if file_path.lower().endswith(".json"):
            product_list = []
            with open(file_path) as file:
                content = file.read()
                product_list.extend(json.loads(content))
            return product_list
        raise ValueError("Arquivo inválido")
