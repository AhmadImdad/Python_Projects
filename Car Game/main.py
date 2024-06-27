import turtle
from car import Car
from traffic import Traffic
import time
from levels import Level

COLOR = "white"

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor(COLOR)
screen.title("Car Game")
screen.tracer(0)
screen.colormode(255)

traffic = Traffic()
car = Car()
level = Level()
screen.listen()
screen.onkey(fun=car.move_up, key="w")

check = False
temp_cars_list = list()
traffic.create_cars()
speed = 0.15
game_on = True

while game_on:
    
    traffic.create_cars()
    level.update()
    time.sleep(speed)
    screen.update()
    traffic.move()
    # condition that turtle does not go out of screen and
    # reached the end
    if car.ycor() > 280:
        level.level += 1
        speed *= 0.9
        car.goto(0, -280)
    # make a condition to check collision with the traffic
    for cars in traffic.cars_list:
        if cars.distance(car) < 15:
            game_on = False
            screen.clear()
            level.game_over()

screen.exitonclick()
