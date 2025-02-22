from turtle import Turtle

SPEED = 50
DOWN = 20
UP = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_len=1, stretch_wid=6)
        self.penup()
        self.goto(-350 if position == "left" else 350, 0)

    def move_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - UP)

    def move_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + UP)
