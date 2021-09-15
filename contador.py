from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("black")
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.Score}", aligh = "center", font=("Arial", 20, "normal"))

    def inc_score(self):
        self.score +=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", aligh="center", font=("Arial", 30, "normal"))

