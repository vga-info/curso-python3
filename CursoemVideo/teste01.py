
# O objetivo deste programa é solicitar ao usuário seu nome, idade e peso,
# e exibir essas informações na tela.

nome = input('Qual é o seu nome? ')  # Solicita ao usuário que insira seu nome e armazena o valor fornecido na variável 'nome'.
# input() é uma função que captura a entrada do usuário como uma string.

idade = input('Qual sua idade? ')  # Solicita ao usuário que insira sua idade e armazena o valor fornecido na variável 'idade'.
# A entrada também é armazenada como uma string.

peso = input('Qual seu peso? ')  # Solicita ao usuário que insira seu peso e armazena o valor fornecido na variável 'peso'.
# A entrada é armazenada como uma string.

print(nome, idade, peso)  # Exibe as informações fornecidas pelo usuário. O comando print() separa os valores por espaços por padrão.
# Neste caso, os valores das variáveis 'nome', 'idade' e 'peso' são exibidos na mesma linha.

# Nota:
# - A função `input()` sempre retorna uma string, mesmo que o usuário insira números. Se for necessário realizar cálculos ou validações numéricas, a conversão de tipo será necessária.
# - `print(nome, idade, peso)` exibe as variáveis separadas por espaços, mas não formata a saída. Para uma exibição mais detalhada ou formatada, o método `format()` ou f-strings podem ser usados.
