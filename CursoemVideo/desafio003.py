print('===== DESAFIO 03 =====')
n1: int = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
#sintaxe antiga
print('A soma entre', n1, 'e', n2, 'vale', soma)
#sintaxe nova
print('A soma entre {} e {} vale {}'.format(n1,n2,soma))