library(dplyr)

dados <- read.csv("vendas.csv", sep = ";", encoding = "UTF-8")
vendas_sp <- dados %>% filter(estado == "SP") %>% group_by(produto) %>% summarise(total = sum(valor))
print(vendas_sp)