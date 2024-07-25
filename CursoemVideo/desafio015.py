# DESAFIO 015
# Escreva um programa que pergunte a quantidade de KM percorrido por um carro
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia
# e R$0,15 por KM rodado
d = int(input('Quantos dias alugado? '))
km = float(input('Quantos KM Rodados? '))
p = (d * 60)+(km * 0.15)
print('Total a pagar: R${:.2f}'.format(p))
