from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.last_direction = RIGHT  # Initialize the last direction as RIGHT
        self.direction_changed = False  # Initialize the direction change flag as False
 
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
           
    
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(MOVE_DISTANCE)
        self.direction_changed = False  # Reset the direction change flag
    
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        
    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def up(self):
        if not self.direction_changed and self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.last_direction = UP
            self.direction_changed = True

    def down(self):
        if not self.direction_changed and self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.last_direction = DOWN
            self.direction_changed = True
    
    def right(self):
        if not self.direction_changed and self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.last_direction = RIGHT
            self.direction_changed = True
    
    def left(self):
        if not self.direction_changed and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.last_direction = LEFT
            self.direction_changed = True
