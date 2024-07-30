# DESAFIO 005
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))  # Solicita ao usuário que digite um número inteiro e converte para int

a = n - 1  # Calcula o antecessor do número
d = n + 1  # Calcula o sucessor do número

# Exibe o antecessor e o sucessor usando as variáveis 'a' e 'd'
print('Antecessor: {} | Sucessor: {}'.format(a, d))

# Outra forma de exibir o antecessor e o sucessor sem usar variáveis intermediárias
print('Antecessor: {} | Sucessor: {}'.format(n - 1, n + 1))
