from turtle import Turtle
import random
color1 = ["blue","red","green","yellow"]
class food1(Turtle):   #inherit the Turtle in the food1 class

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color(random.choice(color1))
        self.speed(("fastest"))
        self.new()


    def new(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)



