from turtle import Turtle
import random

# Create Food class that will inherit from Turtle class
class Food(Turtle):                  # Add in superclass 'Turtle' in parentheses: class 'Food' will now inherit attributes/methods from Superclass

    def __init__(self):
        super().__init__()                                  # Add Call to superclass initialise
        self.shape("circle")                                # use superclass method to change shape
        self.penup()                                        # so that pen won't leave behind marking on screen
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)    # half the size of the circle (food)--> 20x20 to 10x10
        self.color("blue")                                  # set color of food
        self.speed("fastest")                               # so that i don't have to look at animation of food being created on screen
        random_x = random.randint(-280,280)                 # get random x coordinate of food
        random_y = random.randint(-280,280)                 # get random y coordinate of food
        self.goto(random_x, random_y)

    def refresh(self):                          # food will be shown on diff random position
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)