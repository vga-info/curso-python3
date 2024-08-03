# DESAFIO 035
# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUÁRIO SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO

# Solicita ao usuário o comprimento das três retas
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

# Verifica se as retas podem formar um triângulo usando a desigualdade triangular
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')
