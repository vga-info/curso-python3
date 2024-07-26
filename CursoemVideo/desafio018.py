# DESAFIO 018
# Faça um programa que leia um angulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse angulo
import math

a = float(input('Insira um angulo: '))
s = math.sin(a)
c = math.cos(a)
t = math.tan(a)
print('Seno: {}\nCosseno: {}\nTangente: {}'.format(s,c,t))
