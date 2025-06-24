import pandas as pd
import os

def read_spreadsheets(folder_path):
    all_data = []
    for file in os.listdir(folder_path):
        if file.endswith(".xlsx"):
            df = pd.read_excel(os.path.join(folder_path, file))
            all_data.append(df)
    return pd.concat(all_data, ignore_index=True)
