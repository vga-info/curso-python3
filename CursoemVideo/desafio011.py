# DESAFIO 011
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule sua área e a quantidade de tinta necessária para printa-la,
# sabendo que cada litro de tinta pinta uma área de 2m²
l = float(input('Digite a Largura da Parede em metros: '))
a = float(input('Digite a Altura da Parede em metros: '))
area = l * a
lt = area / 2
print('Area a ser pintada: {}m²'.format(area))
print('Qtd Litros de Tinta necessários: {}'.format(lt))
