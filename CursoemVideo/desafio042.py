# DESAFIO 042
# Refaça o 'Desafio 035' dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: TODOS OS LADOS IGUAIS
# - ISÓSCELES: DOIS LADOS IGUAIS
# - ESCALENO: TODOS OS LADOS DIFERENTES

# Solicita ao usuário o comprimento das três retas
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

# Verifica se as retas podem formar um triângulo usando a desigualdade triangular
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    # Determina o tipo de triângulo com base no comprimento dos lados
    if r1 == r2 == r3:
        tipo = 'Equilátero'  # Todos os lados são iguais
    elif r1 != r2 and r2 != r3 and r1 != r3:
        tipo = 'Escaleno'  # Todos os lados são diferentes
    else:
        tipo = 'Isósceles'  # Dois lados são iguais
    print('É possível formar um Triângulo {}.'.format(tipo))
else:
    print('Não é possível formar um Triângulo.')
