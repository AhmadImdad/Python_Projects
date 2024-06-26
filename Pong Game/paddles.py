import turtle
from turtle import Turtle
SIZE = 4
COLOR = "white"
SHAPE = "square"


class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape(SHAPE)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(COLOR)
        self.penup()
        self.goto(xcor, ycor)
        self.score = 0

    def move_up(self):
        new_y = self.ycor() + 30
        new_x = self.xcor()
        self.goto(new_x, new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        new_x = self.xcor()
        self.goto(new_x, new_y)
