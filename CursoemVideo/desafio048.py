# DESAFIO 048
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
# e que se encontram no intervalo de 1 até 500

soma = 0  # Inicializa a variável soma com 0
for c in range(1, 501):  # Laço que percorre os números de 1 a 500 (inclusive)
    if c % 2 != 0 and c % 3 == 0:  # Verifica se o número é ímpar e múltiplo de 3
        soma += c  # Soma o número à variável soma
print('A soma dos números ímpares múltiplos de 3 no intervalo de 1 até 500 é {}'.format(soma))
