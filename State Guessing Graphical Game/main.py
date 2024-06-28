import turtle

import pandas
import pandas as pd
from turtle import Turtle

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.setup(800, 600)
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pd.read_csv("50_states.csv")
states = data["state"].tolist()

for i in range(len(states)):
    states[i] = states[i].lower()

x_cord = data["x"].tolist()
y_cord = data["y"].tolist()

game_on = True
guessed = 0
answered_states = list()

while game_on:
    index = 0
    state_name = turtle.textinput(f"{guessed}/50 Guessed",
                                  "Write the state's name : ")
    state_name = state_name.lower()
    for names in states:
        if state_name == names and names not in answered_states:
            state_turtle = Turtle()
            state_turtle.penup()
            state_turtle.hideturtle()
            # A turtle writes text wherever it is standing at the moment
            state_turtle.goto(x_cord[index], y_cord[index])
            state_turtle.write(arg=state_name, align="center",
                               font=("Times New Roman", 10, "normal"))
            guessed += 1
            answered_states.append(state_name)
            break
        elif state_name in answered_states:
            break
        index += 1

    if index == len(states):
        game_on = False
        temp_list = [name for name in states if name not in answered_states]
        data_dict = {
            "states": temp_list
        }
        temp_DF = pandas.DataFrame(data_dict)
        temp_DF.to_csv("States_to_learn.csv")

screen.exitonclick()
