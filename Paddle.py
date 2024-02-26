from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.color("yellow")
        self.shape("square")
        self.shapesize(5, 1, 1)


    def up(self):
        new_y = self.ycor()+30
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)