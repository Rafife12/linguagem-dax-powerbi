import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vendas.csv")
soma = df.groupby("produto")["valor"].sum()

soma.plot(kind="bar", color="skyblue")
plt.title("Total de Vendas por Produto")
plt.ylabel("Valor")
plt.xlabel("Produto")
plt.tight_layout()
plt.show()