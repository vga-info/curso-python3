# DESAFIO 053
# Crie um programa que leia uma frase qualquer e diga se ela é
# um palindromo, desconsiderando os espaços.
# Exemplo: apos a sopa | a sacada da casa | a torre da derrota | o lobo ama o bolo
# anotaram a data da maratona

# Solicita ao usuário que digite uma frase e armazena o valor na variável 'frase'
frase = input('Digite uma frase: ').strip()

# Remove os espaços da frase e armazena a versão limpa na variável 'fraselimpa'
fraselimpa = frase.replace(' ', '')

# Verifica se a versão limpa da frase é igual à sua inversa
if fraselimpa == fraselimpa[::-1]:
    print('É um Palíndromo')  # A frase é um palíndromo
else:
    print('Não é um Palíndromo')  # A frase não é um palíndromo