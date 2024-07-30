# DESAFIO 007
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

n1 = float(input('1ª Nota: '))  # Solicita ao usuário que digite a primeira nota e converte para float
n2 = float(input('2ª Nota: '))  # Solicita ao usuário que digite a segunda nota e converte para float

m = (n1 + n2) / 2  # Calcula a média das duas notas

# Exibe a média das notas, formatada com duas casas decimais
print('A Média das notas é {:.2f}'.format(m))
