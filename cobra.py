#
# Programa que define os atributos do objeto cobra do jogo.
#

from turtle import Turtle


class Cobra():

    def cima(self):

        return cabeca.setheading(90)

    def baixo(self):

        return cabeca.setheading(270)

    def esquerda(self):

        return cabeca.setheading(180)

    def direita(self):

        return cabeca.setheading(0)

    def criaCabeca(self):
        cabeca.setpos(0, 0)
        cabeca.speed(0)
        cabeca.shape("square")
        cabeca.color("green")
        cabeca.penup()
        cabeca.showturtle()

        return cabeca

    def criaCauda(self, segmentos):
        cauda = Turtle("square")
        cauda.hideturtle()
        cauda.speed(0)
        cauda.penup()
        cauda.color("green")
        segmentos.append(cauda)
        cauda.goto(cabeca.pos())
        cauda.showturtle()

    # Define movimento da cauda da cobra de acordo com posição das tartarugas.
    def moveCauda(self, segmentos):
        for i in range(len(segmentos)-1, 0, -1):

            posX = segmentos[i-1].xcor()
            posY = segmentos[i-1].ycor()
            segmentos[i].goto(posX, posY)

        if len(segmentos) > 0:
            x = cabeca.xcor()
            y = cabeca.ycor()
            segmentos[0].goto(x, y)


#
# Registra o movimento à partir das teclas.
#

cabeca = Turtle()
cabeca.hideturtle()

s = cabeca.getscreen()

s.onkey(Cobra().cima,     "Up")
s.onkey(Cobra().baixo,    "Down")
s.onkey(Cobra().esquerda, "Left")
s.onkey(Cobra().direita,  "Right")

s.listen()
