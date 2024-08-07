# DESAFIO 041
# A Confederação Nacional de Natação precisa de um programa que leia a idade do atleta e mostre sua
# categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - 20 anos: SÊNIOR
# - Acima de 20 anos: MASTER

# Solicita a idade do atleta
idade = int(input('Digite a idade do Atleta: '))

# Determina a categoria com base na idade do atleta
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade == 20:  # Exatamente 20 anos
    print('Categoria SÊNIOR')
else:  # Acima de 20 anos
    print('Categoria MASTER')
