from turtle import Turtle


class MakeLine:
    def __init__(self):
        self.line = Turtle()
        self.line.penup()
        self.line.hideturtle()
        self.make_line()

    def make_line(self):
        self.line.penup()
        self.line.hideturtle()
        self.line.color("white")
        self.line.pensize(5)
        self.line.goto(0, 280)
        self.line.setheading(270)
        rotater = 0
        gap = 30
        for _ in range(0, 560, 30):
            if rotater == 0:
                self.line.pendown()
                self.line.forward(gap)
                rotater = 1
            else:
                self.line.penup()
                self.line.forward(gap)
                rotater = 0

    def clearer(self):
        self.line.clear()
