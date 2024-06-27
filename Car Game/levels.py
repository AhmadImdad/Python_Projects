from turtle import Turtle
COLOR = "black"


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.color(COLOR)
        self.hideturtle()
        self.write(arg=f"Level: {self.level}",
                   align="left", font=("Courier", 20, "normal"))
        self.goto(-270, 270)

    def update(self):
        self.clear()
        self.write(arg=f"Level: {self.level}",
                   align="left", font=("Courier", 20, "normal"))
        self.goto(-270, 270)

    def game_over(self):
        self.home()
        self.write(arg=f"Game Over\nScore = {self.level}",
                   align="Center", font=("Courier", 20, "normal"))
