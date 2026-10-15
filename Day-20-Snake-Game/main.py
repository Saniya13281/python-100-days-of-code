import time
from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Welcome to the Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #Detect collision with food
    if snake.segments[0].distance(food) < 15 :
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect Collision  with wall
    if snake.segments[0].xcor() > 280 or  snake.segments[0].xcor() < -280 or  snake.segments[0].ycor() > 280 or  snake.segments[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    #if head collides with any segment in tail
    #trigger game over


screen.exitonclick()

