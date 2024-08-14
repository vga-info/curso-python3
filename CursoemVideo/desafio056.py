# DESAFIO 056
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# 1- A média de idade do grupo.
# 2- O nome do homem mais velho.
# 3- Quantas mulheres têm menos de 20 anos.

# Inicialização das variáveis
somaidade = 0  # Para acumular a soma das idades
maioridade = 0  # Para armazenar a idade do homem mais velho
velho = ""  # Para armazenar o nome do homem mais velho
mulheres = 0  # Para contar quantas mulheres têm menos de 20 anos

# Loop para ler os dados das 4 pessoas
for c in range(1, 5):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = int(input('Digite o Sexo:\n1 para Masculino\n2 para Feminino\n'))

    # Acumulando a soma das idades
    somaidade += idade

    # Verifica se a pessoa é homem e se a idade é maior que a maioridade registrada
    if sexo == 1:
        if idade > maioridade:
            maioridade = idade
            velho = nome

    # Verifica se a pessoa é mulher e se a idade é menor que 20
    if sexo == 2:
        if idade < 20:
            mulheres += 1

# Calcula a média de idade do grupo
mediaidade = somaidade / 4

# Mostra os resultados
print('A média de idade do grupo é {:.2f}'.format(mediaidade))
print('Nome do homem mais velho é {}'.format(velho))
print('Quantidade de mulheres abaixo dos 20 anos é {}'.format(mulheres))
