from turtle import Turtle
SHAPE = "turtle"
COLOR = "black"
DISTANCE = 20


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move_up(self):
        self.forward(DISTANCE)
