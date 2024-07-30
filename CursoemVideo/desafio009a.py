# DESAFIO 009
# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

#versão alternativa usando loop para gerar a tabuada

n = int(input('Digite um número INTEIRO: '))  # Solicita ao usuário que digite um número inteiro e converte para int

# Exibe a tabuada do número fornecido usando um loop
print('Tabuada de {}'.format(n))
for i in range(1, 11):  # Itera de 1 a 10
    print('{} x {} = {}'.format(n, i, n * i))
