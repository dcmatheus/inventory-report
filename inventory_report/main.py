import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    try:
        file_path, report_type = sys.argv[1], sys.argv[2]
        return InventoryRefactor.importer(file_path, report_type)
    except IndexError:
        sys.stderr.write("Verifique os argumentos\n")
