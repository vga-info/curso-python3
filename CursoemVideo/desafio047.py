# DESAFIO 047
# Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 a 50

# Laço de repetição que vai de 0 até 50 (inclusive)
for c in range(1, 51):
    # Verifica se o número atual 'c' é par usando o operador módulo (%)
    if c % 2 == 0:
        print(c, end=' ')  # Se o número for par, ele é exibido na tela

print('FIM')  # Exibe a mensagem final após a contagem
