# DESAFIO 049
# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher
# só que agora utilizando um laço for.

n = int(input('Digite um número INTEIRO: '))  # Solicita ao usuário que digite um número inteiro e converte para int

# Exibe a tabuada do número fornecido usando um loop
print('Tabuada de {}'.format(n))
for i in range(1, 11):  # Itera de 1 a 10
    print('{} x {} = {}'.format(n, i, n * i))  # Mostra a multiplicação do número fornecido pelo índice
