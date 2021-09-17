#
# Programa que simula o jogo da cobrinha.
# Todos os direitos reservados à Luiza Klafke e Kesya Lopes.
#

from ambiente import *
from comida import *
from cobra import *
from funcoes import *
from time import sleep
import os
import os.path

colisao = False
segmentos = []
scores = []
score = 0
highScores = [0, ]
filePath = 'scores.csv'

# Verifica existência de base de dados CSV.

if os.path.exists(filePath):
    manipulaCsv('r', filePath, highScores)

else:
    manipulaCsv('w', filePath, highScores)

highScore = max(highScores)

Ambiente()
Ambiente().score(score, highScore)

Cobra().criaCabeca()

Comida().novaComida()

# Loop principal do jogo.

while True:
    sleep(0.1)
    Cobra().moveCauda(segmentos)
    cabeca.forward(20)

    # Verifica colisão da cabeça com cauda da cobra.
    for i in segmentos:
        if i.distance(cabeca) < 10:

            colisao = True

    # Verifica encontro da cabeça da cobra com a comida.
    if cabeca.distance(comida) < 10:
        Comida().mudarPos()
        score += 20
        scores.append(score)
        Cobra().criaCauda(segmentos)

        if highScore < score:
            highScore = score

        Ambiente().incScore(score, highScore)

    cobraPosX = abs(cabeca.xcor())
    cobraPosY = abs(cabeca.ycor())

    # Verifica colisão da cabeça da cobra com limites definidos no jogo.
    # Caso verdade, encerra loop principal
    if cobraPosX > 230 or cobraPosY > 230:
        finalizarJogo(scores, highScores, filePath)
        Ambiente().gameOver(cabeca, segmentos, comida)

        break

    # Em caso de colisão com cauda da cobra, encerra loop principal.
    elif colisao == True:
        finalizarJogo(scores, highScores, filePath)
        Ambiente().gameOver(cabeca, segmentos, comida)

        break
