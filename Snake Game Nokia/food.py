import random
from turtle import Turtle
SHAPE = "turtle"
SPEED = "fastest"
COLOR = "red"


class Food:
    def __init__(self):
        self.food = Turtle()

    def spread_food(self):
        self.food.penup()
        self.food.goto(float(random.randint(-270, 270)),
                       float(random.randint(-270, 270)))
        self.food.shape(SHAPE)
        self.food.speed(SPEED)
        self.food.color(COLOR)
        self.food.shapesize(stretch_len=0.5, stretch_wid=0.5)
