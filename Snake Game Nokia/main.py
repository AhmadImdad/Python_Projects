import turtle
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.tracer(0)
screen.setup(width=630, height=630)
screen.title("The Snake Game")
screen.bgcolor("black")
screen.listen()

snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(snake.move_up, key='Up')
screen.onkey(snake.move_right, key='Right')
screen.onkey(snake.move_down, key='Down')
screen.onkey(snake.move_left, key='Left')

food.spread_food()


def escape():
    turtle.bye()


screen.onkey(escape, key='Escape')
game_on = True

while game_on:

    screen.update()
    time.sleep(0.1)
    score.put_score()
    snake.movement()
    if snake.head.distance(food.food) < 15:
        food.spread_food()
        score.increase_score()
        snake.extend()

    if (snake.head.xcor() > 285 or snake.head.xcor() < -285
            or snake.head.ycor() > 285 or snake.head.ycor() < -285):
        score.update_scoreboard()
        snake.reset()

    for segments in snake.snakes[1:]:
        if snake.head.distance(segments) < 5:
            score.increase_score()

screen.exitonclick()
