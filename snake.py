from turtle import Turtle
# --------------------------------------#
STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]  #global variables or otherwise constants
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
# --------------------------------------#


class Snake:

    def __init__(self):  #inializor, what kind of attributes should the snake have?
        self.segments = []  #the three bodies to start
        self.create_snake()  #new segment which consists of color, square and starting position
        self.head = self.segments[0]  #just the very first square (the head) in our case

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')  # this defines the shape.
        new_segment.color('cadet blue')
        new_segment.shapesize(stretch_len=0.5, stretch_wid=0.5)
        new_segment.penup()  # this is so there is no line underneath out snake
        new_segment.goto(position)  # first one goes to (0, 0) second goes to (-20, 0) and so on.
        self.segments.append(new_segment)  # [snake head, middle, end]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  #Start: 2, End: 0, Step: -1
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # we are using this to move position 3 to 2
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:  #if the head is not facing down, then we can move UP.
            self.head.setheading(UP)     #snake cannot move backwards

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
