# DESAFIO 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite uma distância em metros: '))  # Solicita ao usuário que digite uma distância em metros e converte para float

c = n * 100  # Converte a distância de metros para centímetros
m = c * 10   # Converte a distância de centímetros para milímetros

# Exibe a distância em centímetros e milímetros
print('Centímetros: {} | Milímetros: {}'.format(c, m))
