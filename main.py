from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)

snake = Snake()


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





#
#
#
#
# snake.shape("square")
# snake.color("white")
# snake.shapesize(stretch_wid=None, stretch_len=3, outline=None)
# snake.penup()
# snake.goto(x=-20, y=0)
# game_is_on = True
#
# while game_is_on:
#     screen.listen()
#     screen.onkey(key="w", fun=move_forward)
#     screen.onkey(key="s", fun=move_backward)
#     screen.onkey(key="a", fun=move_counter_clockwise)
#     screen.onkey(key="d", fun=move_clockwise)
#     snake.forward(5)





screen.exitonclick()
