from turtle import Turtle
SHAPE = "circle"
COLOR = "white"


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.color(COLOR)
        self.increment_x = 10
        self.increment_y = 10
        self.flag = False

    def move(self):
        self.goto(self.xcor() + self.increment_x, self.ycor() + self.increment_y)

    def bounce_y(self):
        self.increment_y *= -1

    def bounce_x(self):
        if not self.flag:
            self.increment_x *= -1
            self.flag = True

    def bounce_again(self):
        self.bounce_x()
