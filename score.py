from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("hs.txt", mode="r") as self.sc:
            self.highscore = int(self.sc.read())
        self.showscore()

    def showscore(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=300)
        self.write(arg=f"Score: {self.score} Highscore: {self.highscore}", move=False, align='center',
                   font=('Arial', 24, 'normal'))

    def reset(self):
        self.score = 0
        self.clear()

    def update(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
            with open("hs.txt", mode="w") as sc:
                sc.write(str(self.highscore))
        self.clear()
        self.showscore()

    def print_fscore(self):
        self.clear()
        self.color("white")
        self.goto(x=0, y=0)
        self.write(arg=f"   GAME OVER\nYour final Score: {self.score}", move=False, align='center',
                   font=('Arial', 20, 'normal'))
        self.goto(x=0, y= -45)
        self.write(arg=f" Press R to restart the game", move=False, align='center',
                   font=('Arial', 16, 'normal'))
