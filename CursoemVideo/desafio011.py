# DESAFIO 011
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m²

l = float(input('Digite a Largura da Parede em metros: '))  # Solicita ao usuário a largura da parede e converte para float
a = float(input('Digite a Altura da Parede em metros: '))  # Solicita ao usuário a altura da parede e converte para float

area = l * a  # Calcula a área da parede em metros quadrados (m²)
lt = area / 2  # Calcula a quantidade de litros de tinta necessária, sabendo que cada litro cobre 2m²

# Exibe a área da parede a ser pintada e a quantidade de tinta necessária
print('Área a ser pintada: {}m²'.format(area))
print('Qtd Litros de Tinta necessários: {}'.format(lt))

# Nota:
# - A fórmula para a área da parede é largura * altura.
# - Para calcular a quantidade de tinta necessária, dividimos a área total por 2, pois cada litro cobre 2m².
# - O resultado indica quantos litros de tinta são necessários para cobrir a parede.
