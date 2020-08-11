from tkinter import *
from tkinter import messagebox as mb
import numpy as np

#canvas settings
root = Tk()
root.geometry("800x800")

#variables
board_width = 530
board_height = 600
diameter = 75
radius = 65
imgR = PhotoImage(file="redDot.gif")
imgY = PhotoImage(file="yellowDot.gif")
imgRe = PhotoImage(file="reset.gif")
button = []
col = [6,6,6,6,6,6,6]
#turn True: red; turn False: yellow
turn = True

#create the board
board = Canvas(width=board_width, height=board_height, bg='blue')
board.pack()
board.place(x=135, y=61)

def change_buttons():
    global turn
    if turn:
        for i in range(len(button)):
            button[i]['image'] = imgY
    else:
        for i in range(len(button)):
            button[i]['image'] = imgR
    
def check_winner(index):
    global turn
    buffer =[]
    conditions = np.array([[0, -7, -14, -21], [0, -1, -2, -3], [0, 5, 10, 15], [0, 6, 12, 18], [0, 7, 14, 21], [0, 1, 2, 3], [0, -5, -10, -15], [0, -6, -12, -18]])
    buffer = conditions + index
    root.update()
    for i in range(len(buffer)):
            if all(board.itemcget(buffer[i][n], "fill") == "red" for n in range(4)):
                print('winner!')
                for i in range(7):
                    button[i]['state'] = 'disabled'
                if mb.askyesno('Winner!', 'You Won! Play Again?'):
                    reset_grid()
            elif all(board.itemcget(buffer[i][n], "fill") == "yellow" for n in range(4)):
                for i in range(7):
                    button[i]['state'] = 'disabled'
                if mb.askyesno('Winner!', 'You Won! Play Again?'):
                    reset_grid()

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
    for i in range(7):
        for j in range(6):
            board.create_oval(diameter*(i+1), diameter*(j+1), (diameter*(i+1)-radius), (diameter*(j+1)-radius), fill='black')

def reset_grid():
    global col
    global turn
    global button
    for index in button:
        index['state'] = 'normal'
        index['image'] = imgR
    for i in range(1,43,1):
        board.itemconfig(i, fill='black')
        col = [6,6,6,6,6,6,6]
        turn = True

#create the array of buttons and place on the canvas
def create_buttons():
    for i in range(7):
        button.append(Button(root, command=lambda c=i: change_color(c), image=imgR, width=60))
        button[i].pack()
        button[i].place(x=(145+(diameter*i)), y=0)

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
        button[c]['state'] = 'disabled'
    
    check_winner(index)

def main():
    create_grid()
    create_buttons()
    reset = Button(root, command=reset_grid, image=imgRe, width=240)
    reset.pack()
    reset.place(x=270, y=700)
    root.mainloop()

if __name__ == "__main__":
    main()