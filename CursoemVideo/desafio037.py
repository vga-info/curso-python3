# DESAFIO 037
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

# Solicita ao usuário o número inteiro a ser convertido
num = int(input('Digite um número inteiro: '))

# Solicita ao usuário escolher a base de conversão
base = int(input('Qual a base para conversão? (digite o número da opção)\n1 - Binário\n2 - Octal\n3 - Hexadecimal\nOpção: '))

# Verifica a opção escolhida e realiza a conversão correspondente
if base == 1:
    # Converte o número para binário e exibe o resultado
    print('{} em binário é: {}'.format(num, bin(num)[2:]))  # [2:] remove o prefixo '0b'
elif base == 2:
    # Converte o número para octal e exibe o resultado
    print('{} em octal é: {}'.format(num, oct(num)[2:]))  # [2:] remove o prefixo '0o'
elif base == 3:
    # Converte o número para hexadecimal e exibe o resultado
    print('{} em hexadecimal é: {}'.format(num, hex(num)[2:].upper()))  # [2:] remove o prefixo '0x' e .upper() para letras maiúsculas
else:
    # Exibe uma mensagem de erro se a opção for inválida
    print('Opção "{}" é inválida! Tente novamente.'.format(base))  # Corrigido para mostrar a opção inválida
