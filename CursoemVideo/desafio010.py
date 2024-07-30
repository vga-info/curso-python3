# DESAFIO 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos dólares ela pode comprar, considerando a cotação de US$1,00 = R$3,27

real = float(input('Quanto dinheiro você tem? R$'))  # Solicita ao usuário que informe o valor em reais e converte para float
cotacao = 3.27  # Define a cotação do dólar em reais (R$3,27 por USD$1,00)
dolar = real / cotacao  # Calcula a quantidade de dólares que pode ser comprada com o valor em reais

# Exibe o valor em reais, a cotação do dólar e o valor convertido em dólares
print('R${:.2f} convertido na cotação de R${:.2f} o Dólar vale USD$ {:.2f}'.format(real, cotacao, dolar))

# Nota:
# - {:.2f} na formatação da string é utilizado para exibir valores com duas casas decimais.
# - A cotação do dólar é usada para converter o valor em reais para dólares.
# - O resultado é o valor em dólares que pode ser comprado com a quantia informada em reais.
