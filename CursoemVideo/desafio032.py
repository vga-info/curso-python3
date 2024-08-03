# DESAFIO 032
# FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO
# EXTRA: "Digite 0 para considerar o ano atual (função adicionada na correção do exercicio)

from datetime import date
# Solicita ao usuário que insira um ano
ano = int(input('Qual ano quer analizar? (Coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year

# Verifica se o ano é bissexto
if ano % 4 == 0 and ano % 100 != 0 or (ano % 400 == 0):
    # Se o ano é bissexto, exibe uma mensagem informando que o ano é bissexto
    print('O ano {} é bissexto!'.format(ano))
else:
    # Se o ano não é bissexto, exibe uma mensagem informando que o ano não é bissexto
    print('O ano {} não é bissexto.'.format(ano))
