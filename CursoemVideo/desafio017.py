# DESAFIO 017
# Faça um programa que leia o comprimento do cateto oposto
# e o cateto adjacente de um triângulo retângulo, calcule e mostre
# o comprimento da hipotenusa.
# Utilize o módulo math para calcular a hipotenusa.

import math  # Importa o módulo math para utilizar a função hypot

co = float(input('Digite o cateto oposto: '))  # Solicita ao usuário o comprimento do cateto oposto e converte para float
ca = float(input('Digite o cateto adjacente: '))  # Solicita ao usuário o comprimento do cateto adjacente e converte para float

# Calcula o comprimento da hipotenusa usando a função hypot do módulo math
h = math.hypot(co, ca)

# Exibe o comprimento da hipotenusa
print('A hipotenusa é: {}'.format(h))

# Nota:
# - A função `math.hypot(x, y)` calcula a hipotenusa de um triângulo retângulo com catetos x e y.
# - A fórmula utilizada é h = sqrt(co^2 + ca^2), onde `co` é o cateto oposto e `ca` é o cateto adjacente.
# - O resultado é o comprimento da hipotenusa do triângulo retângulo.
