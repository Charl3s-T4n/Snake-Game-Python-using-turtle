import time
from turtle import Screen               # import Screen Class from turtle module
from snake import Snake                 # import Snake Class from snake file
from food import Food                   # import Food Class from food file
from scoreboard import Scoreboard       # import Scoreboard Class from scoreboard file

screen = Screen()                            # create new instance of object screen
screen.setup(width=600, height=600)          # call the method setup()---> to get specific width and height of window
screen.bgcolor("black")                      # Set background color
screen.title("My Snake Game")                # Set title of screen window
screen.tracer(0)                             # turn tracer method of screen class to off

snake = Snake()                # Create snake object from class Snake
food = Food()                  # Create food object from class Food
scoreboard = Scoreboard()      # Create scoreboard object from class Scoreboard

screen.listen()                # screen.listen() to tell screen to listen to what keypress user press
screen.onkey(snake.up, "Up")        # access the method up/down/right/left in snake Class ----> represents arrow keys
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_continues = True                    # Create flag variable
while game_continues:                    # while True
    screen.update()                      # Updates/ refresh the display on the screen
    time.sleep(0.1)                      # adds a delay (in seconds) after each snake body moves
    snake.move()
                                                     # STEP 4: Detect snake collision with food
    if snake.snake_bodies[0].distance(food) < 15:    # if distance between snake and food is <15 pixels (food is 10x10)
        food.refresh()                               # when snake collides with food: call the method refresh() from food object
        scoreboard.increase_score()                  # call the method increase_score() from object scoreboard of class Scoreboard
        snake.extend_body()                          # extend body of snake when hits food

                                                       # STEP 6: Detect snake collision with wall
    if snake.snake_bodies[0].xcor() > 280 or snake.snake_bodies[0].xcor() < -280 or snake.snake_bodies[0].ycor() >280 or snake.snake_bodies[0].ycor() < -280:
        scoreboard.collide_wall_and_lost()
        game_continues = False                         # ends while loop, stop game

                                                         # STEP 7: Detect snake collision with tail
    for body in snake.snake_bodies[1:]:                  # LIST SLICING: don't count head of snake(from second body to end of body)
        if snake.snake_bodies[0].distance(body) < 10:    # elif distance between head of snake and any part of snake is <10--> count as touch
            scoreboard.collide_tail_and_lost()
            game_continues = False                       # ends while loop, stop game


screen.exitonclick()                                     # window only closes when i click outside

