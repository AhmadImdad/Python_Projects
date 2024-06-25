import turtle
from turtle import Turtle as t
tim = t("turtle")
chonk = t("turtle")
bruno = t("turtle")
G = t("turtle")
pikachu = t("turtle")


def race_line ():
    tim.penup()
    tim.goto(246,190)
    tim.right(90)
    tim.pendown()
    tim.forward(380)
    tim.penup()
    tim.home()


def starter():
    race_line()
    tim.color("red")
    bruno.color("purple")
    chonk.color("green")
    G.color("orange")
    pikachu.color("yellow")
    tim.penup()
    chonk.penup()
    G.penup()
    pikachu.penup()
    bruno.penup()
    tim.goto(-230, -100)
    chonk.goto(-230, -50)
    G.goto(-230, 0)
    pikachu.goto(-230, 50)
    bruno.goto(-230, 100)