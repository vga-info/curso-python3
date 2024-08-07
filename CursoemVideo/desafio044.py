# DESAFIO 044
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu 'preço normal' e 'condição de
# pagamento':
# - À VISTA DINHEIRO/CHEQUE 10% DESC
# - À VISTA NO CARTÃO 5% DESC
# - EM ATÉ 2X NO CARTÃO PREÇO NORMAL
# - 3X OU MAIS NO CARTÃO PREÇO NORMAL + 20% DE JUROS

# Solicita ao usuário o preço normal do produto
preconormal = float(input('Digite o preço do produto: R$'))

# Solicita ao usuário o código da forma de pagamento
formpag = int(input('Digite o código da forma de pagamento:\n1 - Dinheiro ou Cheque\n2 - Cartão\nDigite a Opção: '))

print('\n')  # Adiciona uma linha em branco para melhor formatação na saída

# Verifica a forma de pagamento escolhida
if formpag == 1:
    # Se a forma de pagamento for Dinheiro ou Cheque, aplica 10% de desconto
    preco = preconormal - (preconormal * 0.10)
    print('Forma de pagamento: Dinheiro ou Cheque\nValor Total a Pagar: R${:.2f}'.format(preco))
elif formpag == 2:
    # Se a forma de pagamento for Cartão, solicita a quantidade de parcelas
    parcela = int(input('Digite a quantidade de parcelas: '))
    if parcela == 1:
        # Se for 1 parcela no cartão, aplica 5% de desconto
        preco = preconormal - (preconormal * 0.05)
        print('Forma de pagamento: 1x no Cartão sem juros\nValor Total a Pagar: R${:.2f}'.format(preco))
    elif parcela == 2:
        # Se for 2 parcelas no cartão, preço normal, calcula o valor da parcela
        valorparcela = preconormal / 2
        print('Forma de pagamento: 2x no Cartão sem juros\nValor Total a Pagar: R${:.2f}\nValor da Parcela: R${:.2f}'.format(preconormal, valorparcela))
    elif parcela >= 3:
        # Se for 3 ou mais parcelas no cartão, aplica 20% de juros
        preco = preconormal + (preconormal * 0.20)
        valorparcela = preco / parcela
        print('Forma de pagamento: {}x no Cartão com Juros\nValor Total a Pagar: R${:.2f}\nValor da Parcela: R${:.2f}'.format(parcela, preco, valorparcela))
else:
    # Caso a opção de pagamento seja inválida
    print('Opção de pagamento inválida! Tente novamente.')
