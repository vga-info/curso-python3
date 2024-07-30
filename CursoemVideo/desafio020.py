# DESAFIO 020
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# dos trabalhos dos alunos. Faça um programa que leia o nome dos 4 alunos
# e mostre a ordem sorteada. Utilize o módulo random para realizar o sorteio.

import random  # Importa o módulo random para utilizar a função de embaralhamento

# Solicita ao usuário o nome dos quatro alunos e armazena em variáveis
a1 = input('Nome do aluno 1: ')
a2 = input('Nome do aluno 2: ')
a3 = input('Nome do aluno 3: ')
a4 = input('Nome do aluno 4: ')

# Cria uma lista com os nomes dos alunos
alunos = [a1, a2, a3, a4]

# Embaralha a ordem dos nomes na lista usando a função shuffle do módulo random
random.shuffle(alunos)

# Exibe a lista dos alunos na nova ordem de apresentação
print('Alunos na ordem de apresentação: {}'.format(alunos))

# Nota:
# - A função `random.shuffle()` embaralha os elementos da lista em ordem aleatória.
# - O programa lê os nomes dos quatro alunos, os armazena em uma lista e depois embaralha a lista.
# - Finalmente, exibe a lista com a nova ordem dos alunos para apresentação dos trabalhos.
