import turtle
from turtle import Turtle
import time
from paddles import Paddle
from ball import Ball
from scoreboard import Score
from make_line import MakeLine

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
score_l = Score()
score_r = Score()
line = MakeLine()

screen.listen()
screen.onkey(fun=l_paddle.move_up, key='w')
screen.onkey(fun=l_paddle.move_down, key='s')
screen.onkey(fun=r_paddle.move_up, key='Up')
screen.onkey(fun=r_paddle.move_down, key='Down')

speed = 0.1
game_on = True
while game_on:

    score_l.update_score_l(l_paddle.score)
    score_r.update_score_r(r_paddle.score)
    time.sleep(speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        ball.flag = False
    if (r_paddle.distance(ball) <= 50 and ball.xcor() < 340 or
            l_paddle.distance(ball) <= 50 and ball.xcor() > -340):
        ball.bounce_x()
        speed *= 0.9
    if r_paddle.distance(ball) > 50 and ball.xcor() > 380:
        l_paddle.score += 1
        speed = 0.1
        ball.home()
        ball.bounce_again()
    if l_paddle.distance(ball) > 50 and ball.xcor() < -380:
        r_paddle.score += 1
        speed = 0.1
        ball.home()
        ball.bounce_again()
    if l_paddle.score == 5 or r_paddle.score == 5:
        if l_paddle.score == 5:
            score_l.game_over("Left", line)
            game_on = False
        elif r_paddle.score == 5:
            game_on = False
            score_r.game_over("Right", line)


screen.exitonclick()
