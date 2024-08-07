import random

# Dicionário para cores
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m'
}

# Lista de opções
opcao = ['PEDRA', 'PAPEL', 'TESOURA']

# Computador escolhe uma opção aleatoriamente
computador = random.choice(opcao)

# Solicita a escolha do jogador e exibe opções
jogador = int(input('{}Vamos jogar JOKENPÔ? Eu já escolhi minha opção.{} Agora é sua vez:\n{}1 - Pedra\n{}2 - Papel\n{}3 - Tesoura\n{}Qual sua Opção? '.format(
    cores['vermelho'], cores['limpa'], cores['verde'], cores['amarelo'], cores['azul'], cores['limpa']
)))

# Converte a escolha do jogador em texto correspondente
if jogador == 1:
    jogador = 'PEDRA'
elif jogador == 2:
    jogador = 'PAPEL'
elif jogador == 3:
    jogador = 'TESOURA'
else:
    print('Opção inválida, tente novamente.')
    exit()  # Encerra o programa se a opção for inválida

# Exibe as escolhas e resultado
print(f'Computador: {computador}')
print(f'Jogador: {jogador}')

# Verifica quem ganhou
if (computador == 'PEDRA' and jogador == 'TESOURA') or \
   (computador == 'PAPEL' and jogador == 'PEDRA') or \
   (computador == 'TESOURA' and jogador == 'PAPEL'):
    print('Ganhei!')
elif (jogador == 'PEDRA' and computador == 'TESOURA') or \
     (jogador == 'PAPEL' and computador == 'PEDRA') or \
     (jogador == 'TESOURA' and computador == 'PAPEL'):
    print('Você Ganhou, parabéns!')
elif jogador == computador:
    print('Empate! Vamos jogar novamente.')
else:
    print('ERRO')
