# DESAFIO 053
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplo: "apos a sopa", "a sacada da casa", "a torre da derrota", "o lobo ama o bolo", "anotaram a data da maratona".

# Solicita ao usuário que digite uma frase, remove espaços no início e no final e converte para maiúsculas.
frase = str(input('Digite uma frase: ')).strip().upper()

# Divide a frase em palavras, formando uma lista.
palavras = frase.split()

# Junta todas as palavras em uma única string, removendo os espaços.
junto = ''.join(palavras)

# Cria uma string vazia para armazenar o inverso da frase.
inverso = ''

# Itera sobre cada letra da string 'junto' de trás para frente.
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

# Verifica se a string original sem espaços e o seu inverso são iguais.
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo.')
