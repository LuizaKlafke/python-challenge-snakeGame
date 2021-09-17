#
# Programa simples que orienta movimento da cobra segundo as teclas de setas
#
from turtle import Turtle


class Cobra(Turtle):

    # Aponta para cima

    def cima(self):

        return cabeca.setheading(90)

    # Aponta para baixo

    def baixo(self):

        return cabeca.setheading(270)

    # Aponta para a esquerda

    def esquerda(self):

        return cabeca.setheading(180)

    # Aponta para a direita

    def direita(self):

        return cabeca.setheading(0)

    # Muda design da cabeça da cobra

    def criaCabeca(self):
        cabeca.setpos(0, 0)
        cabeca.speed(0)
        cabeca.shape("square")
        cabeca.color("green")
        cabeca.penup()
        cabeca.showturtle()

        return cabeca

    def criaCauda(self, cobra):
        cauda = Turtle("square")
        cauda.hideturtle()
        cauda.speed(0)
        cauda.penup()
        cauda.color("green")
        cauda.setpos(cobra[-1].position())
        cobra.append(cauda)
        cauda.showturtle()

    def moveCauda(self, cobra):
        for i in range(len(cobra) - 1, 0, -1):
            posX = cobra[i - 1].xcor()
            posY = cobra[i - 1].ycor()
            cobra[i].goto(posX, posY)


#
# Registra as teclas e inicia movimento
#
cabeca = Cobra()
cabeca.hideturtle()

s = cabeca.getscreen()

s.onkey(cabeca.cima,     "Up")
s.onkey(cabeca.baixo,    "Down")
s.onkey(cabeca.esquerda, "Left")
s.onkey(cabeca.direita,  "Right")

s.listen()
cabeca.criaCabeca()
