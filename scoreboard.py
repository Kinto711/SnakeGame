from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_banner()

    def create_banner(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 25, 'normal'))

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 25, 'normal'))
        print("+1 to score")
        print(self.score)


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=('Arial', 60, 'normal'))