#
# Programa que define os atributos do objeto ambiente do jogo.
#

from time import sleep
import turtle


class Ambiente():

    # Cria background do jogo.
    def __init__(self):
        b = turtle.Screen()
        b.title("Snake Game")
        b.bgcolor("blue")
        b.setup(width=600, height=640)
        l = turtle.Turtle()
        l.hideturtle()
        l.penup()
        l.goto(-260, 260)
        l.pendown()
        l.speed(25)
        l.color("white")
        l.pensize(10)
        l.forward(520)
        l.right(90)
        l.forward(520)
        l.right(90)
        l.forward(520)
        l.right(90)
        l.forward(520)

    def score(self, score, highScore):
        pen.speed(0)
        pen.shape("circle")
        pen.color("white")
        pen.penup()
        pen.goto(0, 270)
        Ambiente().updateScore(score, highScore)

    def updateScore(self, score, highScore):
        pen.write(f"Score: {score} | High Score: {highScore}", align="center",
                  font=("Arial", 20, "normal"))

    def incScore(self, score, highScore):
        pen.clear()
        Ambiente().updateScore(score, highScore)

    def gameOver(self, cabeca, segmentos, comida):
        pen.goto(0, 0)
        pen.write("Game over", align="center", font=("Arial", 30, "normal"))

        cabeca.hideturtle()
        comida.hideturtle()
        for i in segmentos:
            i.hideturtle()

        sleep(3)


pen = turtle.Turtle()
pen.hideturtle()
