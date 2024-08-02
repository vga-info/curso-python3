# DESAFIO 026
# Faça um programa que leia uma frase pelo teclado e mostre:
# 1 - Quantas vezes aparece a letra "A"
# 2 - Em que posição ela aparece a primeira vez
# 3 - Em que posição ela aparece a ultima vez

# Lê uma frase digitada pelo usuário
frase = str(input('Digite uma frase: ').strip())

# Conta quantas vezes a letra "A" maiúscula aparece na frase
A = frase.count('A')
# Conta quantas vezes a letra "a" minúscula aparece na frase
a = frase.count('a')

# Soma as ocorrências de "A" e "a"
tot = A + a

# Mostra o total de letras "A" maiúsculas, "a" minúsculas e o total geral de ambas
print('Total de {} "A" (Maiúsculo)'.format(A))
print('Total de {} "a" (Minúsculo)'.format(a))
print('Total de "A"s encontrados {}'.format(tot))

# Mostra a posição da primeira ocorrência de "A" ou "a"
primeira_ocorrencia = frase.lower().find('a')
print('A letra "A" aparece pela primeira vez na posição {}'.format(primeira_ocorrencia + 1)) # Soma +1 pois começa no 0

# Mostra a posição da última ocorrência de "A" ou "a"
ultima_ocorrencia = frase.lower().rfind('a')
print('A letra "A" aparece pela última vez na posição {}'.format(ultima_ocorrencia + 1))
