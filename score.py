import turtle
score = 0
high_score = 0

def score():
    pen = turtle.Turtle()   
    pen.speed(0)
    pen.shape("circle")
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,225)
    pen.write("Score: 0 High Score: 0", align="center", font=("Arial", 24, "normal"))
    
score()
