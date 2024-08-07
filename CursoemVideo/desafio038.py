# DESAFIO 038
# Escreva um programa que leia 'dois números' inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é MAIOR;
# O segundo valor é MAIOR;
# Não existe valor maior ou menor, os dois são IGUAIS.

# Solicita o primeiro número ao usuário
n1 = int(input('Digite o primeiro número: '))

# Solicita o segundo número ao usuário
n2 = int(input('Digite o segundo número: '))

# Compara os dois números e exibe a mensagem apropriada
if n1 > n2:
    # Se o primeiro número é maior que o segundo
    print('O primeiro é o maior valor!')
elif n2 > n1:
    # Se o segundo número é maior que o primeiro
    print('O segundo é o maior valor!')
else:
    # Se os números são iguais
    print('Os números são IGUAIS!')
