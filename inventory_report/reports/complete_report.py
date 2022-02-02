from inventory_report.reports.simple_report import SimpleReport


def products_for_company(stock):
    company_stock = {}
    for products in stock:
        if products["nome_da_empresa"] not in company_stock:
            company_stock[products["nome_da_empresa"]] = 1
        else:
            company_stock[products["nome_da_empresa"]] += 1
    stock_products = ""
    company = company_stock.items()
    for prod in company:
        stock_products += (f"- {prod[0]}: {prod[1]}\n")

    return stock_products


class CompleteReport:
    @staticmethod
    def generate(stock):
        return (
            f"{SimpleReport.generate(stock)}\n"
            "Produtos estocados por empresa: \n"
            f"{products_for_company(stock)}"
        )
