# DESAFIO 053
# Crie um programa que leia uma frase qualquer e diga se ela é
# um palindromo, desconsiderando os espaços.
# Exemplo: apos a sopa | a sacada da casa | a torre da derrota | o lobo ama o bolo
# anotaram a data da maratona

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase nao é um palíndromo.')
