from turtle import Turtle
from random import randint, choice

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.fo = ['circle', 'square', 'triangle']
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.x = randint(-280, 280)
        self.y = randint(-280, 280)
        self.foo = choice(self.fo)
        self.shape(self.foo)
        self.goto(self.x, self.y)
