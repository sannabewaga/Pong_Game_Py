from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()

        self.shape("circle")
        self.color("yellow")
        self.speed("slowest")
        self.ymove=10
        self.xmove=10


    def move(self):


        new_x= self.xcor()+ self.xmove
        new_y = self.ycor()+self.ymove

        self.goto(new_x,new_y)

        if self.ycor()>280 or self.ycor()<-280:
            self.ymove=-self.ymove






