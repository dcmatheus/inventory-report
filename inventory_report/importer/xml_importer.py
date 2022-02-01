import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_path):
        if file_path.lower().endswith(".xml"):
            product_list = []
            with open(file_path) as file:
                for record in ET.parse(file).getroot():
                    obj = {}
                    for key in record:
                        obj[key.tag] = key.text
                    product_list.append(obj)
            return product_list
        raise ValueError("Arquivo inválido")
