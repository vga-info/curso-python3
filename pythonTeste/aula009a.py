frase = 'Curso em Vídeo Python'
# Índices dos caracteres na string 'Curso em Vídeo Python':
# C[0] u[1] r[2] s[3] o[4]  [5] e[6] m[7]  [8] V[9] í[10] d[11] e[12] o[13]  [14] P[15] y[16] t[17] h[18] o[19] n[20]

print(frase)  # Exibe a frase armazenada na variável 'frase'
print(frase[3])  # Exibe o 4º caractere da string (índice 3): 's'
print(frase[3:13])  # Exibe os caracteres do índice 3 ao 12 (13-1): 'so em Víde'
print(frase[:13])  # Exibe os caracteres do início até o índice 12: 'Curso em Víde'
print(frase[13:])  # Exibe os caracteres do índice 13 até o final: 'o Python'
print(frase[1:15:2])  # Exibe os caracteres do índice 1 ao 14, pulando de 2 em 2: 'uroe íeP'
print(frase[::2])  # Exibe todos os caracteres da string, pulando de 2 em 2: 'Cro mVdoPto'
print(frase.count('o'))  # Conta quantas vezes o caractere 'o' (minúsculo) aparece: 3
print(frase.count('O'))  # Conta quantas vezes o caractere 'O' (maiúsculo) aparece: 0
print(frase.upper().count('O'))  # Converte a string para maiúsculas e conta os 'O': 3
print(len(frase))  # Exibe o número total de caracteres na string, incluindo espaços: 21
print(len(frase.strip()))  # Exibe o número de caracteres excluindo espaços no início e no fim: 20
# ' Curso em Vídeo Python ' -> 'Curso em Vídeo Python' (21 caracteres)
print(frase.replace('Python', 'Android'))  # Substitui 'Python' por 'Android': 'Curso em Vídeo Android'
print(frase, '(antes do replace)')  # Exibe a frase original antes do replace
frase = frase.replace('Python', 'Android')  # Atualiza a variável 'frase' com a substituição
print(frase, '(depois do replace)')  # Exibe a frase após o replace
print('Curso' in frase)  # Verifica se 'Curso' está presente na frase: True
print(frase.find('Curso'))  # Retorna o índice da primeira ocorrência de 'Curso': 0
print(frase.lower().find('vídeo'))  # Converte a string para minúsculas e encontra 'vídeo': 9
print(frase.split())  # Divide a string em uma lista de palavras: ['Curso', 'em', 'Vídeo', 'Android']
dividido = frase.split()  # Armazena a lista de palavras na variável 'dividido'
print(dividido[0])  # Exibe o primeiro item da lista 'dividido': 'Curso'
print(dividido[2][3])  # Exibe o 4º caractere do terceiro item da lista: 'e' (índice 3 de 'Vídeo')
print(
    """UM TEXTO MUITO LONGO
PULANDO LINHAS
QUANTAS QUISER"""
)  # Utiliza três aspas para exibir um texto de várias linhas
