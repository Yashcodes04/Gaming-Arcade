from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.update_score()
        self.hideturtle()
    def update_score(self):
        self.write(f"Score: {self.score1}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(x=0,y=0)
        self.write("U DIED" , align="center" , font=("Arial", 24 , "normal"))



    def score_in(self):
        self.score1 +=1
        self.clear()
        self.update_score()




