from turtle import Turtle

ALIGNMENT = "center"                     # Set constants as variables at top: so i can change easily
FONT = ("Arial", 24, "normal")           # instead of scrolling down and find to replace
FONT_POPUP = ("Arial", 14, "normal")

# create Scoreboard class that will inherit from superclass Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()                # Add superclass call
        self.score = 0
        self.penup()                      # no drawing when moving to the goto coordinates
        self.goto(x=0, y=250)             # to shift to top of screen
        self.color("white")               # whatever u type below will be white
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()                 # to hide the cursor (that represents turtle, because we only need the text)

    def increase_score(self):
        self.clear()                       # clear the previous score on the screen whenever snake hits food
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def collide_wall_and_lost(self):       # Create method that will show user on screen they hit the wall and lost
        self.color("red")                  # text will be red
        self.goto(x=0, y=0)                # center the pop up text in middle of screen
        self.write(f"You have hit the wall and lost. Your score: {self.score}", align=ALIGNMENT, font=FONT_POPUP)

    def collide_tail_and_lost(self):
        self.color("yellow")
        self.goto(x=0, y=0)
        self.write(f"You have hit yourself and lost. You score: {self.score}", align=ALIGNMENT, font=FONT_POPUP)