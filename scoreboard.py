from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        # Before write set the position
        self.goto(-280, 250)
        # if we didn't give it will doest show score at first time won
        self.update_score_bord()

    def update_score_bord(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        # self.clear() use here or above
        self.level += 1
        self.update_score_bord()






