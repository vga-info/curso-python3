# Curso Python #11 - Cores no Terminal

# A sequência \033 é usada para iniciar o código de cores no terminal
# \033[style;text;backgroundm
# style > 0 (none), 1 (bold), 4 (underline), 7 (negative)
# text > 30 (branco), 31 (vermelho), 32 (verde), 33 (amarelo), 34 (azul), 35 (magenta), 36 (ciano), 37 (cinza)
# background > 40 até 47, as mesmas cores acima

# Exemplo de uso: texto em vermelho, fundo azul, estilo negrito
print('\033[1;31;44mOlá Mundo!\033[m')

# Definindo duas variáveis
a = 3
b = 5

# Exibindo os valores de a e b com cores diferentes
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))

# Definindo uma variável de string
nome = 'Guanabara'

# Exibindo uma mensagem com o nome sublinhado e azul
print('Olá! Muito prazer em te reconhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

# Criando um dicionário de cores
cores = {
    'limpa': '\033[m',           # Reseta a cor para o padrão
    'azul': '\033[34m',          # Texto azul
    'amarelo': '\033[33m',       # Texto amarelo
    'pretoebranco': '\033[7;30m' # Texto preto em fundo branco (inversão de cores)
}

# Exibindo uma mensagem com o nome em amarelo usando o dicionário de cores
print('Olá Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))

x = 'curso de python no cursoemvideo'
print(x[:5])
