# DESAFIO 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário
# com 15% de aumento.

s = float(input('Digite o salário atual: '))  # Solicita ao usuário o salário atual e converte para float
a = float(input('Digite o reajuste em %: '))  # Solicita ao usuário a porcentagem de reajuste e converte para float

sr = s + (s * a / 100)  # Calcula o novo salário com o reajuste, adicionando o valor do aumento ao salário atual

# Exibe o salário atual, a porcentagem de reajuste e o novo salário com o reajuste aplicado
print('Salário de R${:.2f} com reajuste de {:.2f}% é: R${:.2f}'.format(s, a, sr))

# Nota:
# - O valor do reajuste é calculado multiplicando o salário atual pela porcentagem de reajuste e dividindo por 100.
# - O novo salário é obtido adicionando o valor do reajuste ao salário atual.
# - {:.2f} na formatação da string é utilizado para exibir valores com duas casas decimais.
