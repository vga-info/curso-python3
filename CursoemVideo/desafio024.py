# DESAFIO 024
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"

# Lê o nome da cidade do usuário
cidade = str(input('Digite o nome de uma cidade: ')).strip()

# Converte o nome da cidade para minúsculas para garantir que a comparação seja feita de forma case-insensitive
minuscula = cidade.lower()

# Verifica se o nome da cidade começa com a palavra "santo"
result = minuscula.startswith('santo')

# Exibe o resultado de forma informativa
if result:
    print('A cidade começa com "Santo".')
else:
    print('A cidade não começa com "Santo".')
