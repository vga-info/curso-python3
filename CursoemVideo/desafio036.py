# DESAFIO 036
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o 'valor da casa', o 'salário' do comprador e 'quantos anos' ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# Solicita o valor da casa
valordacasa = float(input('Qual o valor da casa? R$ '))

# Solicita o salário do comprador
salario = float(input('Qual o seu salário? R$ '))

# Solicita em quantos anos o empréstimo será pago
anos = int(input('Em quantos anos vai pagar? '))

# Converte anos para meses
meses = anos * 12

# Calcula o valor da prestação mensal
prestacao = valordacasa / meses

# Calcula o limite de 30% do salário
prestacao30 = salario * 0.30

# Verifica se a prestação mensal é menor ou igual a 30% do salário
if prestacao <= prestacao30:
    # Exibe mensagem de aprovação com detalhes
    print('Empréstimo Aprovado!\nPagamento em {} anos ({} meses/parcelas)\nValor da prestação (pago mensalmente): R${:.2f}'.format(anos, meses, prestacao))
else:
    # Exibe mensagem de negação
    print('Empréstimo Negado!')
