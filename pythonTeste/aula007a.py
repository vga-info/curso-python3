n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('Soma {}'.format(n1+n2))
print('Subtração {}'.format(n1-n2))
print('Multiplicação {}'.format(n1*n2))
print('Divisão {:.3f}'.format(n1/n2)) #:.3f indica 3 casas decimais
print('Potência {}'.format(n1**n2))
print('Divisão Inteira {}'.format(n1//n2))
print('Resto da Divisão Inteira {}'.format(n1%n2))
#Tambem podemos fazer usando variaveis e um print direto como abaixo
soma = n1 + n2
subt = n1 - n2
mult = n1 * n2
div = n1 / n2
pot = n1 ** n2
divint = n1 // n2
resdiv = n1 % n2
print('A soma é {}, a subtração é {}, a multiplicação é {}, a divisão é {:.3f},\n a potência é {}, a divisão inteira é {} e o resto da divisão inteira é {}'
      .format(soma,subt,mult,div,pot,divint,resdiv))
# \n pula linha