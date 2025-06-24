import xlsxwriter
import pandas as pd

def export_report(grouped_data, charts, output_path):
    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
    workbook = writer.book

    grouped_data["raw"].to_excel(writer, sheet_name="Base de Dados", index=False)

    summary_sheet = workbook.add_worksheet("Resumo")
    writer.sheets["Resumo"] = summary_sheet

    summary_sheet.write("A1", "Relatório de Vendas")

    row = 2
    for name, path in charts.items():
        summary_sheet.insert_image(row, 0, path, {"x_scale": 0.7, "y_scale": 0.7})
        row += 25

    writer.close()
