# DESAFIO 054
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# CONSIDERE MAIORIDADE COM 21 ANOS

import datetime

# Contador para pessoas menores de 21 anos
menor_de_idade = 0

# Loop para ler o ano de nascimento de 7 pessoas
for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = datetime.date.today().year - nasc

    # Verifica se a idade é menor que 21
    if idade < 21:
        menor_de_idade += 1

# Exibe o número de pessoas que ainda não atingiram a maioridade
print(f'Número de pessoas que ainda não atingiram a maioridade: {menor_de_idade}')
