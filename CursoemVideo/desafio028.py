# Exercício Python #028 - Jogo da Adivinhação v.1.0
# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR PENSAR EM UM NUMERO INTEIRO ENTRE 0 E 5 E PEÇA PARA O USUARIO TENTAR DESCOBRIR QUAL FOI O NUMERO ESCOLHIDO PELO COMPUTADOR.
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUARIO VENCEU OU PERDEU.

import random  # Importa o módulo random para gerar números aleatórios

# Cria uma lista de números inteiros de 0 a 5
numeros = [0, 1, 2, 3, 4, 5]

# Seleciona aleatoriamente um número da lista de números
sorteado = random.choice(numeros)
# outra opção abaixo
sorteado2 = random.randint(0,5) # usando outro modulo de 0 até 5, nao precisando declarar uma variavel com os num

# Pede ao usuário para tentar adivinhar o número sorteado
teste = int(input('Estou pensando em um número entre 0 e 5, qual é o número? '))

# Compara a resposta do usuário com o número sorteado
if teste == sorteado:
    # Se o usuário acertou, exibe uma mensagem de sucesso
    print('Certa resposta!')
else:
    # Se o usuário errou, exibe uma mensagem de erro e revela o número sorteado
    print('Errou feio, errou rude! Pensei no número {}!'.format(sorteado))
