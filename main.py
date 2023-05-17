from tkinter import *
from tkinter import messagebox as mb
from enum import Enum


#region Classes

class State(Enum):
    empty = 0
    player_one = 1
    player_two = 2

class Game():
    def __init__(self):
        self.turn = State.player_one
        self.winner = False

class Color(str, Enum):
    BLACK = "black"
    RED = "red"
    YELLOW = "yellow"

class Dot:
    def __init__(self, row, column, diameter, radius):
        self.row = row
        self.column = column
        self.fill = Color.BLACK
        self.state = State.empty
        board.create_oval(diameter*(row), 
                          diameter*(column), 
                          (diameter*(row)-radius), 
                          (diameter*(column)-radius), 
                          fill = Color.BLACK)
    def reset(self):
        fill = Color.BLACK
        state = State.empty

class Game_Button:
    def __init__(self, column):
       self.column = column
       Button(root, 
              command = change_color(), 
              image=image_red_dot, 
              width=60) 
    

#endregion


#region Properties

screen_width = 800
screen_height = 800
board_width = 530
board_height = 600
dot_diameter = 75
dot_radius = 65
buttons = []
dots = []
col = [6,6,6,6,6,6,6]
turn = True

#endregion

#canvas settings
root = Tk()
root.geometry("800x800")
image_red_dot = PhotoImage(file="redDot.gif")
image_yellow_dot = PhotoImage(file="yellowDot.gif")
image_reset = PhotoImage(file="reset.gif")
#create the board
board = Canvas(width=board_width, height=board_height, bg='blue')
board.pack()
board.place(x=135, y=61)
 
def turn_select():
    global turn
    if turn == True:
        turn = False
        return str('red')
    elif turn == False:
        turn = True
        return str('yellow')

#create the grid of circles
def create_grid():
    for i in range(1,7):
        for j in range(1,8):
            dots.append(Dot(j, i, dot_diameter, dot_radius))

def reset_grid():
    for dot in dots:
        dot.reset()

#create the array of buttons and place on the canvas
def create_buttons():
    for i in range(7):
        buttons.append()
        buttons[i].pack()
        buttons[i].place(x=(145+(dot_diameter*i)), y=0)

#change the color of the dot
def change_color(c):
    #place the coin
    global col
    global button
    index = (c*6)+col[c]
    change_buttons()

    board.itemconfig(index, fill=turn_select())
    col[c] -=1
    print(col[c])

    if any(t == 0 for t in col):
        col[c] = 6
        buttons[c]['state'] = 'disabled'
    
    check_winner(index)

def main():
    create_grid()
    create_buttons()
    reset = Button(root, command=reset_grid, image=image_reset, width=240)
    reset.pack()
    reset.place(x=270, y=700)
    root.mainloop()

if __name__ == "__main__":
    main()
     
