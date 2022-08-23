from math import trunc
from turtle import Turtle

STARTIMG_POINT = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTIMG_POINT)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self):
        self.goto(STARTIMG_POINT)

    def level_completed(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False
