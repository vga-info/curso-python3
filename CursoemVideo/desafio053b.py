# DESAFIO 053
# Crie um programa que leia uma frase qualquer e diga se ela é
# um palindromo, desconsiderando os espaços.
# Exemplo: apos a sopa | a sacada da casa | a torre da derrota | o lobo ama o bolo
# anotaram a data da maratona

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo!')
