# O objetivo deste programa é solicitar o nome do usuário e exibir uma mensagem de boas-vindas de duas maneiras diferentes.

nome = input('Qual seu nome? ')  # Solicita ao usuário que insira seu nome e armazena o valor fornecido na variável 'nome'.
# input() é uma função que captura a entrada do usuário e retorna uma string.

print('É um prazer te conhecer', nome, '.')  # Exibe uma mensagem de boas-vindas usando a variável 'nome'.
# O comando print() pode aceitar múltiplos argumentos e os separa por espaços por padrão.

print('ou')  # Exibe a palavra 'ou' para separar as duas formas de exibição da mensagem.

print('É um prazer te conhecer, {}.'.format(nome))  # Exibe a mesma mensagem usando o método format().
# {} é um marcador de posição que é substituído pelo valor da variável 'nome' especificada em .format().
# O método .format() é usado para formatar strings, permitindo a inserção de variáveis no texto.

# Nota:
# - `input()` lê a entrada do usuário e a armazena como uma string.
# - O método `print()` pode ser usado para exibir múltiplos valores separados por espaços.
# - O método `format()` permite a substituição de {} por variáveis ou valores passados como argumento, facilitando a formatação de strings.
