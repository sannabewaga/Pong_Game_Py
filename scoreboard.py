from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.color("yellow")
        self.goto(-100, 200)

        self.write(self.lscore, align="center", font=("Courier", 80, "normal"))

        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Courier", 80, "normal"))

    def leftup(self):
        self.lscore+=1
        self.updatescore()
    def rightup(self):
        self.rscore+=1
        self.updatescore()
