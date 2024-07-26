# DESAFIO 016
# Crie um programa que leia um número Real qualquer pelo teclado e mostre
# na tela sua porção inteira
# Ex: Digite o numero 6.127 e mostre a parte inteira, que é 6
# Use Math
import math
n = float(input('Insira um numero real: '))
p = math.floor(n)
print('Parte inteira é {}'.format(p))
