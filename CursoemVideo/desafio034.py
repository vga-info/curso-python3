# DESAFIO 034
# ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO.
# PARA SALÁRIOS SUPERIORES A R$ 1250,00 CALCULE UM AUMENTO DE 10%
# PARA SALÁRIOS INFERIORES OU IGUAIS A R$ 1250,00 É DE 15%

# Solicita ao usuário o salário do funcionário
salario = float(input('Qual o salário do funcionário: R$'))

# Verifica se o salário é menor ou igual a R$ 1250,00
if salario <= 1250.00:
    # Calcula o aumento de 15%
    aumento = salario * 0.15
    # Calcula o novo salário após o aumento
    novosalario = salario + aumento
    # Exibe o valor do aumento e o novo salário
    print('Aumento de R${:.2f} (15%)\nNovo Salário R${:.2f}'.format(aumento, novosalario))
else:
    # Calcula o aumento de 10%
    aumento = salario * 0.10
    # Calcula o novo salário após o aumento
    novosalario = salario + aumento
    # Exibe o valor do aumento e o novo salário
    print('Aumento de R${:.2f} (10%)\nNovo Salário R${:.2f}'.format(aumento, novosalario))
