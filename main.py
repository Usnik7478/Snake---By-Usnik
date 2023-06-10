import turtle
import time
from snake import Snake
from food import Food
from score import Score

screen = turtle.Screen()  # //--> Setting the screen
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Snake 🐍 - By Usnik")
border = turtle.Turtle()
border.speed(0)
border.penup()
border.hideturtle()
border.goto(x=-290, y=290)
border.pencolor('white')
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

game_is_on = True

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.update()
        snake.extends()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        score.reset()
        score.showscore()

    for i in snake.snake_body[1:]:
        if snake.head.distance(i) < 10:
            snake.reset()
            score.reset()
            score.showscore()

score.print_fscore()

screen.exitonclick()
