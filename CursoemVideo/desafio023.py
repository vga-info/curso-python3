# DESAFIO 023
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# Exemplo: Digite um número: 1834
# Saída: Unidade 4, Dezena 3, Centena 8, Milhar 1

# Lê um número como uma string
numero = input('Digite um número entre 0 e 9999: ')

# Garante que o número tenha exatamente 4 dígitos, preenchendo com zeros à esquerda se necessário
numero = numero.zfill(4)  # Adiciona zeros à esquerda para garantir que o número tenha 4 dígitos

# Divide o número em seus dígitos individuais
milhar = numero[0]  # Milhar: o primeiro dígito
centena = numero[1]  # Centena: o segundo dígito
dezena = numero[2]  # Dezena: o terceiro dígito
unidade = numero[3]  # Unidade: o quarto dígito

# Exibe os resultados formatados
print('Unidade: {}, Dezena {}, Centena {}, Milhar {}'.format(unidade,dezena,centena,milhar))
