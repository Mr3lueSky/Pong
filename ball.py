from turtle import Turtle

class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.sleep_time = 0.06
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    def bounce_y(self):
        self.y_move *= -1
        self.sleep_time *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.sleep_time *= 0.9

    def reset(self):
        self.goto(0,0)
        self.bounce_x()
        self.bounce_y()
        self.sleep_time=0.06




