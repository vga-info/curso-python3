# DESAFIO 015
# Escreva um programa que pergunte a quantidade de KM percorrido por um carro
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia
# e R$0,15 por KM rodado.

d = int(input('Quantos dias alugado? '))  # Solicita ao usuário o número de dias que o carro foi alugado e converte para inteiro
km = float(input('Quantos KM Rodados? '))  # Solicita ao usuário o número de quilômetros rodados e converte para float

# Calcula o preço total a pagar:
# Preço por dias = dias alugado * R$60,00
# Preço por KM = quilômetros rodados * R$0,15
p = (d * 60) + (km * 0.15)  # Soma o custo do aluguel dos dias e o custo por quilômetro rodado

# Exibe o total a pagar, formatado com duas casas decimais
print('Total a pagar: R${:.2f}'.format(p))

# Nota:
# - O custo do aluguel é calculado multiplicando o número de dias pelo valor diário.
# - O custo dos quilômetros rodados é calculado multiplicando a quantidade de KM pelo valor por KM.
# - {:.2f} na formatação da string é utilizado para exibir o valor total com duas casas decimais.
