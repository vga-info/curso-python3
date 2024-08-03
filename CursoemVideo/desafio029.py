# DESAFIO 029
# ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
# SE ELE ULTRAPASSAR 80KM/H MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
# A MULTA VAI CUSTAR R$ 7,00 PARA CADA KM ACIMA DO LIMITE

# Solicita ao usuário a velocidade do carro
speed = int(input('Qual a velocidade do carro em KM/h? '))

# Verifica se a velocidade excede 80 KM/h
if speed > 80:
    # Calcula a multa: R$ 7,00 para cada KM acima do limite
    multa = (speed - 80) * 7
    # Exibe uma mensagem informando que o carro foi multado e o valor da multa
    print(f'Multa! Valor a pagar: R${multa:.2f}')
