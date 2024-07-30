# DESAFIO 016
# Crie um programa que leia um número real qualquer pelo teclado e mostre
# na tela sua porção inteira.
# Exemplo: Digite o número 6.127 e mostre a parte inteira, que é 6.
# Utilize o módulo math para obter a parte inteira do número.

import math  # Importa o módulo math para utilizar a função de arredondamento para baixo

n = float(input('Insira um número real: '))  # Solicita ao usuário que insira um número real e converte para float

p = math.floor(n)  # Calcula a parte inteira do número real usando a função floor do módulo math

# Exibe a parte inteira do número real
print('Parte inteira é {}'.format(p))

# Nota:
# - A função `math.floor()` arredonda o número real para o menor inteiro mais próximo, efetivamente extraindo a parte inteira.
# - O valor obtido será a porção inteira do número, descartando qualquer parte decimal.
