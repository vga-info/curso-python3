#Curso de Python 3 – Mundo 1 [40 Horas] finalizado em 06/08/2024
#Teste Python Mundo 1

#Das opções abaixo, apenas uma NÃO É uma característica da linguagem Python. Marque a opção inválida da lista a seguir:
# É nativamente compilada

#O nome da linguagem Python foi escolhido pelo seu criador para homenagear o que?
# Um programa de TV chamado Monty Python

#Qual das opções a seguir permite ler a idade de uma pessoa em Python, já considerando o valor digitado como um número?
# idade = int('Quantos anos você tem?')
# idade = input(int('Quantos anos você tem?'))
# idade = int(input('Quantos anos você tem?')) <<<<<
# idade = input('Quantos anos você tem?')

idade = int(input('Quantos anos você tem? '))
print('A idade digitada é: {}'.format(idade))
print(type(idade))

#Considere a string s = 'prova de python'. A instrução len(s) retornaria qual valor?
# 15 <<<<<
# 14
# 13
# 10

s = 'prova de python'
print('"{}" tem '.format(s),len(s),' caracteres')

#Qual dos comandos a seguir é capaz de escrever uma mensagem na tela usando Python?

# print() <<<<<
# echo()
# System.out.println()
# Console.log()

#Se o nosso programa Python precisar calcular a raiz quadrada de um número, seria interessante incluir qual linha como primeiro comando desse programa?

# from numbers import pow
# import sqrt
# from math import sqrt <<<<<
# from math import pow

#Qual das opções a seguir completa as lacunas da afirmação abaixo?

#A Linguagem Python foi criada no ano de ___ , pelo programador ______________. Das opções abaixo, a única que preenche corretamente as lacunas é:

# 1993 / Rasmus Lerdorf
# 1992 / James Gosling
# 1982 / Guido Van Hossum <<<<<
# 2000 / Anders Hejlsberg

#Considere a string x = 'curso de python no cursoemvideo'. Qual dos comandos abaixo retornaria a palavra 'curso'?

# x[4]
# x[:5] <<<<<
# x[1:5]
# x[5]

x = 'curso de python no cursoemvideo'
print('mostrando apenas a palavra curso: {}'.format(x[:5]))

#Qual é o resultado calculado pelo Python para as expressões simples 19 // 2 e 19%2, respectivamente?

# 9.5 e 1
# 9 e 1 <<<<<
# 1 e 0
# 0 e 1

a = 19//2
b = 19%2
print('19//2= {} || 19%2= {}'.format(a,b))
