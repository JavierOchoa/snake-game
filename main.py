from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.title('SnKGame')
screen.setup(600, 600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.down, 'Down')

is_On = True
while is_On:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.points()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_On = False
        scoreboard.gameOver()

    for segment in snake.all_segments[1::]:
        if snake.head.distance(segment) < 10:
            is_On = False
            scoreboard.gameOver()
            
    
    # for segment in snake.all_segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         is_On = False
    #         scoreboard.gameOver()
            
screen.exitonclick()