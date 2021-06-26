from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = []
x_start = 0

for segment in range(0, 3):
    segment = Turtle()
    segment.shape("square")
    segment.color("white")
    segment.penup()
    segment.setpos(x_start, 0)
    snake.append(segment)
    x_start -= 20



game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for segment in snake:
        segment.forward(20)










screen.exitonclick()