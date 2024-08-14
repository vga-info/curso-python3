# DESAFIO 055
# Faça um programa que leia o peso de 5 pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0  # Inicializa a variável para o maior peso
menor = float('inf')  # Inicializa a variável para o menor peso com infinito para garantir que qualquer peso seja menor

for c in range(1, 6):  # Loop para ler o peso de 5 pessoas
    peso = float(input('Digite um peso: '))  # Lê o peso da pessoa

    if peso > maior:  # Verifica se o peso atual é maior que o maior peso registrado
        maior = peso  # Atualiza o maior peso

    if peso < menor:  # Verifica se o peso atual é menor que o menor peso registrado
        menor = peso  # Atualiza o menor peso

print('Maior peso: {:.2f}'.format(maior))  # Exibe o maior peso com duas casas decimais
print('Menor peso: {:.2f}'.format(menor))  # Exibe o menor peso com duas casas decimais
