# DESAFIO 019
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome
# do escolhido. Utilize o módulo random para realizar o sorteio.

import random  # Importa o módulo random para utilizar a função de escolha aleatória

# Solicita ao usuário o nome dos quatro alunos e armazena em variáveis
a1 = input('Nome do aluno 1: ')
a2 = input('Nome do aluno 2: ')
a3 = input('Nome do aluno 3: ')
a4 = input('Nome do aluno 4: ')

# Cria uma lista com os nomes dos alunos
alunos = [a1, a2, a3, a4]

# Escolhe aleatoriamente um dos nomes da lista usando a função choice do módulo random
sorte = random.choice(alunos)

# Exibe o nome do aluno sorteado
print('O aluno sorteado é: {}'.format(sorte))

# Nota:
# - A função `random.choice()` seleciona aleatoriamente um elemento de uma lista.
# - O programa lê os nomes dos quatro alunos e os armazena em uma lista.
# - Em seguida, escolhe um aluno aleatoriamente e exibe o nome do aluno sorteado.
