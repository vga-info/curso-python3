# DESAFIO 051
# Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética (PA)
# No final, mostre os 10 primeiros termos dessa progressão

# Lê o primeiro termo da PA e a razão da progressão
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

# Número de termos que queremos exibir
num_termos = 10

# Exibe os 10 primeiros termos da PA
print('Os 10 primeiros termos da PA são:')
for i in range(num_termos):
    termo_atual = primeiro_termo + i * razao  # Calcula o termo atual
    print(termo_atual, end=' ')  # Exibe o termo atual na mesma linha, separado por espaço

print()  # Quebra de linha após listar todos os termos
