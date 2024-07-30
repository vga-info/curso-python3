# AULA 007A
# O objetivo deste programa é realizar e exibir os resultados de várias operações matemáticas
# com dois números inteiros fornecidos pelo usuário.

# Solicita ao usuário que insira dois valores inteiros.
n1 = int(input('Um valor: '))  # A função input() captura a entrada do usuário como uma string. int() converte a string para um número inteiro.
n2 = int(input('Outro valor: '))  # A mesma conversão é aplicada para o segundo valor.

# Realiza e exibe as operações matemáticas diretamente dentro do método format().
print('Soma {}'.format(n1 + n2))  # Exibe a soma dos dois números.
print('Subtração {}'.format(n1 - n2))  # Exibe a subtração do segundo número do primeiro.
print('Multiplicação {}'.format(n1 * n2))  # Exibe o produto dos dois números.
print('Divisão {:.3f}'.format(n1 / n2))  # Exibe a divisão dos dois números, formatada para mostrar 3 casas decimais. {:.3f} é um especificador de formato que limita a saída a 3 casas decimais.
print('Potência {}'.format(n1 ** n2))  # Exibe o resultado da potência do primeiro número elevado ao segundo.
print('Divisão Inteira {}'.format(n1 // n2))  # Exibe o resultado da divisão inteira dos dois números, que descarta a parte decimal.
print('Resto da Divisão Inteira {}'.format(n1 % n2))  # Exibe o resto da divisão inteira dos dois números.

# Calcula as operações e armazena os resultados em variáveis.
soma = n1 + n2  # Armazena a soma dos dois números.
subt = n1 - n2  # Armazena a subtração do segundo número do primeiro.
mult = n1 * n2  # Armazena o produto dos dois números.
div = n1 / n2  # Armazena o resultado da divisão dos dois números.
pot = n1 ** n2  # Armazena o resultado da potência do primeiro número elevado ao segundo.
divint = n1 // n2  # Armazena o resultado da divisão inteira dos dois números.
resdiv = n1 % n2  # Armazena o resto da divisão inteira dos dois números.

# Exibe os resultados de todas as operações em uma única linha, formatando o valor da divisão para mostrar 3 casas decimais e incluindo quebras de linha (\n).
print('A soma é {}, a subtração é {}, a multiplicação é {}, a divisão é {:.3f},\n a potência é {}, a divisão inteira é {} e o resto da divisão inteira é {}'
      .format(soma, subt, mult, div, pot, divint, resdiv))

# Nota:
# - O método `format()` é usado para inserir variáveis dentro das strings de forma formatada.
# - O especificador de formato {:.3f} é utilizado para limitar o número de casas decimais exibidas.
# - `\n` é um caractere de nova linha que adiciona quebras de linha na saída, melhorando a legibilidade.
