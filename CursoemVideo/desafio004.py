n = input('Escreva algo: ')  # Solicita ao usuário que escreva algo e armazena o valor na variável 'n'

# Exibe informações sobre a entrada do usuário
print('Informações sobre: {}'.format(n))

# Exibe o tipo primitivo do valor digitado
print('O tipo primitivo desse valor é', type(n))

# Verifica se a entrada é numérica (contém apenas dígitos)
print('Numérico?', n.isnumeric())

# Verifica se a entrada é alfabética (contém apenas letras)
print('Alfabético?', n.isalpha())

# Verifica se a entrada é alfanumérica (contém apenas letras e/ou números)
print('Alfa Numérico?', n.isalnum())

# Verifica se a entrada é um decimal (contém apenas dígitos decimais)
print('Decimal?', n.isdecimal())

# Verifica se a entrada está toda em letras minúsculas
print('Tudo Minúsculo?', n.islower())

# Verifica se a entrada está toda em letras maiúsculas
print('Tudo Maiúsculo?', n.isupper())

# Verifica se a entrada contém apenas espaços
print('Só tem espaços?', n.isspace())

# Verifica se a entrada está capitalizada (primeira letra em maiúscula e o restante em minúsculas)
print('Está Capitalizada?', n.istitle())
