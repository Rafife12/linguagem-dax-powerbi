library(ggplot2)

dados <- data.frame(produto = c("A", "B"), total = c(100, 200))
ggplot(dados, aes(x = produto, y = total)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  theme_minimal()