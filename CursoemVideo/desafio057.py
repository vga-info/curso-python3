# DESAFIO 057
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = 'N'  # Inicializa a variável com um valor que não seja M nem F
while sexo != 'M' and sexo != 'F':  # Continua pedindo até receber M ou F
    sexo = str(input('Digite o Sexo [M/F]: ')).upper()  # Recebe o input e converte para maiúsculo
    if sexo != 'M' and sexo != 'F':  # Verifica se o valor é inválido
        print('Erro, digite apenas M ou F!')

# Define a variável 'sx' de acordo com o valor digitado, especificando o sexo
if sexo == 'F':
    sx = 'Feminino'  # Atribui 'Feminino' se o valor digitado for 'F'
if sexo == 'M':
    sx = 'Masculino'  # Atribui 'Masculino' se o valor digitado for 'M'

# Informa ao usuário o sexo digitado de forma clara
print('O Sexo digitado é {}'.format(sx))
