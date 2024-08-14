# DESAFIO 046
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de
# artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time  # Importa o módulo time, que permite pausar a execução do programa

print('Iniciando contagem regressiva...⏳')  # Exibe uma mensagem indicando o início da contagem regressiva

# Laço de repetição para contagem regressiva de 10 até 1
for c in range(10, 0, -1):  # O range começa em 10, vai até 1 (exclusivo) e decrementa de 1 em 1
    print(c)  # Exibe o número atual da contagem
    time.sleep(1)  # Pausa a execução por 1 segundo

print('🎆Feliz Ano Novo🎆')  # Exibe a mensagem final após a contagem regressiva
