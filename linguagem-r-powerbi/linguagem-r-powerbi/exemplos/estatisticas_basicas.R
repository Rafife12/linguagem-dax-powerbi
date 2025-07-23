dados <- read.csv("vendas.csv", sep = ";", encoding = "UTF-8")
summary(dados$valor)
mean(dados$valor)
sd(dados$valor)