import turtle
import time
from snake import Snake
from food import Food
from score import Score

def runGame():
    pass

screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Snake 🐍 - By Usnik")
border = turtle.Turtle()
border.speed(0)
border.penup()
border.hideturtle()
border.goto(x=-290, y=290)
border.pencolor('blue')
border.pendown()
border.setheading(0)
border.forward(580)
border.right(90)
border.forward(580)
border.right(90)
border.forward(580)
border.right(90)
border.forward(580)
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


def runGame():
    score.clear()
    score.reset()
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        score.showscore()

        if snake.head.distance(food) < 15:
            food.refresh()
            score.update()
            snake.extends()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            score.reset()
            snake.reset()
            game_is_on = False

        for i in snake.snake_body[1:]:
            if snake.head.distance(i) < 10:
                score.reset()
                snake.reset()
                game_is_on = False


runGame()

screen.onkey(runGame, 'r')

score.print_fscore()

screen.exitonclick()
