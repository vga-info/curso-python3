# desafio 062
# Melohore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input('Digite o primeiro termo da PA: '))  # Solicita o primeiro termo da PA
razao = int(input('Digite a razão da PA: '))  # Solicita a razão da PA

numtermos = 0  # Inicializa o contador de termos
continuar = 1
while numtermos != 10:  # Continua o loop até gerar 10 termos
    termo_atual = primeiro_termo + numtermos * razao  # Calcula o termo atual da PA
    print(termo_atual, end=' ')  # Exibe o termo atual seguido por um espaço
    numtermos += 1  # Incrementa o contador de termos

while continuar != 0:
    continuar = int(input('\n\nDeseja continuar mostrando?\nDigite a Qtd de termos adicionais\n ou 0 (zero) para parar: '))
    continua_pa = continuar + numtermos
    while numtermos != continua_pa:  # Continua o loop até gerar 10 termos
            termo_atual = primeiro_termo + numtermos * razao  # Calcula o termo atual da PA
            print(termo_atual, end=' ')  # Exibe o termo atual seguido por um espaço
            numtermos += 1  # Incrementa o contador de termos
    continuar -= 1
print('Saindo do programa...\n')
print('Fim.')  # Adiciona uma linha ao final da saída
