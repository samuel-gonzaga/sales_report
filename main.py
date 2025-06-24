from modules.reader import read_spreadsheets
from modules.processor import process_data
from modules.visualizer import generate_charts
from modules.exporter import export_report
from utils.timer import measure_time
from config import OUTPUT_FILE

@measure_time
def run():
    df = read_spreadsheets("input/")
    grouped_data = process_data(df)
    charts = generate_charts(grouped_data)
    output_path = OUTPUT_FILE if OUTPUT_FILE else "output/relatorio_vendas.xlsx"
    export_report(grouped_data, charts, output_path=output_path)
if __name__ == "__main__":
    run()
