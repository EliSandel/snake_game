from turtle import Turtle
FONT = ('Courier',24,'normal')


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.point = 0
        self.penup()
        self.hideturtle()
        self.color("green")
        self.goto(0,260)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.point} High Score: {self.highscore}", align="center", font=FONT)
    
    def add_point(self):
        self.point += 1
        self.update_scoreboard()
        
    def reset(self):
        if self.point > self.highscore:
            self.highscore = self.point
            with open("data.txt", mode="w") as data:
                data.write(f"{self.point}")
        self.point = 0
        self.update_scoreboard()
        

