# DESAFIO 005
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número: '))
a = n - 1
d = n + 1
print('Antecessor: {} | Sucessor: {}'.format(a,d))
#tambem pode ser escrito sem usar variaveis de operação
print('Antecessor: {} | Sucessor: {}'.format(a, (n-1), (n+1)))