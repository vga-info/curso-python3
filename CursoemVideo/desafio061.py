# DESAFIO 061
# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input('Digite o primeiro termo da PA: '))  # Solicita o primeiro termo da PA
razao = int(input('Digite a razão da PA: '))  # Solicita a razão da PA

numtermos = 0  # Inicializa o contador de termos

while numtermos != 10:  # Continua o loop até gerar 10 termos
    termo_atual = primeiro_termo + numtermos * razao  # Calcula o termo atual da PA
    print(termo_atual, end=' ')  # Exibe o termo atual seguido por um espaço
    numtermos += 1  # Incrementa o contador de termos

print()  # Adiciona uma linha ao final da saída
