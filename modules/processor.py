import pandas as pd

def process_data(df):
    df['Data'] = pd.to_datetime(df['Data'])
    df['Ano-Mês'] = df['Data'].dt.to_period('M').astype(str)

    return {
        "por_periodo": df.groupby("Data")["Valor"].sum(),
        "por_produto": df.groupby("Produto")["Valor"].sum(),
        "por_vendedor": df.groupby("Vendedor")["Valor"].sum(),
        "raw": df
    }
