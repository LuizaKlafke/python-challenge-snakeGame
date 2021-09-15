from turtle import Turtle

start_pos = [(0, 0), (-20, 0), (-40, 0)]

class cobra:
    def __init__(self):
        self.cobra=[]
        self.creat_cobra()

    def creat_cobra(self):
        for num in start_pos:
            new_tur = Turtle("square")
            new_tur.color("green")
            new_tur.penup()
            new_tur.goto(num)
            self.cobra.append(new_tur)

    def move(self):
        for num in range(len(self.snake) - 1, 0, -1):
            new_x = self.cobra[num - 1].xcor()
            new_y = self.cobra[num - 1].ycor()
            self.snake[num].goto(new-x, new_y)
        self.snake[0].forward(20)

    def inc_cobra(self):
        new_tur = Turtle("square")
        new_tur.color("green")
        new_tur.goto(self.cobra[-1].position())
        self.cobra.append(new_tur)
        
            
                          
        
