from turtle import Turtle
position = [(0,0),(20,0),(40,0)]
class Snake:

    def __init__(self):
        self.snake1 = []
        self.create_snake()
        self.head = self.snake1[0]

    def create_snake(self):
        for pos in position:  # creating the snake
            self.new_seg(pos)
    def new_seg(self,pos):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(pos)
        self.snake1.append(t)


    def extend(self):
        self.new_seg(self.snake1[-1].pos())


    def move(self):
        for i in range(len(self.snake1) - 1, 0, -1):
            new_x = self.snake1[i - 1].xcor()
            new_y = self.snake1[i - 1].ycor()
            self.snake1[i].goto(new_x, new_y)
        self.snake1[0].forward(20)

    def up(self):
        self.snake1[0].setheading(90)

    def down(self):
        self.snake1[0].setheading(270)


    def left(self):
        self.snake1[0].setheading(180)


    def right(self):
        self.snake1[0].setheading(0)





