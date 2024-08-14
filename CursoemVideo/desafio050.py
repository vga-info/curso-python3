# DESAFIO 050
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
# forem pares. Se o valor digitado for ímpar, desconsidere-o.

# Inicializa a variável 'soma' com valor 0, que irá acumular a soma dos números pares
soma = 0

# Loop que irá executar 6 vezes, permitindo ao usuário digitar 6 números
for c in range(1, 7):
    numero = int(input('Digite um número: '))  # Solicita ao usuário que digite um número inteiro
    if numero % 2 == 0:  # Verifica se o número é par (resto da divisão por 2 é zero)
        soma += numero  # Adiciona o número par à variável 'soma'

# Exibe a soma de todos os números pares digitados
print('A soma dos números pares é: {}'.format(soma))
