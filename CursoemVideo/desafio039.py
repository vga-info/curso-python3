# DESAFIO 039
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - se ele 'ainda vai se alistar' no serviço militar
# - se é a 'hora de se alistar'
# - se já 'passou do tempo' do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

# Solicita o ano de nascimento ao usuário
ano = int(input('Digite seu ano de nascimento: '))

# Calcula a idade com base no ano atual
idade = datetime.date.today().year - ano

# Verifica a situação do alistamento com base na idade
if idade < 18:
    # Se a idade for menor que 18, calcula quantos anos faltam para o alistamento
    falta = 18 - idade
    print('Faltam {} anos para se alistar!'.format(falta))
elif idade == 18:
    # Se a idade for exatamente 18, é o momento de se alistar
    print('Está na hora de se alistar!')
elif idade > 18:
    # Se a idade for maior que 18, calcula quantos anos já passaram do prazo de alistamento
    falta = idade - 18
    print('Já passou da hora! Você está {} anos atrasado para o alistamento.'.format(falta))
