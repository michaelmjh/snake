from turtle import Turtle

ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("yellow")
        self.setpos(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT)

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"Game over", False, align=ALIGNMENT)
