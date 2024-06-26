from turtle import Turtle

COLOR = "white"
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color(COLOR)

    def put_score(self):
        self.clear()
        self.goto(0, 288)
        self.write(arg=f"Score = {self.score}", align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
