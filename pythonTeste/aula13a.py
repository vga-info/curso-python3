# Exemplo de repetição manual
# Aqui, o comando print é repetido manualmente três vezes
print('oi')
print('oi')
print('oi')
print('FIM da repetição manual\n\n')

# Exemplo de repetição automática usando for
# O laço for repete o comando print 6 vezes
for c in range(0, 6):  # range(0, 6) cria uma sequência de 0 a 5
    print('oi')  # Cada iteração do laço imprime 'oi'
print('FIM do laço\n\n')

# Contagem de 0 até 5
# O laço for conta de 0 a 5 e imprime cada número
for c in range(0, 6):  # range(0, 6) cria uma sequência de 0 a 5
    print(c)  # Imprime o valor atual de c em cada iteração
print('FIM\n\n')

# Contagem de 6 até 1
# O laço for conta de 6 até 1, diminuindo 1 a cada iteração
for c in range(6, 0, -1):  # range(6, 0, -1) conta de 6 até 1, decrementando 1
    print(c)  # Imprime o valor atual de c em cada iteração
print('FIM \n\n')

# Contagem de 0 até 6, pulando de 2 em 2
for c in range(0, 7, 2):  # range(0, 7, 2) conta de 0 até 6, incrementando 2 a cada passo
    print(c)  # Imprime o valor atual de c em cada iteração
print('FIM \n\n')

# Exemplo de laço for com entrada do usuário
n = int(input('Digite um número: '))  # Solicita um número ao usuário
for c in range(0, n+1):  # Conta de 0 até n (inclusivo)
    print(c)  # Imprime o valor atual de c em cada iteração
print('FIM\n\n')

# Laço for com início, fim e passo definidos pelo usuário
inicio = int(input('Início: '))  # Solicita o valor inicial ao usuário
fim = int(input('Fim: '))  # Solicita o valor final ao usuário
passo = int(input('Passo: '))  # Solicita o valor do passo (incremento) ao usuário
for c in range(inicio, fim+1, passo):  # Conta de 'inicio' até 'fim', usando o 'passo' definido pelo usuário
    print(c)  # Imprime o valor atual de c em cada iteração
print('FIM\n\n')

# Exemplo de somatório usando for
s = 0  # Variável para armazenar a soma
# O laço for será executado 4 vezes, solicitando 4 valores ao usuário
for c in range(0, 4):  # range(0, 4) cria uma sequência de 0 a 3
    n = int(input('Digite um valor: '))  # Solicita um valor ao usuário
    s += n  # Adiciona o valor inserido à variável '
