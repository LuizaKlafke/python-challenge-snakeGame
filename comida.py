from random import randrange
import turtle


class Comida():
    def novaComida(self):
        comida.setpos(0, 0)
        comida.shape("circle")
        comida.penup()
        comida.shapesize(stretch_len=0.5, stretch_wid=0.5)
        comida.color("red")
        comida.goto(randrange(-220, 220, 20), randrange(-220, 220, 20))
        comida.showturtle()

    def mudarPos(self):
        comida.hideturtle()
        comida.goto(randrange(-220, 220, 20), randrange(-220, 220, 20))
        comida.showturtle()


comida = turtle.Turtle()
comida.hideturtle()
