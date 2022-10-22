from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as data:
            self.record = int(data.read())
        self.create_banner()

    def create_banner(self):

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-80, 270)
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 25, 'normal'))
        self.goto(80, 270)
        self.write(f"score: {self.record}", False, align="center", font=('Arial', 25, 'normal'))

    def update(self):
        self.clear()
        self.score += 1
        self.goto(-80, 270)
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 25, 'normal'))

        if self.score > self.record:
            self.record = self.score
            with open("score.txt", 'w') as f:
                f.write(str(self.record))
        self.goto(80, 270)
        self.write(f"score: {self.record}", False, align="center", font=('Arial', 25, 'normal'))
        # print(f"{self.score} + score")
        # print(f"{self.record.read()} Record")



    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=('Arial', 60, 'normal'))

