# DESAFIO 047
# Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 a 50.

# Loop para iterar sobre o intervalo de 2 a 50, considerando apenas os números pares.
for n in range(2, 51, 2):
    # O parâmetro 'end=' '' é utilizado para evitar a quebra de linha após cada número
    print(n, end=' ')

# Exibe a mensagem 'FIM' após a lista de números pares.
print('FIM')
