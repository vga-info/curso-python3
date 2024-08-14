# DESAFIO 051
# Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética (PA).
# No final, mostre os 10 primeiros termos dessa progressão.

# Solicita o primeiro termo da PA ao usuário.
primeiro = int(input('Primeiro termo: '))
# Solicita a razão da PA ao usuário.
razao = int(input('Razão: '))

# Calcula o décimo termo da PA usando a fórmula: décimo = primeiro + (n-1) * razão
decimo = primeiro + (10 - 1) * razao

# Itera sobre a PA para exibir os 10 primeiros termos.
for c in range(primeiro, decimo + razao, razao):
    # Exibe cada termo seguido de uma seta.
    print('{} '.format(c), end=' -> ')

# Exibe "FIM" após a lista de termos.
print('FIM')
