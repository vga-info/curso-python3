# DESAFIO 052
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input('Digite um número inteiro: '))  # Solicita um número inteiro do usuário

# O número 1 não é considerado primo, e números menores que 2 não são primos
if num <= 1:
    print('{} não é Primo!'.format(num))
else:
    result = 0  # Inicializa uma variável para contar o número de divisores
    for c in range(2, num):  # Verifica divisores de 2 até num-1
        if num % c == 0:  # Se num é divisível por c, então c é um divisor
            result += 1  # Incrementa o contador de divisores
            break  # Não é necessário continuar verificando se já encontramos um divisor

    if result == 0:  # Se não encontramos divisores, o número é primo
        print('{} é Primo!'.format(num))
    else:
        print('{} não é Primo!'.format(num))
