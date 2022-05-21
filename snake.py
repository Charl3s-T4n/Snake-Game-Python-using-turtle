from turtle import Turtle
distance_moved = 20

# 0- East, 90-North, 180-West, 270-South (standard mode)----> because turtle starts out pointing East
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.snake_bodies = []
        self.create_snake()
       # can also create     self.head = self.snake_bodies[0], so that don't have to keep calling self.snake_bodies[0] below,
       #                                                       instead just need call self.head

    def create_snake(self):                                # For the initial 3 bodies of snake
        for index in range(3):                             # iterate through bodies of the snake
            self.add_body()

    def add_body(self):
        x_starting_position = 20
        snake = Turtle(shape="square")                     # Create new instance of snake object from Turtle() Class
        snake.color("white")                               # change color of snake to white
        snake.penup()                                      # remove the lines
        x_starting_position -= 20                          # first body will be at (0,0)
        snake.goto(x=x_starting_position, y=0)
        self.snake_bodies.append(snake)                    # append objects of snake bodies to empty list


    def extend_body(self):                                        # Create function that will extend snake body when collide with food
        x_position = self.snake_bodies[-1].xcor()                 # find the position of the last snake body
        y_position = self.snake_bodies[-1].ycor()
        snake_extend = Turtle(shape="square")                     # Create new instance of snake_extend object from Turtle() Class
        snake_extend.color("white")                               # change color of snake_extend to white
        snake_extend.penup()                                      # remove the lines
        snake_extend.goto(x=x_position, y=y_position)             # this new extended body will go to the snake previous last body
        self.snake_bodies.append(snake_extend)


    def move(self):
        for body_number in range(len(self.snake_bodies) - 1, 0, -1):        # where body 2 replace 1 and body 3 replace 2
            new_x = self.snake_bodies[
                body_number - 1].xcor()                                     # E.g: To find the x coordinate of the snake body infront of referenced body
            new_y = self.snake_bodies[body_number - 1].ycor()               # for the y coordinate
            self.snake_bodies[body_number].goto(x=new_x, y=new_y)           # E.g: Body 2 will now go to body 1's position
        self.snake_bodies[0].forward(distance_moved)                        # Move the first snake body forward by 20


# Create methods(snake can do) modelled by functions
# we only need change direction of snake's first body(snake_bodies[0]) since second and third body will follow
# Ensure snake can't change direction 180 degrees
    def up(self):
        if self.snake_bodies[0].heading() != DOWN:           # Can only go up if u are not facing down(CAN'T change direction 180 degrees)
            self.snake_bodies[0].setheading(UP)              # shift the first snake body upwards North

    def down(self):
        if self.snake_bodies[0].heading() != UP:             # Can only go down if not facing up
            self.snake_bodies[0].setheading(DOWN)            # shift first snake body downwards South

    def right(self):
        if self.snake_bodies[0].heading() != LEFT:           # Can only go right if not facing left
            self.snake_bodies[0].setheading(RIGHT)           # shift first snake body right Eastwards

    def left(self):
        if self.snake_bodies[0].heading() != RIGHT:          # Can only go left if not facing right
            self.snake_bodies[0].setheading(LEFT)            # shift first snake body left westwards




