from tkinter import *
from tkinter import messagebox as mb
from enum import Enum

#region Properties
screen_width = 800
screen_height = 800
board_width = 530
board_height = 600
board_position_x = 0
board_position_y = 65
dot_diameter = 75
dot_radius = 65
number_of_rows = 6
number_of_columns = 7

#endregion

#canvas settings
root = Tk()
root.geometry("{}x{}".format(screen_width, screen_height))
image_red_dot = PhotoImage(file="redDot.gif")
image_yellow_dot = PhotoImage(file="yellowDot.gif")
image_reset = PhotoImage(file="reset.gif")
#create the board

#region Classes

class State(Enum):
    empty = 0
    player_one = 1
    player_two = 2

class Color(str, Enum):
    BLACK = "black"
    RED = "red"
    YELLOW = "yellow"

class GameButton(object):
    def __init__(self, game, column, image, width):
        self.image = image
        self.game = game
        self.state = State.player_one
        self.column = column
        self.tk = Button(root, command = self.change_color, image = self.image, width = width)
        self.tk.grid(row = 0, column=column, padx = 5)
    
    def change_color(self):
        if (self.state == State.player_one):
            for button in self.game.buttons:
                button.tk.configure(image=image_yellow_dot)
            self.game.dots[3].itemconfig(fill="red")
            self.state = State.player_two
        elif(self.state == State.player_two):
            for button in self.game.buttons:
                button.tk.configure(image=image_red_dot)
            self.state = State.player_one
        else:
            print("Error in turns")

class Dot:
    def __init__(self, board, row, column, diameter, radius):
        self.row = row
        self.column = column
        self.fill = Color.BLACK
        self.state = State.empty
        self.oval = board.create_oval(diameter*(row), 
                                      diameter*(column),
                                      (diameter*(row)-radius),
                                      (diameter*(column)-radius),
                                      fill = self.fill)
    def change_color(self):
        self.oval.configure(fill="red")
    def reset(self):
        self.oval.fill = Color.BLACK
        self.state = State.empty

class Board(object):
    def __init__(self, width, height, x_placement, y_placement, background_color):
        self.board = Canvas(width=width, height=height, bg=background_color)
        self.board.pack()
        self.board.place(x=x_placement, y=y_placement)
    
        self.dots = []
        for i in range(1, number_of_columns+1):
            for j in range(1, number_of_rows+1):
                self.dots.append(Dot(self.board, i, j, dot_diameter, dot_radius))

        self.buttons = []
        for i in range(number_of_columns):
            self.buttons.append(GameButton(self, i,  image_red_dot, 60))

        
#endregion

def main():
    game = Board(board_width, board_height, board_position_x, board_position_y, "blue")
    root.mainloop()

if __name__ == "__main__":
    main()
     