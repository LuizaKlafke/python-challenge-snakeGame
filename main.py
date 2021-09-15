from ambiente import *
from comida import *
from cobra import *
from funcoes import *
from time import sleep
import math
import os
import os.path

scores = []
score = 0
highScores = [0, ]
filePath = 'scores.csv'

if os.path.exists(filePath):
    Funcoes().manipulaCsv('r', filePath, highScores)

else:
    Funcoes().manipulaCsv('w', filePath, highScores)

highScore = max(highScores)

Ambiente().score(score, highScore)
comidaPos = Comida().novaComida()

while True:
    cobraPos = t.pos()
    sleep(0.5)
    t.forward(20)

    diferencaPosX = Funcoes().calculaDiferenca('x', cobraPos, comidaPos)
    diferencaPosY = Funcoes().calculaDiferenca('y', cobraPos, comidaPos)

    cobraPosX = math.floor(abs(cobraPos[0]))
    cobraPosY = math.floor(abs(cobraPos[1]))

    if -10 < diferencaPosX < 10 and -10 < diferencaPosY < 10:
        comidaPos = Comida().novaComida()
        score += 20
        scores.append(score)

        if highScore < score:
            highScore = score

        Ambiente().incScore(score, highScore)

    elif cobraPosX > 230 or cobraPosY > 230:
        Ambiente().gameOver()

        for score in scores:
            highScores.append(score)

        highScores = Funcoes().removeRepetido(highScores)

        Funcoes().manipulaCsv('w', filePath, highScores)

        sleep(5)
        break
