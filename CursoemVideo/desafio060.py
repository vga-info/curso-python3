'''from math import factorial'''  # Apenas para controle (opcional, caso queira comparar com a função pronta)

numero = int(input('Digite um número: '))  # Solicita ao usuário que insira um número

'''print('Fatorial de {} é {}'.format(numero,factorial(numero)))'''  # Controle opcional para verificar com a função math.factorial

calc = numero - 1  # Inicializa a variável 'calc' com o número inserido menos 1
fatorial = numero  # Começa o fatorial com o valor do número inserido

# Enquanto 'calc' não for igual a 1, continua multiplicando para calcular o fatorial
while calc != 1:
    fatorial = (fatorial * calc)  # Multiplica o valor atual do fatorial pelo valor de 'calc'
    calc -= 1  # Decrementa 'calc' em 1

# Exibe o resultado do fatorial
print('Fatorial de {} é {}'.format(numero, fatorial))
