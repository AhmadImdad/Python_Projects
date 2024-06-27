from turtle import Turtle
SHAPE = "square"
COLOR = "white"


class Snake:
    def __init__(self):
        self.snakes = list()
        self.count = 0
        self.create_snakes()
        self.head = self.snakes[0]
        self.create_boundary()

    def create_snakes(self):
        x = 0
        for i in range(3):
            self.snakes.append(Turtle(SHAPE))
            self.count += 1
            self.snakes[i].color(COLOR)
            self.snakes[i].penup()
            self.snakes[i].goto(x, 0)
            x -= 20

    def move_up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)

    def move_down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)

    def move_right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)

    def move_left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)

    def movement(self):
        i = len(self.snakes) - 1
        while i >= 0:
            if i != 0:
                self.snakes[i].goto(self.snakes[i - 1].xcor(),
                                    self.snakes[i - 1].ycor())
            else:
                self.snakes[i].forward(20)
            i -= 1

    def extend(self):
        self.snakes.append(Turtle("square"))
        self.snakes[self.count].color("white")
        self.snakes[self.count].penup()
        self.movement()
        self.count += 1

    def create_boundary(self):
        boundary = Turtle()
        boundary.hideturtle()
        boundary.color(COLOR)
        boundary.penup()
        boundary.goto(290, 290)
        boundary.pendown()
        for _ in range(4):
            boundary.right(90)
            boundary.forward(580)

    def reset(self):
        for snake in self.snakes:
            snake.hideturtle()
        self.snakes.clear()
        self.count = 0
        self.create_snakes()
        self.head = self.snakes[0]

