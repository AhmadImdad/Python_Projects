import random
from Starter import *
import turtle
from turtle import Turtle as t

screen = turtle.Screen()
screen.setup(width=550, height=400)
starter()

reached = False
flag = [False, False, False, False, False]

while not reached:
    tim.forward(random.randint(0, 10))
    chonk.forward(random.randint(0, 10))
    G.forward(random.randint(0, 10))
    pikachu.forward(random.randint(0, 10))
    bruno.forward(random.randint(0, 10))
    current_position1 = tim.pos()
    current_position2 = G.pos()
    current_position3 = pikachu.pos()
    current_position4 = bruno.pos()
    current_position5 = chonk.pos()

    if (current_position1[0] >= 230 or current_position2[0] >= 230 or
            current_position3[0] >= 230 or current_position4[0] >= 230 or
            current_position5[0] >= 230):

        if current_position1[0] >= 230:
            print(f"{tim.pencolor()} won the race!!!!")
            flag[0] = True
        if current_position2[0] >= 230:
            print(f"{G.pencolor()} won the race!!!!")
            flag[1] = True
        if current_position3[0] >= 230:
            print(f"{pikachu.pencolor()} won the race!!!!")
            flag[2] = True
        if current_position4[0] >= 230:
            print(f"{bruno.pencolor()} won the race!!!!")
            flag[3] = True
        if current_position5[0] >= 230:
            print(f"{chonk.pencolor()} won the race!!!!")
            flag[4] = True

        # Reset check to count flags
        check = sum(flag)
        if check > 1:
            print("Race was a draw!!!! Finding winner with maximum score!!!")
            total = []
            if flag[0]:
                total.append((tim.xcor(), 0))
            if flag[1]:
                total.append((G.xcor(), 1))
            if flag[2]:
                total.append((pikachu.xcor(), 2))
            if flag[3]:
                total.append((bruno.xcor(), 3))
            if flag[4]:
                total.append((chonk.xcor(), 4))

            # Find the turtle with the maximum distance
            max_total = 0
            index = -1
            for position, i in total:
                if position > max_total:
                    max_total = position
                    index = i

            if index == 0:
                print(f"{tim.pencolor()} won the race!!!!")
            elif index == 1:
                print(f"{G.pencolor()} won the race!!!!")
            elif index == 2:
                print(f"{pikachu.pencolor()} won the race!!!!")
            elif index == 3:
                print(f"{bruno.pencolor()} won the race!!!!")
            elif index == 4:
                print(f"{chonk.pencolor()} won the race!!!!")

        reached = True

screen.exitonclick()
