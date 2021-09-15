from random import randrange
import turtle


class Comida():
    def novaComida(self):
        turtle.hideturtle()
        turtle.setpos(0, 0)
        turtle.shape("circle")
        turtle.penup()
        turtle.shapesize(stretch_len=0.5, stretch_wid=0.5)
        turtle.color("red")
        turtle.goto(randrange(-280, 280, 20), randrange(-280, 280, 20))
        turtle.showturtle()
        comidaPos = turtle.pos()

        return comidaPos
