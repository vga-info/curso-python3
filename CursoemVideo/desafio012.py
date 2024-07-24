# DESAFIO 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto
p = float(input("Preço do produto: "))
d = float(input("% de Desconto: "))
v = p-(p/100*d)
print('Valor do produto com {:.2f}% de desconto: R${:.2f}'.format(d,v))
