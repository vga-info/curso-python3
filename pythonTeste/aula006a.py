# AULA 006A
# O objetivo deste programa é solicitar ao usuário dois números inteiros,
# calcular a soma desses números e exibir o resultado de duas maneiras diferentes.

# Solicita ao usuário que insira o primeiro número e o converte para um inteiro.
n1: int = int(input('Digite um número: '))  # A função input() captura a entrada do usuário como uma string. int() converte a string para um número inteiro.

# Solicita ao usuário que insira o segundo número e o converte para um inteiro.
n2 = int(input('Digite outro número: '))  # A mesma conversão é aplicada para o segundo número.

# Calcula a soma dos dois números.
soma = n1 + n2  # Adiciona os valores das variáveis 'n1' e 'n2' e armazena o resultado na variável 'soma'.

# Exibe a soma dos números de forma simples, com valores separados por espaços.
print('A soma entre', n1, 'e', n2, 'vale', soma)  # O comando print() exibe a mensagem e os valores das variáveis separados por espaços padrão.

# Exibe a soma dos números usando formatação de string.
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))  # O método format() substitui os {} pelos valores das variáveis passadas como argumentos.

# Nota:
# - `input()` sempre retorna uma string, então é necessário converter a entrada para um tipo numérico usando `int()` se for realizar operações matemáticas.
# - O método `print()` pode ser usado para exibir valores diretamente, mas o método `format()` oferece mais controle sobre a formatação da string.
# - A sintaxe `{}.format()` é uma forma de formatar strings que facilita a inclusão de variáveis no texto. Alternativamente, f-strings podem ser usadas para uma sintaxe mais moderna e direta.
