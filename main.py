from ambiente import *
from comida import *
from cobra import *
from funcoes import *
from time import sleep
import os
import os.path

cobra = []
scores = []
score = 0
highScores = [0, ]
filePath = 'scores.csv'


if os.path.exists(filePath):
    Funcoes().manipulaCsv('r', filePath, highScores)

else:
    Funcoes().manipulaCsv('w', filePath, highScores)

highScore = max(highScores)
Ambiente()
Ambiente().score(score, highScore)
cobra.append(Cobra().criaCabeca())
Comida().novaComida()

comidaPos = comida.pos()

while True:
    cobraPos = cabeca.pos()
    sleep(0.1)
    Cobra().moveCauda(cobra)
    cabeca.forward(20)

    for i in cobra:
        if 0 < i.distance(cabeca) < 10:
            Ambiente().gameOver(scores, highScores, filePath)

            break

    cobraPosX = abs(cabeca.xcor())
    cobraPosY = abs(cabeca.ycor())

    if cabeca.distance(comida) < 10:
        comidaPos = comida.pos()
        Comida().mudarPos()
        score += 20
        scores.append(score)
        Cobra().criaCauda(cobra)

        if highScore < score:
            highScore = score

        Ambiente().incScore(score, highScore)

    elif cobraPosX > 230 or cobraPosY > 230:
        Ambiente().gameOver(scores, highScores, filePath)

        break
