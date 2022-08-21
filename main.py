# --------------------------------------#
from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard
# --------------------------------------#
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('navy')
screen.title("Joseph's Snake Game")
screen.tracer(0)
# --------------------------------------#
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
# --------------------------------------#
screen.listen()  #listens for the users keyboard
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")  # <--- these are the controls of the game
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# --------------------------------------#

game_is_on = True

while game_is_on:
    screen.update()  #makes it so there is no delay between movements of body 1, 2 and 3.
    time.sleep(.1)
    snake.move()   #will move position 2 to 1, 3 to 2 and 1 to next position

    #Detect when head hits food
    if snake.head.distance(food) < 10:  #if the first segment of list is within 10 pixels of food, then refresh
        food.refresh()
        snake.extend()  #append the snake list so that body grows
        scoreboard.increase_score()

    #Detect when head hits wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False   #if the first segment hits the right wall, left wall, top wall or bottom wall then end.
        scoreboard.reset_scoreboard()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:  #This will ensure that we are checking for every part of the body except the head
        if snake.head.distance(segment) < 10:  #if the head hits any other part of the body, then game over
            # game_is_on = False
            scoreboard.reset_scoreboard()
            snake.reset()


screen.exitonclick()
