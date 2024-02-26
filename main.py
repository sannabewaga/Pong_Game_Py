from turtle import Turtle, Screen
from ball import Ball
from Paddle import Paddle
import time

from scoreboard import ScoreBoard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)



pad1 = Paddle()
pad1.setposition(350, 0)
pad2= Paddle()
pad2.setposition(-350,0)


ball = Ball()
sb = ScoreBoard()




screen.listen()

screen.onkey(pad1.up, key="Up")
screen.onkey(pad1.down, key="Down")
screen.onkey(pad2.up, key="w")
screen.onkey(pad2.down, key="s")


game_is_on = True


while game_is_on:
    ball.move()
    time.sleep(0.05)


    if ball.xcor()>320 and ball.distance(pad1)<50:
        ball.xmove *= -1

    elif ball.xcor()<-320 and ball.distance(pad2)<50:
        ball.xmove *=-1


    if ball.xcor()>380:
        ball.setpos(0,0)
        ball.xmove*=-1
        sb.leftup()


    if ball.xcor()<-380:
        ball.setpos(0,0)
        ball.xmove *= -1
        sb.rightup()

    screen.update()

screen.exitonclick()
