# DESAFIO 059
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] SOMAR [2] MULTIPLICAR [3] MAIOR [4] NOVOS NÚMEROS [5] SAIR DO PROGRAMA
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
opcao = 0  # Inicializa a variável de opção para controlar o loop

while opcao != 5:  # Continua no loop até o usuário escolher a opção de sair
    print('\n\nNúmeros digitados: {} e {}, o que deseja realizar?'.format(n1, n2))
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Digitar novos números\n[5] Sair')
    opcao = int(input('Digite a opção: '))

    # Verifica se a opção escolhida é somar
    if opcao == 1:
        soma = n1 + n2  # Realiza a soma dos dois números
        print('A soma entre eles é {}'.format(soma))

    # Verifica se a opção escolhida é multiplicar
    elif opcao == 2:
        multi = n1 * n2  # Realiza a multiplicação dos dois números
        print('O produto entre eles é {}'.format(multi))

    # Verifica se a opção escolhida é encontrar o maior número
    elif opcao == 3:
        if n1 > n2:
            print('{} é o maior número entre {} e {}'.format(n1, n1, n2))
        elif n2 > n1:
            print('{} é o maior número entre {} e {}'.format(n2, n1, n2))
        else:
            print('Os números {} e {} são iguais!'.format(n1, n2))

    # Verifica se a opção escolhida é digitar novos números
    elif opcao == 4:
        n1 = float(input('Digite um novo número: '))  # Solicita o primeiro novo número
        n2 = float(input('Digite outro novo número: '))  # Solicita o segundo novo número

    # Verifica se a opção escolhida é sair
    elif opcao == 5:
        print('Finalizando o programa...')  # Mensagem de finalização

    else:
        print('Opção inválida! Tente novamente.')  # Mensagem de erro para opções inválidas

print('FIM')  # Indica o final do programa
