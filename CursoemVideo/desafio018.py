# DESAFIO 018
# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.
# Utilize o módulo math para calcular as funções trigonométricas.

import math  # Importa o módulo math para utilizar as funções trigonométricas

a = float(input('Insira um ângulo: '))  # Solicita ao usuário que insira um ângulo em graus e converte para float

# Converte o ângulo de graus para radianos, pois as funções trigonométricas do módulo math utilizam radianos
a_rad = math.radians(a)

# Calcula o seno, cosseno e tangente do ângulo
s = math.sin(a_rad)  # Calcula o seno do ângulo em radianos
c = math.cos(a_rad)  # Calcula o cosseno do ângulo em radianos
t = math.tan(a_rad)  # Calcula a tangente do ângulo em radianos

# Exibe o valor do seno, cosseno e tangente do ângulo
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(s, c, t))

# Nota:
# - As funções `math.sin()`, `math.cos()` e `math.tan()` requerem o ângulo em radianos.
# - A função `math.radians()` é usada para converter o ângulo de graus para radianos.
# - {:.2f} na formatação da string é utilizado para exibir os valores com duas casas decimais.
