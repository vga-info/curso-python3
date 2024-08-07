# DESAFIO 040
# Cria um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
# média atingida:
# - média abaixo de 5.0: REPROVADO.
# - entre 5.0 e 6.9: RECUPERAÇÃO
# - 7.0 ou superior: APROVADO

# Solicita as duas notas do aluno
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

# Calcula a média das notas
media = (n1 + n2) / 2

# Exibe a média formatada e a situação do aluno com base na média
if media < 5.0:
    print('Média {:.2f}'.format(media))
    print('REPROVADO! Nos vemos ano que vem...')
elif media <= 6.9:
    print('Média {:.2f}'.format(media))
    print('RECUPERAÇÃO! Estude mais!')
else:  # Considera que media >= 7.0
    print('Média {:.2f}'.format(media))
    print('APROVADO! Parabéns, continue assim.')
