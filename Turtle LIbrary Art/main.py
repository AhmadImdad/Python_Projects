import turtle
import random
from turtle import Turtle
timmy = Turtle()
screen = turtle.Screen()
timmy.pensize(15)
screen.colormode(255)
timmy.speed(0)


def to_start():
    timmy.penup()
    timmy.right(90)
    timmy.forward(250)
    timmy.right(90)
    timmy.forward(300)
    timmy.right(180)

def make_painting():
    i = 30
    horizontal_check = 0
    vertical_check = 0
    rotater = 0
    while True:
        timmy.color(random.randint(0, 255),
            random.randint(0, 255), random.randint(0,255))
        timmy.pendown()
        timmy.circle(1)
        timmy.penup()
        timmy.forward(i)
        horizontal_check += i
        if horizontal_check == 600:
            horizontal_check = 0
            if rotater == 0:
                timmy.left(90)
                timmy.pendown()
                timmy.color(random.randint(0, 255),
                random.randint(0, 255), random.randint(0, 255))
                timmy.circle(1)
                timmy.penup()
                timmy.forward(30)
                timmy.left(90)
                vertical_check += 30
                rotater = 1
            elif rotater == 1:
                timmy.right(90)
                timmy.pendown()
                timmy.color(random.randint(0, 255),
                            random.randint(0, 255), random.randint(0, 255))
                timmy.circle(1)
                timmy.penup()
                timmy.forward(30)
                timmy.right(90)
                vertical_check += 30
                rotater = 0
        if vertical_check > 500:
            break


to_start()
make_painting()
screen.exitonclick()

