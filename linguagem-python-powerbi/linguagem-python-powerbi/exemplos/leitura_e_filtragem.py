import pandas as pd

df = pd.read_csv("vendas.csv")
df_filtrado = df[df["estado"] == "SP"]
print(df_filtrado.head())