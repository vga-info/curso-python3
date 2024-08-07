### Aula 12 – Condições Aninhadas

# Solicita o nome do usuário
nome = str(input('Qual é o seu nome? '))

# Verifica se o nome é 'Vitor'
if nome == 'Vitor':  # Verifica a primeira condição
    print('Que nome bonito!')
# Verifica se o nome é um dos nomes populares
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':  # Verifica a segunda condição
    print('Seu nome é bem popular no Brasil!')
# Verifica se o nome está em uma lista de nomes femininos
elif nome in 'Ana Cláudia Jéssica Juliana':  # Verifica a terceira condição
    print('Belo nome Feminino!')
# Caso nenhuma das condições anteriores seja verdadeira
else:  # O 'else' é opcional e sempre é o último da estrutura
    print('Seu nome é bem normal.')

# Exibe uma mensagem final com o nome do usuário
print('Tenha um bom dia, {}!'.format(nome))
