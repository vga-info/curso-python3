# DESAFIO 019
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome
# do escolhido.
import random
a1 = input('Nome do aluno 1: ')
a2 = input('Nome do aluno 2: ')
a3 = input('Nome do aluno 3: ')
a4 = input('Nome do aluno 4: ')
alunos = [a1,a2,a3,a4]
sorte = random.choice(alunos)
print('O aluno sorteador é: {}'.format(sorte))
