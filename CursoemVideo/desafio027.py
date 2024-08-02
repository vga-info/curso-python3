# DESAFIO 027
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
# e último nome separadamente. Ex. Ana Maria de Souza | primeiro: Ana | último: Souza

# Lê o nome completo da pessoa
nome = str(input('Digite o nome completo da pessoa: ')).strip()

# Divide o nome completo em partes, separando por espaços
dividido = nome.split()

# Print da lista resultante da divisão (opcional, útil para depuração)
print(dividido)

# Mostra o primeiro e o último nome da lista
# Usando índices: o primeiro elemento é [0] e o último é [-1]
print('Nome Completo: {}\nPrimeiro nome: {}\nÚltimo nome: {}'.format(nome, dividido[0], dividido[-1]))
