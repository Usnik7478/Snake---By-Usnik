from turtle import Turtle 


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.showscore()

    def showscore(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0,y=250)
        self.write( arg= f"Score: {self.score}",move = False,align='center',font=('Arial', 24, 'normal'))
        
    def update(self):
        self.score +=1
        self.clear()
        self.showscore()
    
    def print_fscore(self):
        self.clear()
        self.color("white")
        self.goto(x=0,y=0)
        self.write( arg= f"   GAME OVER\nYour final Score: {self.score}",move = False,align='center',font=('Arial', 20, 'normal'))