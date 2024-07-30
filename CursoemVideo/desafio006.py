# DESAFIO 006
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.

n = float(input('Digite um número: '))  # Solicita ao usuário que digite um número e converte para float

d = n * 2  # Calcula o dobro do número
t = n * 3  # Calcula o triplo do número
r = n ** (1/2)  # Calcula a raiz quadrada do número usando a operação de exponenciação

# Exibe o dobro, triplo e a raiz quadrada do número
print('Dobro: {} | Triplo: {} | Raiz Quadrada: {:.2f}'.format(d, t, r))
