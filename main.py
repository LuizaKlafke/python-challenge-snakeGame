from ambiente import *
from comida import *
from cobra import *
from time import sleep
import math

score = 0
scores = []
highScore = 0

comidaPos = Comida().novaComida()
print(comidaPos)

while True:
    cobraPos = t.pos()
    sleep(0.5)
    t.forward(20.0)
    valorX = math.floor(cobraPos[0]) - math.floor(comidaPos[0])
    valorY = math.floor(cobraPos[1]) - math.floor(comidaPos[1])
    valores = valorX + valorY

    if -9 < valores < 9:
        comidaPos = Comida().novaComida()
        score += 20
        scores.append(score)
        highScore = max(scores)
        Ambiente().score(score, highScore)
