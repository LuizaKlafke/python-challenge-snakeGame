#
# Programa simples que orienta movimento da cobra segundo as teclas de setas
#
from turtle import Turtle


class Cobra(Turtle):

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
        t.setpos(0, 0)
        t.speed(0)
        t.shape("square")
        t.color("green")
        t.penup()
        t.showturtle()


#
# Registra as teclas e inicia movimento
#
t = Cobra()
t.hideturtle()

s = t.getscreen()

s.onkey(t.cima,     "Up")
s.onkey(t.baixo,    "Down")
s.onkey(t.esquerda, "Left")
s.onkey(t.direita,  "Right")

s.listen()

t.cabeca()
