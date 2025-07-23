import pandas as pd

vendas = pd.read_csv("vendas.csv")
print("Média:", vendas["valor"].mean())
print("Desvio Padrão:", vendas["valor"].std())
print("Resumo:\n", vendas.describe())