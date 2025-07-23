# Linguagem DAX (Data Analysis Expressions) - Power BI

Este repositório contém exemplos práticos, funções e explicações sobre a **Linguagem DAX**, usada no Power BI, Excel (Power Pivot) e Analysis Services.

---

## 📌 Sobre a Linguagem DAX

- Linguagem de fórmulas para modelos tabulares
- Mistura conceitos de Excel, SQL e funções analíticas
- Usada para criar **medidas**, **colunas calculadas** e **tabelas**
- Poderosa para análise de dados e inteligência de tempo

---

## 🧪 Exemplos de Código

### 🔢 Medida - Soma Total

```dax
Total Vendas = SUM(Vendas[Valor])
```

### 🗓️ Coluna - Mês por extenso

```dax
Mes = FORMAT(Vendas[Data], "MMMM")
```

### 🔍 Medida com filtro

```dax
Vendas SP = CALCULATE(
    SUM(Vendas[Valor]),
    Vendas[Estado] = "SP"
)
```

### 📈 Crescimento Anual

```dax
Crescimento = 
VAR VendasAtual = SUM(Vendas[Valor])
VAR VendasAnterior = CALCULATE(SUM(Vendas[Valor]), SAMEPERIODLASTYEAR('Calendario'[Data]))
RETURN DIVIDE(VendasAtual - VendasAnterior, VendasAnterior)
```

---

## 🔧 Funções Comuns

| Categoria       | Exemplos                                 |
|----------------|-------------------------------------------|
| Agregação      | `SUM`, `AVERAGE`, `MAX`, `MIN`            |
| Filtro         | `CALCULATE`, `FILTER`, `ALL`              |
| Tempo          | `DATESYTD`, `SAMEPERIODLASTYEAR`, `DATEADD` |
| Texto          | `LEFT`, `RIGHT`, `CONCATENATE`, `FORMAT`  |
| Relacionamento | `RELATED`, `RELATEDTABLE`                 |

---

## 🎯 Objetivo

Este repositório serve como guia de referência para:

- Criar cálculos e indicadores personalizados
- Automatizar análises com inteligência de tempo
- Estudar a linguagem DAX com exemplos reais

---

## 📘 Recursos Úteis

- [Documentação Oficial DAX - Microsoft](https://learn.microsoft.com/pt-br/dax/)
- [Guia DAX Studio](https://daxstudio.org/)

---

## 🧑‍💻 Autor

**Rafael Silva**  
[LinkedIn](https://www.linkedin.com/) | [GitHub](https://github.com/)
