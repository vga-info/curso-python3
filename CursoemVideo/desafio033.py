# DESAFIO 033
# FAÇA UM PROGRAMA QUE LEIA 3 NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR.

# Solicita ao usuário que insira três números
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))

# Verifica qual é o maior número
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

# Verifica qual é o menor número
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3

print('Menor numero: {}'.format(menor))
print('Maior numero: {}'.format(maior))
