from turtle import Turtle

COLOR = "white"
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.read_from_file()
        self.hideturtle()
        self.penup()
        self.color(COLOR)

    def put_score(self):
        self.clear()
        self.goto(0, 288)
        self.write(arg=f"Score = {self.score} Highscore: {self.highscore}",
                   align=ALIGNMENT,
                   font=FONT)

    def update_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("scores.txt", mode='w') as file:
                file.write(str(self.highscore))
        self.score = 0
        self.put_score()

    def increase_score(self):
        self.score += 1
        self.put_score()

    def read_from_file(self):
        with open("scores.txt") as file:
            temp = file.read()
            temp = int(temp)
            return temp
