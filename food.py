from turtle import Turtle
import random

MOVE_DISTANCE = 20

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        
        # Adjust x and y coordinates to align with the snake's grid
        x -= x % MOVE_DISTANCE
        y -= y % MOVE_DISTANCE
        
        self.goto(x,y)
