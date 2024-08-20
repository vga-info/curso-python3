# DESAFIO 058
# Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

import random

# O computador sorteia um número entre 0 e 10
sorteado = random.randint(0, 10)
contador_de_erros = 1  # Inicializa o contador de tentativas

print('Pensei em um número, tente adivinhar...')
# Usuário faz a primeira tentativa
teste = int(input('Digite um número de 0 a 10: '))

# Laço que continua enquanto o usuário não acerta o número
while teste != sorteado:
    contador_de_erros += 1  # Incrementa o contador de tentativas
    teste = int(input('Errou feio, errou rude! Tente outra vez: '))  # Pede uma nova tentativa

# Se o jogador acertou na primeira tentativa
if contador_de_erros == 1:
    print('Incrível! Acertou de primeira!')
else:
    # Exibe a quantidade de tentativas necessárias para acertar
    print('Certa resposta! Precisou de {} tentativas para acertar'.format(contador_de_erros))
