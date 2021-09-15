import turtle


class Ambiente():
    def background(self):
        b = turtle.Screen()
        b.title("Snake Game")
        b.bgcolor("blue")
        b.setup(width=600, height=600)

    def score(self, score, highScore):
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.speed(0)
        pen.shape("circle")
        pen.color("black")
        pen.penup()
        pen.goto(0, 225)
        pen.write(f"Score: {score} High Score: {highScore}", align="center",
                  font=("Arial", 24, "normal"))


Ambiente().background()
Ambiente().score(0, 0)
