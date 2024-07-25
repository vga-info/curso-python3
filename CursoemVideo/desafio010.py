# DESAFIO 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos dólares ela pode comprar, considera US$1,00=R$3,27
real = float(input('Quanto dinheiro você tem? R$'))
cotacao = 3.27
dolar = real / cotacao
print('R${:.2f} convertido na cotação de R${:.2f} o Dólar vale USD$ {:.2f}'.format(real,cotacao,dolar))
