# AULA 14

# Exemplo 1: Comparando for e while para uma contagem simples
for c in range(1, 10):  # Usando for (ideal quando se sabe o limite)
    print(c)
print('fim')

c = 1
while c < 10:  # Usando while (útil tanto para limites conhecidos quanto desconhecidos)
    print(c)
    c += 1  # Incrementa c em 1 a cada iteração
print('fim')

# Exemplo 2: Lendo valores com for e while
for c in range(1, 5):  # Usando for para ler 4 números (limite conhecido)
    n = int(input('Digite um valor: '))
print('fim')

n = 1
while n != 0:  # Usando while para ler números até que o usuário digite 0 (limite desconhecido)
    n = int(input('Digite um valor: '))
print('fim')

# Exemplo 3: Controle de fluxo com uma variável de condição
r = 'S'
while r == 'S':  # Usando while para continuar solicitando números enquanto o usuário desejar
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()  # Pergunta se o usuário deseja continuar
print('fim')

# Exemplo 4: Contagem de números pares e ímpares
n = 1
par = impar = 0
while n != 0:  # O loop continua até que o usuário digite 0
    n = int(input('Digite um valor: '))
    if n != 0:  # Ignora o zero na contagem
        if n % 2 == 0:  # Verifica se o número é par
            par += 1
        else:  # Se não for par, é ímpar
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
print('Acabou')
