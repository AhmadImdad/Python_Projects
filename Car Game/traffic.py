from turtle import Turtle
import random

SHAPE = "square"
DISTANCE = 20


class Traffic:
    def __init__(self):
        self.cars_list = list()

    def create_cars(self):
        chance = random.randint(1, 6)
        if chance == 1 or chance == 2:
            car = Turtle()
            car.shape(SHAPE)
            car.color((random.randint(0, 255),
                       random.randint(0, 255),
                       random.randint(0, 255)))
            car.penup()
            car.goto(250, random.randint(-250, 250))
            car.shapesize(stretch_len=2, stretch_wid=1)
            self.cars_list.append(car)

    def move(self):
        for cars in self.cars_list:
            cars.setheading(180)
            cars.forward(DISTANCE)
