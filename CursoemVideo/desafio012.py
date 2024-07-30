# DESAFIO 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto

p = float(input("Preço do produto: "))  # Solicita ao usuário o preço do produto e converte para float
d = 5  # Define a porcentagem de desconto como 5%

# Calcula o valor do desconto e o novo preço do produto
v = p - (p * d / 100)  # Subtrai o valor do desconto do preço original para obter o novo preço

# Exibe o novo preço do produto após aplicar o desconto
print('Valor do produto com {:.2f}% de desconto: R${:.2f}'.format(d, v))

# Nota:
# - O desconto é calculado multiplicando o preço do produto pela porcentagem de desconto e dividindo por 100.
# - O novo preço é obtido subtraindo o valor do desconto do preço original.
# - {:.2f} na formatação da string é utilizado para exibir valores com duas casas decimais.
