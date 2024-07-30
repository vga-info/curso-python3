# AULA 006B
# O objetivo deste programa é solicitar ao usuário que insira um valor numérico decimal
# e exibir esse valor na tela.

# Solicita ao usuário que insira um valor e o converte para um número de ponto flutuante (float).
n = float(input('Digite um valor: '))  # A função input() captura a entrada do usuário como uma string. float() converte a string para um número decimal.

# Exibe o valor digitado pelo usuário.
print(n)  # O comando print() exibe o valor armazenado na variável 'n'.

# Nota:
# - `input()` sempre retorna uma string, então é necessário converter a entrada para um tipo numérico usando `float()` se for necessário lidar com números decimais.
# - O `print()` é utilizado para mostrar a saída no console. Neste caso, ele exibe o valor numérico que foi convertido a partir da entrada do usuário.
