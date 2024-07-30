# AULA 008A

# Importa a função sqrt (raiz quadrada) do módulo math para realizar cálculos matemáticos.
from math import sqrt  # O módulo math fornece funções matemáticas, e sqrt é usado para calcular a raiz quadrada de um número.

# Importa o módulo emoji, que permite usar emojis no código. Neste exemplo, não está sendo utilizado.
import emoji  # O módulo emoji é útil para adicionar emojis em textos, mas não é utilizado neste código.

# Solicita ao usuário que digite um número e o converte para um tipo inteiro.
num = int(input('Digite um número: '))  # A função input() captura a entrada do usuário como uma string. int() converte a string para um número inteiro.

# Calcula a raiz quadrada do número digitado.
raiz = sqrt(num)  # A função sqrt() do módulo math calcula a raiz quadrada do número fornecido.

# Exibe a raiz quadrada do número digitado, formatando o resultado para duas casas decimais.
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
# {} é um placeholder no método format() que será substituído pelo valor das variáveis fornecidas.
# {:.2f} é um especificador de formato que limita a exibição do número para 2 casas decimais.

# Nota:
# - O método format() é usado para inserir valores em uma string e também permite formatar a exibição dos números.
# - A função sqrt() só pode ser usada com números não negativos, pois a raiz quadrada de um número negativo não é um número real.
