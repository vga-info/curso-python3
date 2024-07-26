# DESAFIO 020
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos 4 alunos
# e mostre a ordem sorteada.
import random
a1 = input('Nome do aluno 1: ')
a2 = input('Nome do aluno 2: ')
a3 = input('Nome do aluno 3: ')
a4 = input('Nome do aluno 4: ')
alunos = [a1,a2,a3,a4]
random.shuffle(alunos)
print('Alunos na ordem de apresentação: {}'.format(alunos))
