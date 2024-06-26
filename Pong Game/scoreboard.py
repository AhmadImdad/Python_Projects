from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = Turtle()
        self.score.penup()
        self.score.hideturtle()
        self.score.color("white")

    def update_score_l(self, score):
        self.score.clear()
        self.score.goto(-100, 200)
        self.score.write(arg=f"{score}", align="center", font=("Courier", 60, "normal"))

    def update_score_r(self, score):
        self.score.clear()
        self.score.goto(100, 200)
        self.score.write(arg=f"{score}",
                         align="center", font=("Courier", 60, "normal"))

    def game_over(self, user, line):
        line.clearer()
        self.score.home()
        self.score.write(arg=f"Game Over\n{user} Wins",
                         align="center", font=("Courier", 40, "normal"))
