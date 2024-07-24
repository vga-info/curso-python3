# DESAFIO 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário
# com 15% de aumento.
s = float(input('Digite o salário atual: '))
a = float(input('Digite o reajuste em %: ')) #variavel de ajuste salario em %
sr = s+(s/100*a) # sr é SalárioReajustado
print('Salário de R${:.2f} com reajuste de {:.2f}% é: R${:.2f}'.format(s,a,sr))
