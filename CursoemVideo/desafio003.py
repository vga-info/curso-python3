n1: int = int(input('Digite um número: '))  # Solicita ao usuário que digite um número e converte para inteiro, armazenando em 'n1'
n2 = int(input('Digite outro número: '))  # Solicita ao usuário que digite outro número, converte para inteiro e armazena em 'n2'

soma = n1 + n2  # Calcula a soma dos dois números e armazena o resultado na variável 'soma'

# Exibe o resultado da soma usando a sintaxe antiga de formatação de strings
print('A soma entre', n1, 'e', n2, 'vale', soma)

# Exibe o resultado da soma usando a sintaxe nova de formatação de strings com o método format()
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
