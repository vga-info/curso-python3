# DESAFIO 014
# Escreva um programa que converta uma temperatura digitada em ºC
# e converta para ºF (Fahrenheit).

c = float(input('Digite a temperatura em ºC: '))  # Solicita ao usuário a temperatura em graus Celsius e converte para float

# Converte a temperatura de Celsius para Fahrenheit usando a fórmula:
# Fahrenheit = (Celsius * 1.8) + 32
f = c * 1.8 + 32  # Calcula a temperatura em Fahrenheit

# Exibe a temperatura em Celsius e sua conversão para Fahrenheit
print('{}ºC corresponde a {}ºF'.format(c, f))

# Nota:
# - A fórmula para converter Celsius para Fahrenheit é multiplicar a temperatura em Celsius por 1.8 e adicionar 32.
# - A formatação da string permite que os valores sejam exibidos diretamente, sem a necessidade de formatação adicional.
