from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)

right_boarder = (300, 0)
left_boarder = (0, -300)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.update()
        food.refresh()
        snake.growing()

    if snake.head.xcor() > 280:
        game_is_on = False
        scoreboard.game_over()
    elif snake.head.ycor() > 300:
        game_is_on = False
        scoreboard.game_over()
    elif snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
    elif snake.head.xcor() < -300:
        game_is_on = False
        scoreboard.game_over()




screen.exitonclick()
