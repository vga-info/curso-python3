# DESAFIO 030
# CRIE UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU IMPAR.

# Solicita ao usuário um número inteiro
numero = int(input('Digite um numero inteiro: '))

# Calcula o resto da divisão do número por 2
resto = numero % 2

# Verifica se o resto é zero (o número é par), se nao, é impar
if resto == 0:
    print(f'O numero {numero} é Par')
else:
    print(f'O numero {numero} é Ímpar')
