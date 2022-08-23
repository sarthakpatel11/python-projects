from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboard()

    def level_increase(self):
        self.level += 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def game_over(self):
        self.level = 1
