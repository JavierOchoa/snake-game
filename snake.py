from turtle import Turtle
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270

class Snake:
    
    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segmenet(position)

    def add_segmenet(self, position):
        new_turtle = Turtle('square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(position)
        self.all_segments.append(new_turtle)
    
    def extend(self):
        self.add_segmenet(self.all_segments[-1].position())
    
    def move(self):
        for segment in range(len(self.all_segments) -1, 0, -1):
            new_x = self.all_segments[segment - 1].xcor()
            new_y = self.all_segments[segment - 1].ycor()
            self.all_segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
