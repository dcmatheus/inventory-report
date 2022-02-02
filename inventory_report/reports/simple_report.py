from datetime import datetime


def generate_fabrication_date(stock):
    date = set()
    for fabrication in stock:
        date.add(fabrication["data_de_fabricacao"])
    return min(date)


def generate_validate(stock):
    validate = set()
    atual_date = datetime.today()
    date_text = atual_date.strftime('%Y-%m-%d')

    for validate_date in stock:
        if validate_date["data_de_validade"] > date_text:
            validate.add(validate_date["data_de_validade"])
    return min(validate)


def generate_quantity_stock(stock):
    stock_by_company = []
    for product in stock:
        stock_by_company.append(product["nome_da_empresa"])
    return max(stock_by_company)


class SimpleReport:
    @staticmethod
    def generate(stock):
        message_fabrication = "Data de fabricação mais antiga:"
        message_validate = "Data de validade mais próxima:"
        message_stock = "Empresa com maior quantidade de produtos estocados:"
        return (
            f"{message_fabrication} {generate_fabrication_date(stock)}\n"
            f"{message_validate} {generate_validate(stock)}\n"
            f"{message_stock} {generate_quantity_stock(stock)}\n"
        )
