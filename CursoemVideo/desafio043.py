# DESAFIO 043
# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# tabela abaixo:
# - abaixo de 18.5: abaixo do peso
# - entre 18.5 e 25: peso ideal
# - 25 até 30: sobrepeso
# - 30 até 40: obesidade
# - acima de 40: obesidade mórbida

# Solicita ao usuário o peso e a altura
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

# Calcula o IMC (Índice de Massa Corporal)
imc = peso / (altura * altura)

# Determina a categoria do IMC e exibe o resultado
if imc < 18.5:
    print('IMC: {:.2f}'.format(imc))
    print('Está Abaixo do Peso')
elif imc < 25:
    print('IMC: {:.2f}'.format(imc))
    print('Está com o Peso Ideal')
elif imc < 30:
    print('IMC: {:.2f}'.format(imc))
    print('Está com Sobrepeso')
elif imc < 40:
    print('IMC: {:.2f}'.format(imc))
    print('Está Obeso')
else:  # Se imc >= 40
    print('IMC: {:.2f}'.format(imc))
    print('Obesidade Mórbida!')
