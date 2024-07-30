# DESAFIO 021
# Faça um programa que abra e reproduza o áudio de um arquivo MP3.
# Utilize o módulo pygame para manipulação e reprodução de áudio.

import pygame  # Importa o módulo pygame

# Inicializa o mixer do pygame para reprodução de áudio
pygame.mixer.init()

# Carrega o arquivo de áudio MP3
pygame.mixer.music.load('sample.mp3')  # Certifique-se de que o arquivo 'sample.mp3' está na mesma pasta que este script

# Reproduz o áudio
pygame.mixer.music.play()

# Aguarda a reprodução terminar
while pygame.mixer.music.get_busy():  # Enquanto o áudio estiver sendo reproduzido
    pygame.time.Clock().tick(10)  # Espera para evitar uso excessivo da CPU

# Nota:
# - `pygame.mixer.init()` inicializa o módulo de áudio do pygame.
# - `pygame.mixer.music.load('sample.mp3')` carrega o arquivo de áudio MP3.
# - `pygame.mixer.music.play()` inicia a reprodução do áudio.
# - O loop `while pygame.mixer.music.get_busy()` é usado para manter o programa ativo enquanto o áudio está sendo reproduzido.
# - `pygame.time.Clock().tick(10)` é usado para adicionar uma pequena pausa no loop, evitando que o programa consuma muita CPU.
