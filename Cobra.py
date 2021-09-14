#
# Programa simples que orienta movimento da cobra segundo as teclas de setas
#

from turtle import *
from time import sleep


class Cobra(Turtle):

    # Move para frente

    def movimento(self):

        while True:
            t.forward(5)
            sleep(0.5)

    # Aponta para cima

    def cima(self):

        return t.setheading(90)

    # Aponta para baixo

    def baixo(self):

        return t.setheading(270)

    # Aponta para a esquerda

    def esquerda(self):

        return t.setheading(180)

    # Aponta para a direita

    def direita(self):

        return t.setheading(0)

    # Muda design da cabeça da cobra

    def cabeca(self):
        t.speed(0)
        t.shape("square")
        t.color("black")
        t.penup()


#
# Registra as teclas e inicia movimento
#

t = Cobra()
s = t.getscreen()

s.onkey(t.cima,     "Up")
s.onkey(t.baixo,    "Down")
s.onkey(t.esquerda, "Left")
s.onkey(t.direita,  "Right")

s.listen()
t.cabeca()
t.movimento()
