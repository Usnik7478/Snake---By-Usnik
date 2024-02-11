import turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTACE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.creat_snake()
        self.head = self.snake_body[0]

    def creat_snake(self):
        for position in STARTING_POSITION:
            self.addbody(position)

    def addbody(self, position):
        snake = turtle.Turtle("circle")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.snake_body.append(snake)

    def extends(self):
        self.addbody(self.snake_body[-1].position())

    def reset(self):
        for a in self.snake_body:
            a.goto(x=1000, y=100)
        self.snake_body.clear()
        self.creat_snake()
        self.head = self.snake_body[0]


    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            x = self.snake_body[i - 1].xcor()
            y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(x, y)
        self.head.forward(MOVE_DISTACE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
