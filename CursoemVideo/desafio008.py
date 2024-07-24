# DESAFIO 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
n = float(input('Digite uma distancia em metros: '))
c = n * 100
m = c * 10
print('Centimetros: {} | Milimetros: {}'.format(c,m))
