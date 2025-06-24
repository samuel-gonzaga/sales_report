import matplotlib.pyplot as plt
import os

def generate_charts(grouped_data):
    charts = {}
    os.makedirs("output/images", exist_ok=True)

    def save_plot(name, plot_func):
        plt.figure(figsize=(10, 6))  # Aumenta o tamanho da figura
        plot_func()
        plt.tight_layout()  # Evita cortes nos rótulos
        path = f"output/images/{name}.png"
        plt.savefig(path)
        plt.close()
        charts[name] = path

    # Gráfico de linha
    save_plot("vendas_por_periodo", lambda: grouped_data["por_periodo"].plot(title="Vendas por Período"))

    # Gráfico de barras com rotação dos rótulos do eixo X
    def plot_vendas_por_produto():
        ax = grouped_data["por_produto"].plot(kind="bar", title="Vendas por Produto")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

    save_plot("vendas_por_produto", plot_vendas_por_produto)

    # Gráfico de pizza
    def plot_vendas_por_vendedor():
        grouped_data["por_vendedor"].plot.pie(autopct='%1.1f%%', title="Porcentagem por Vendedor")
        plt.ylabel('')  # Remove o label do eixo Y

    save_plot("vendas_por_vendedor", plot_vendas_por_vendedor)

    return charts
