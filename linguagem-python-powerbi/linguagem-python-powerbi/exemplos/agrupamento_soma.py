import pandas as pd

df = pd.read_csv("vendas.csv")
soma = df.groupby("produto")["valor"].sum()
print(soma)