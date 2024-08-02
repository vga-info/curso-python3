# DESAFIO 025
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

# Lê o nome completo do usuário
nome = input('Digite um nome completo: ')

# Converte o nome para minúsculas para garantir a comparação case-insensitive
minuscula = nome.lower()

# Verifica se a substring "silva" está presente no nome
result = minuscula.find('silva')
# outra opção é usando o 'in' retornando True ou False
result2 = 'silva' in minuscula

# O método find() retorna -1 se a substring não for encontrada, e um índice >= 0 se for encontrada
if result != -1: # !=
    print('Tem "Silva" no nome')
else:
    print('Não tem "Silva" no nome')

if result2:
    print('Tem "Silva" no nome')
else:
    print('Não tem "Silva" no nome')