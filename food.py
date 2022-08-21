from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.4, stretch_wid=0.4)
        self.color('rosy brown')
        self.speed(0)
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)  #Will always be in a random spot that isn't right on the wall

    def refresh(self):
        random_x = random.randint(-270, 270)  #Refresh to new food once food 1 is eaten.
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
