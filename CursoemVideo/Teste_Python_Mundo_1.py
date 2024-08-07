# Curso de Python 3 – Mundo 1 [40 Horas] finalizado em 06/08/2024
# Teste Python Mundo 1

# Das opções abaixo, apenas uma NÃO É uma característica da linguagem Python. Marque a opção inválida da lista a seguir:
# É nativamente compilada
# Python é uma linguagem interpretada, não compilada nativamente.

# O nome da linguagem Python foi escolhido pelo seu criador para homenagear o que?
# Um programa de TV chamado Monty Python
# Guido van Rossum escolheu o nome Python em homenagem ao grupo de comédia britânico Monty Python.

# Qual das opções a seguir permite ler a idade de uma pessoa em Python, já considerando o valor digitado como um número?
# idade = int('Quantos anos você tem?')
# Essa opção é incorreta, pois a função int() espera um argumento que pode ser convertido para um inteiro.
# idade = input(int('Quantos anos você tem?'))
# Essa opção é incorreta, pois a função input() espera uma string como argumento.
# idade = int(input('Quantos anos você tem?')) <<<<<
# Correta. Esta opção lê a entrada como string e depois converte para inteiro.
# idade = input('Quantos anos você tem?')
# Essa opção lê a entrada como string e não a converte para inteiro.

idade = int(input('Quantos anos você tem? '))
print('A idade digitada é: {}'.format(idade))
print(type(idade))
# Verifica e imprime o tipo da variável idade, que deve ser <class 'int'>.

# Considere a string s = 'prova de python'. A instrução len(s) retornaria qual valor?
# 15 <<<<<
# Correta. A função len(s) retorna o comprimento da string, que é 15 caracteres.
# 14
# 13
# 10

s = 'prova de python'
print('"{}" tem '.format(s), len(s), ' caracteres')
# Imprime o comprimento da string s, que é 15 caracteres.

# Qual dos comandos a seguir é capaz de escrever uma mensagem na tela usando Python?
# print() <<<<<
# Correta. A função print() é usada para exibir mensagens na tela.
# echo()
# Essa função não existe em Python.
# System.out.println()
# Esse comando é usado em Java, não em Python.
# Console.log()
# Esse comando é usado em JavaScript, não em Python.

# Se o nosso programa Python precisar calcular a raiz quadrada de um número, seria interessante incluir qual linha como primeiro comando desse programa?
# from numbers import pow
# Importa a função pow do módulo numbers, mas não é adequado para calcular a raiz quadrada diretamente.
# import sqrt
# A sintaxe está incorreta e não especifica o módulo.
# from math import sqrt <<<<<
# Correta. Importa a função sqrt do módulo math para calcular a raiz quadrada.
# from math import pow
# A função pow() pode ser usada para calcular potências, mas não é a melhor opção para raízes quadradas.

# Qual das opções a seguir completa as lacunas da afirmação abaixo?
# A Linguagem Python foi criada no ano de ___ , pelo programador ______________. Das opções abaixo, a única que preenche corretamente as lacunas é:
# 1993 / Rasmus Lerdorf
# Rasmus Lerdorf é o criador da linguagem PHP, não Python.
# 1992 / James Gosling
# James Gosling é o criador da linguagem Java, não Python.
# 1982 / Guido Van Hossum <<<<<
# Correta. A linguagem Python foi criada em 1991 por Guido van Rossum.
# 2000 / Anders Hejlsberg
# Anders Hejlsberg é o criador da linguagem C#, não Python.

# Considere a string x = 'curso de python no cursoemvideo'. Qual dos comandos abaixo retornaria a palavra 'curso'?
# x[4]
# Retorna apenas o caractere na posição 4, que é 'o'.
# x[:5] <<<<<
# Correta. Retorna os primeiros 5 caracteres, que formam a palavra 'curso'.
# x[1:5]
# Retorna os caracteres da posição 1 até 4, que formam a palavra 'urso'.
# x[5]
# Retorna apenas o caractere na posição 5, que é um espaço em branco.

x = 'curso de python no cursoemvideo'
print('mostrando apenas a palavra curso: {}'.format(x[:5]))
# Imprime a palavra 'curso', que corresponde aos primeiros 5 caracteres da string x.

# Qual é o resultado calculado pelo Python para as expressões simples 19 // 2 e 19 % 2, respectivamente?
# 9.5 e 1
# 9.5 seria o resultado de 19 / 2, não 19 // 2.
# 9 e 1 <<<<<
# Correta. 19 // 2 é 9 (divisão inteira) e 19 % 2 é 1 (resto da divisão).
# 1 e 0
# Isso estaria incorreto para as operações fornecidas.
# 0 e 1
# Isso estaria incorreto para as operações fornecidas.

a = 19 // 2
b = 19 % 2
print('19//2= {} || 19%2= {}'.format(a, b))
# Imprime os resultados das operações: 19 // 2 = 9 e 19 % 2 = 1.
