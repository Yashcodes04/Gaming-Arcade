import time
from tkinter import *
import numpy as np
import tkinter as tk

from random import choice
from turtle import *
from freegames import floor, vector
def s():
    from turtle import Turtle ,Screen
    from food import food1
    from snake import Snake
    from score import Score
    screen = Screen()
    screen.setup(width=600,height=600) #setting up the screen
    screen.bgcolor("black") #background color of the screen
    screen.title("SNAKE GAME") #title of the project
    food = food1() #calling
    snake = Snake()
    score = Score()
    screen.tracer(0)
    game_on = True
    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")
    screen.onkey(snake.down, "s")

    while game_on:
        screen.update()
        time.sleep(0.1)

        snake.move()




    #detect the collision with the food

        if snake.head.distance(food) < 15:
            food.new()
            snake.extend()
            score.score_in()



    #to detect collision with the wall
        if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300:
            game_on = False
            score.game_over()

    #detection with the tail
        for segment in snake.snake1:
            if segment == snake.head:
                pass

            elif snake.head.distance(segment) < 0:
                game_on = False
                score.game_over()
#-------------------------------------------------------------------------
def d():
    size_of_board = 600
    number_of_dots = 6
    symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
    symbol_thickness = 50
    dot_color = '#7BC043'
    player1_color = '#0492CF'
    player1_color_light = '#67B0CF'
    player2_color = '#EE4035'
    player2_color_light = '#EE7E77'
    Green_color = '#7BC043'
    dot_width = 0.25 * size_of_board / number_of_dots
    edge_width = 0.1 * size_of_board / number_of_dots
    distance_between_dots = size_of_board / (number_of_dots)

    class Dots_and_Boxes():
        # ------------------------------------------------------------------
        # Initialization functions
        # ------------------------------------------------------------------
        def __init__(self):
            self.window = Tk()
            self.window.title('Dots_and_Boxes')
            self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
            self.canvas.pack()
            self.window.bind('<Button-1>', self.click)
            self.player1_starts = True
            self.refresh_board()
            self.play_again()

        def play_again(self):
            self.refresh_board()
            self.board_status = np.zeros(shape=(number_of_dots - 1, number_of_dots - 1))
            self.row_status = np.zeros(shape=(number_of_dots, number_of_dots - 1))
            self.col_status = np.zeros(shape=(number_of_dots - 1, number_of_dots))

            # Input from user in form of clicks
            self.player1_starts = not self.player1_starts
            self.player1_turn = not self.player1_starts
            self.reset_board = False
            self.turntext_handle = []

            self.already_marked_boxes = []
            self.display_turn_text()

        def mainloop(self):
            self.window.mainloop()

        # ------------------------------------------------------------------
        # Logical Functions:
        # The modules required to carry out game logic
        # ------------------------------------------------------------------

        def is_grid_occupied(self, logical_position, type):
            r = logical_position[0]
            c = logical_position[1]
            occupied = True

            if type == 'row' and self.row_status[c][r] == 0:
                occupied = False
            if type == 'col' and self.col_status[c][r] == 0:
                occupied = False

            return occupied

        def convert_grid_to_logical_position(self, grid_position):
            grid_position = np.array(grid_position)
            position = (grid_position - distance_between_dots / 4) // (distance_between_dots / 2)

            type = False
            logical_position = []
            if position[1] % 2 == 0 and (position[0] - 1) % 2 == 0:
                r = int((position[0] - 1) // 2)
                c = int(position[1] // 2)
                logical_position = [r, c]
                type = 'row'
                # self.row_status[c][r]=1
            elif position[0] % 2 == 0 and (position[1] - 1) % 2 == 0:
                c = int((position[1] - 1) // 2)
                r = int(position[0] // 2)
                logical_position = [r, c]
                type = 'col'

            return logical_position, type

        def mark_box(self):
            boxes = np.argwhere(self.board_status == -4)
            for box in boxes:
                if list(box) not in self.already_marked_boxes and list(box) != []:
                    self.already_marked_boxes.append(list(box))
                    color = player1_color_light
                    self.shade_box(box, color)

            boxes = np.argwhere(self.board_status == 4)
            for box in boxes:
                if list(box) not in self.already_marked_boxes and list(box) != []:
                    self.already_marked_boxes.append(list(box))
                    color = player2_color_light
                    self.shade_box(box, color)

        def update_board(self, type, logical_position):
            r = logical_position[0]
            c = logical_position[1]
            val = 1
            if self.player1_turn:
                val = - 1

            if c < (number_of_dots - 1) and r < (number_of_dots - 1):
                self.board_status[c][r] += val

            if type == 'row':
                self.row_status[c][r] = 1
                if c >= 1:
                    self.board_status[c - 1][r] += val

            elif type == 'col':
                self.col_status[c][r] = 1
                if r >= 1:
                    self.board_status[c][r - 1] += val

        def is_gameover(self):
            return (self.row_status == 1).all() and (self.col_status == 1).all()

        # ------------------------------------------------------------------
        # Drawing Functions:
        # The modules required to draw required game based object on canvas
        # ------------------------------------------------------------------

        def make_edge(self, type, logical_position):
            if type == 'row':
                start_x = distance_between_dots / 2 + logical_position[0] * distance_between_dots
                end_x = start_x + distance_between_dots
                start_y = distance_between_dots / 2 + logical_position[1] * distance_between_dots
                end_y = start_y
            elif type == 'col':
                start_y = distance_between_dots / 2 + logical_position[1] * distance_between_dots
                end_y = start_y + distance_between_dots
                start_x = distance_between_dots / 2 + logical_position[0] * distance_between_dots
                end_x = start_x

            if self.player1_turn:
                color = player1_color
            else:
                color = player2_color
            self.canvas.create_line(start_x, start_y, end_x, end_y, fill=color, width=edge_width)

        def display_gameover(self):
            player1_score = len(np.argwhere(self.board_status == -4))
            player2_score = len(np.argwhere(self.board_status == 4))

            if player1_score > player2_score:
                # Player 1 wins
                text = 'Winner: Player 1 '
                color = player1_color
            elif player2_score > player1_score:
                text = 'Winner: Player 2 '
                color = player2_color
            else:
                text = 'Its a tie'
                color = 'gray'

            self.canvas.delete("all")
            self.canvas.create_text(size_of_board / 2, size_of_board / 3, font="cmr 60 bold", fill=color, text=text)

            score_text = 'Scores \n'
            self.canvas.create_text(size_of_board / 2, 5 * size_of_board / 8, font="cmr 40 bold", fill=Green_color,
                                    text=score_text)

            score_text = 'Player 1 : ' + str(player1_score) + '\n'
            score_text += 'Player 2 : ' + str(player2_score) + '\n'
            # score_text += 'Tie                    : ' + str(self.tie_score)
            self.canvas.create_text(size_of_board / 2, 3 * size_of_board / 4, font="cmr 30 bold", fill=Green_color,
                                    text=score_text)
            self.reset_board = True

            score_text = 'Click to play again \n'
            self.canvas.create_text(size_of_board / 2, 15 * size_of_board / 16, font="cmr 20 bold", fill="gray",
                                    text=score_text)

        def refresh_board(self):
            for i in range(number_of_dots):
                x = i * distance_between_dots + distance_between_dots / 2
                self.canvas.create_line(x, distance_between_dots / 2, x,
                                        size_of_board - distance_between_dots / 2,
                                        fill='gray', dash=(2, 2))
                self.canvas.create_line(distance_between_dots / 2, x,
                                        size_of_board - distance_between_dots / 2, x,
                                        fill='gray', dash=(2, 2))

            for i in range(number_of_dots):
                for j in range(number_of_dots):
                    start_x = i * distance_between_dots + distance_between_dots / 2
                    end_x = j * distance_between_dots + distance_between_dots / 2
                    self.canvas.create_oval(start_x - dot_width / 2, end_x - dot_width / 2, start_x + dot_width / 2,
                                            end_x + dot_width / 2, fill=dot_color,
                                            outline=dot_color)

        def display_turn_text(self):
            text = 'Next turn: '
            if self.player1_turn:
                text += 'Player1'
                color = player1_color
            else:
                text += 'Player2'
                color = player2_color

            self.canvas.delete(self.turntext_handle)
            self.turntext_handle = self.canvas.create_text(size_of_board - 5 * len(text),
                                                           size_of_board - distance_between_dots / 8,
                                                           font="cmr 15 bold", text=text, fill=color)

        def shade_box(self, box, color):
            start_x = distance_between_dots / 2 + box[1] * distance_between_dots + edge_width / 2
            start_y = distance_between_dots / 2 + box[0] * distance_between_dots + edge_width / 2
            end_x = start_x + distance_between_dots - edge_width
            end_y = start_y + distance_between_dots - edge_width
            self.canvas.create_rectangle(start_x, start_y, end_x, end_y, fill=color, outline='')

        def display_turn_text(self):
            text = 'Next turn: '
            if self.player1_turn:
                text += 'Player1'
                color = player1_color
            else:
                text += 'Player2'
                color = player2_color

            self.canvas.delete(self.turntext_handle)
            self.turntext_handle = self.canvas.create_text(size_of_board - 5 * len(text),
                                                           size_of_board - distance_between_dots / 8,
                                                           font="cmr 15 bold", text=text, fill=color)

        def click(self, event):
            if not self.reset_board:
                grid_position = [event.x, event.y]
                logical_positon, valid_input = self.convert_grid_to_logical_position(grid_position)
                if valid_input and not self.is_grid_occupied(logical_positon, valid_input):
                    self.update_board(valid_input, logical_positon)
                    self.make_edge(valid_input, logical_positon)
                    self.mark_box()
                    self.refresh_board()
                    self.player1_turn = not self.player1_turn

                    if self.is_gameover():
                        # self.canvas.delete("all")
                        self.display_gameover()
                    else:
                        self.display_turn_text()
            else:
                self.canvas.delete("all")
                self.play_again()
                self.reset_board = False

    game_instance = Dots_and_Boxes()
    game_instance.mainloop()
#--------------------------------------------------------------------------------------------------------

def p(): #brick breaker


    class GameObject(object):
        def __init__(self, canvas, item):
            self.canvas = canvas
            self.item = item

        def get_position(self):
            return self.canvas.coords(self.item)

        def move(self, x, y):
            self.canvas.move(self.item, x, y)

        def delete(self):
            self.canvas.delete(self.item)

    class Ball(GameObject):
        def __init__(self, canvas, x, y):
            self.radius = 10
            self.direction = [1, -1]
            # increase the below value to increase the speed of ball
            self.speed = 5
            item = canvas.create_oval(x - self.radius, y - self.radius,
                                      x + self.radius, y + self.radius,
                                      fill='white')
            super(Ball, self).__init__(canvas, item)

        def update(self):
            coords = self.get_position()
            width = self.canvas.winfo_width()
            if coords[0] <= 0 or coords[2] >= width:
                self.direction[0] *= -1
            if coords[1] <= 0:
                self.direction[1] *= -1
            x = self.direction[0] * self.speed
            y = self.direction[1] * self.speed
            self.move(x, y)

        def collide(self, game_objects):
            coords = self.get_position()
            x = (coords[0] + coords[2]) * 0.5
            if len(game_objects) > 1:
                self.direction[1] *= -1
            elif len(game_objects) == 1:
                game_object = game_objects[0]
                coords = game_object.get_position()
                if x > coords[2]:
                    self.direction[0] = 1
                elif x < coords[0]:
                    self.direction[0] = -1
                else:
                    self.direction[1] *= -1

            for game_object in game_objects:
                if isinstance(game_object, Brick):
                    game_object.hit()

    class Paddle(GameObject):
        def __init__(self, canvas, x, y):
            self.width = 80
            self.height = 10
            self.ball = None
            item = canvas.create_rectangle(x - self.width / 2,
                                           y - self.height / 2,
                                           x + self.width / 2,
                                           y + self.height / 2,
                                           fill='#FFB643')
            super(Paddle, self).__init__(canvas, item)

        def set_ball(self, ball):
            self.ball = ball

        def move(self, offset):
            coords = self.get_position()
            width = self.canvas.winfo_width()
            if coords[0] + offset >= 0 and coords[2] + offset <= width:
                super(Paddle, self).move(offset, 0)
                if self.ball is not None:
                    self.ball.move(offset, 0)

    class Brick(GameObject):
        COLORS = {1: '#4535AA', 2: '#ED639E', 3: '#8FE1A2'}

        def __init__(self, canvas, x, y, hits):
            self.width = 75
            self.height = 20
            self.hits = hits
            color = Brick.COLORS[hits]
            item = canvas.create_rectangle(x - self.width / 2,
                                           y - self.height / 2,
                                           x + self.width / 2,
                                           y + self.height / 2,
                                           fill=color, tags='brick')
            super(Brick, self).__init__(canvas, item)

        def hit(self):
            self.hits -= 1
            if self.hits == 0:
                self.delete()
            else:
                self.canvas.itemconfig(self.item,
                                       fill=Brick.COLORS[self.hits])

    class Game(tk.Frame):
        def __init__(self, master):
            super(Game, self).__init__(master)
            self.lives = 3
            self.width = 610
            self.height = 400
            self.canvas = tk.Canvas(self, bg='#D6D1F5',
                                    width=self.width,
                                    height=self.height, )
            self.canvas.pack()
            self.pack()

            self.items = {}
            self.ball = None
            self.paddle = Paddle(self.canvas, self.width / 2, 326)
            self.items[self.paddle.item] = self.paddle
            # adding brick with different hit capacities - 3,2 and 1
            for x in range(5, self.width - 5, 75):
                self.add_brick(x + 37.5, 50, 3)
                self.add_brick(x + 37.5, 70, 2)
                self.add_brick(x + 37.5, 90, 1)

            self.hud = None
            self.setup_game()
            self.canvas.focus_set()
            self.canvas.bind('<Left>',
                             lambda _: self.paddle.move(-10))
            self.canvas.bind('<Right>',
                             lambda _: self.paddle.move(10))

        def setup_game(self):
            self.add_ball()
            self.update_lives_text()
            self.text = self.draw_text(300, 200,
                                       'Press Space to start')
            self.canvas.bind('<space>', lambda _: self.start_game())

        def add_ball(self):
            if self.ball is not None:
                self.ball.delete()
            paddle_coords = self.paddle.get_position()
            x = (paddle_coords[0] + paddle_coords[2]) * 0.5
            self.ball = Ball(self.canvas, x, 310)
            self.paddle.set_ball(self.ball)

        def add_brick(self, x, y, hits):
            brick = Brick(self.canvas, x, y, hits)
            self.items[brick.item] = brick

        def draw_text(self, x, y, text, size='40'):
            font = ('Forte', size)
            return self.canvas.create_text(x, y, text=text,
                                           font=font)

        def update_lives_text(self):
            text = 'Lives: %s' % self.lives
            if self.hud is None:
                self.hud = self.draw_text(50, 20, text, 15)
            else:
                self.canvas.itemconfig(self.hud, text=text)

        def start_game(self):
            self.canvas.unbind('<space>')
            self.canvas.delete(self.text)
            self.paddle.ball = None
            self.game_loop()

        def game_loop(self):
            self.check_collisions()
            num_bricks = len(self.canvas.find_withtag('brick'))
            if num_bricks == 0:
                self.ball.speed = None
                self.draw_text(300, 200, 'You win! You the Breaker of Bricks.')
            elif self.ball.get_position()[3] >= self.height:
                self.ball.speed = None
                self.lives -= 1
                if self.lives < 0:
                    self.draw_text(300, 200, 'You Lose! Game Over!')
                else:
                    self.after(1000, self.setup_game)
            else:
                self.ball.update()
                self.after(50, self.game_loop)

        def check_collisions(self):
            ball_coords = self.ball.get_position()
            items = self.canvas.find_overlapping(*ball_coords)
            objects = [self.items[x] for x in items if x in self.items] 
            self.ball.collide(objects)

    if __name__ == '__main__':
        root = tk.Tk()
        root.title('Break those Bricks!')
        game = Game(root)
        game.mainloop()



window = Tk()
window.title(" GAMING ARCADE ")
my_label = Label(text="THE GAMING ARCADE",font=("Arial",24,"bold"))
my_label.pack()
canvas = Canvas(width=900,height=700,bg="black")
snake_img = PhotoImage(file=r"C:\Users\Yash\Desktop\pr1.png")
canvas.create_image(440,300,image=snake_img)
canvas.pack()

button_1 = Button(text="START GAME \n Use arrow keys to move",command=p) #wall breaker
button_1.place(x=380,y=500)
button_2=Button(text="START GAME \n use wasd to move the snake ",command=s) #snake game
button_2.place(x=50,y=500)
button_3=Button(text="START GAME \n just click on the dots the play ",command=d) #dots game
button_3.place(x=670,y=500)
window.mainloop()






#screen.exitonclick()