# DESAFIO 022
# Crie um programa que leia o nome completo de uma pessoa e mostre
# 1 - O nome com todas as letras maiúsculas
# 2 - O nome com todas as letras minúsculas
# 3 - Quantas letras ao todo (sem considerar espaços)
# 4 - Quantas letras tem o primeiro nome

# Lê o nome completo do usuário
nome = str(input('Digite um nome completo: ')).strip() #.strip remove todos os  espaços no inicio e fim da string

# 1 - O nome com todas as letras maiúsculas
maiusculas = nome.upper()  # Converte todas as letras para maiúsculas

# 2 - O nome com todas as letras minúsculas
minusculas = nome.lower()  # Converte todas as letras para minúsculas

# 3 - Quantas letras ao todo (sem considerar espaços)
semespaços = nome.replace(' ', '')  # Remove todos os espaços do nome
qtdletras = len(semespaços)  # Conta o número total de letras (sem espaços)

# 4 - Quantas letras tem o primeiro nome
separado = nome.split()  # Divide o nome em partes usando o espaço como separador
qtdletraspri = len(separado[0])  # Conta o número de letras no primeiro nome
# outra opção é usando find
qtdletraspri2 =nome.find(' ')

# Exibe o nome original e os resultados das operações
print('O nome é: {}'.format(nome))
print('Maiúsculas: {}'.format(maiusculas))
print('Minúsculas: {}'.format(minusculas))
print('Qtd Caracteres (Sem espaços): {}'.format(qtdletras))
print('Qtd Letras primeiro nome: {}'.format(qtdletraspri))
print('Qtd Letras primeiro nome: {}'.format(qtdletraspri2))
