from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.SCORE = 0
        self.color('white')
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.updateScore()
        
    def updateScore(self):
        self.write(f"Scoreboard = {self.SCORE}", align="center", font=('Arial', 24, 'normal'))
        
    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=('Arial', 24, 'normal'))
        
    def points(self):
        self.SCORE += 1
        self.clear()
        self.updateScore()
        
        