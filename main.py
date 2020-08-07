"""
Overall solid approach, there's a few things that could be improved upon but I
think it looks good. Annoylingly GitHub doesn't let you just comment on code
wherever you want so I'll just leave comments inline.

The biggest thing that I think would be improvement would be to make a few classes
to make this more object oriented. A good rule of thumb for when to make something
object oriented vs. functional is if you have state that needs to be maintained. So
for your case, the "board" and individual "buttons" all have state that can be saved
to their objects. So instead of having a bunch of global variables that you have to
keep track of, you'd just have classes that maintain that internally.

Here's a rough example of what that might look like. I don't know how tkinter works
so this might not exactly work for you, but it should hopefully get the general
design across.

class MyButton(object):
    def __init__(self, root, image, width):
        self.image = image
        # not 100% sure if the command=self.change_color thing would work but you get the idea
        self.button = Button(root, command=self.change_color, image=image, width=width)
        self.button.pack()

    def change_color(self):
        self.button.image = something

class Board(object):
    def __init__(self, width, height, background_color):
        self.board = Canvas(width=width, height=height, bg=background_color)
        self.board.pack()

        self.buttons = []
        for i in range(7):
            self.buttons.append(MyButton(root, imgR, 60))

    def check_winner(self):
        for button in self.buttons:
            # do stuff

"""
from tkinter import *
from tkinter import messagebox as mb
import numpy as np

#canvas settings
root = Tk()
root.geometry("800x800")

#variables
board_width = 530
board_height = 600
r = 65
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

def changeButtons():
    # This could be fixed with classes, but it's generally bad practice to have to
    # use global variables. It's a little more common in Python than other languages
    # but overall is best to avoid them unless absolutely necessary, they can get
    # really hard to maintain once a project gets bigger.
    global turn
    """
    Small thing - you can just do:
    if turn: # this implies True
        for i in ...
    else:
        ...
    """
    if turn == True:
        for i in range(len(button)):
            button[i]['image'] = imgY
    else:
        for i in range(len(button)):
            button[i]['image'] = imgR
    
def checkWinner(index):
    global turn
    buffer =[]
    # I haven't actually used numpy before (I know it's super popular) but I'm
    # curious what the numpy array does here differently than a normal array.
    #
    # Also, lots of "magic numbers" (actual term lol) in here, always good to avoid them when possible.
    conditions = np.array([[0, -7, -14, -21], [0, -1, -2, -3], [0, 5, 10, 15], [0, 6, 12, 18], [0, 7, 14, 21], [0, 1, 2, 3], [0, -5, -10, -15], [0, -6, -12, -18]])
    buffer = conditions + index
    root.update()
    for i in range(len(buffer)):
            # Python trick - I think this can be simplified to:
            # if all(board.itemcget(buffer[0][n], "fill") == "red" for n in range(4)):
            if board.itemcget(buffer[i][0], "fill") == 'red' and board.itemcget(buffer[i][1], "fill") == 'red' and board.itemcget(buffer[i][2], "fill") == 'red' and board.itemcget(buffer[i][3], "fill") == 'red':
                print('winner!')
                for i in range(7):
                    button[i]['state'] = 'disabled'
                if mb.askyesno('Winner!', 'You Won! Play Again?'):
                    resetGrid()
            elif board.itemcget(buffer[i][0], "fill") == 'yellow' and board.itemcget(buffer[i][1], "fill") == 'yellow' and board.itemcget(buffer[i][2], "fill") == 'yellow' and board.itemcget(buffer[i][3], "fill") == 'yellow':
                print('winner!')
                for i in range(7):
                    button[i]['state'] = 'disabled'
                if mb.askyesno('Winner!', 'You Won! Play Again?'):
                    resetGrid()

def turnSelect():
    global turn
    if turn == True:
        turn = False
        return str('red')
    elif turn == False:
        turn = True
        return str('yellow')

#create the grid of circles
def createGrid():
    for i in range(7):
        for j in range(6):
            # For a repeated number like this (75), it's usually good to put it in a variable, both
            # for reusability but more importantly to help descripe its purpose.
            # i.e. button_width = 75 (or whatever it is)
            board.create_oval(75*(i+1), 75*(j+1), (75*(i+1)-r), (75*(j+1)-r), fill='black')

def resetGrid():
    global col
    global turn
    global button
    """
    I've seen you do this in a few spots, which is the "typical" for-loop way to do it.
    In Python you can simplify it to this since "button" is a list:

    for ass in button:
        ass['state'] = 'normal'
        ass['image'] = imgR

    """
    for i in range(len(button)):
        button[i]['state'] = 'normal'
        button[i]['image'] = imgR
    for i in range(1,43,1):
        board.itemconfig(i, fill='black')
        col = [6,6,6,6,6,6,6]
        turn = True

#create the array of buttons and place on the canvas
def createButtons():
    for i in range(7):
        button.append(Button(root, command=lambda c=i: changeColor(c), image=imgR, width=60))
        button[i].pack()
        button[i].place(x=(145+(75*i)), y=0)

#change the color of the dot
def changeColor(c):
    #place the coin
    global col
    global button
    index = (c*6)+col[c]
    changeButtons()

    """
    You can probably remove this if statement entirely and instead do:

    board.itemconfig(index, fill=turnSelect())
    col[c] -=1
    print(col[c])

    Good rule of thumb is when you see a block of repeated code, you can
    almost always try and find a way to simplify/combine it.
    """
    if c == 0:
        board.itemconfig(index, fill=turnSelect())
        col[0] -=1
        print(col[0])
    elif c == 1:
        board.itemconfig(index, fill=turnSelect())
        col[1] -=1
        print(col[1])
    elif c == 2:
        board.itemconfig(index, fill=turnSelect())
        col[2] -=1
        print(col[2])
    elif c == 3:
        board.itemconfig(index, fill=turnSelect())
        col[3] -=1
        print(col[3])
    elif c == 4:
        board.itemconfig(index, fill=turnSelect())
        col[4] -=1
        print(col[4])
    elif c == 5:
        board.itemconfig(index, fill=turnSelect())
        col[5] -=1
        print(col[5])
    elif c == 6:
        board.itemconfig(index, fill=turnSelect())
        col[6] -=1
        print(col[6])

    # Nice, always fun to use any() and all()
    if any(t == 0 for t in col):
        col[c] = 6
        button[c]['state'] = 'disabled'
    
    checkWinner(index)


"""
This is small, but in Python the typical naming convention for functions
and variables is snake_case, so:

create_grid() instead of createGrid()

Several languages (like Java) prefer camelCase
"""
createGrid()
createButtons()
reset = Button(root, command=resetGrid, image=imgRe, width=240)
reset.pack()
reset.place(x=270, y=700)
root.mainloop()

"""
This is Python specific, but a good common practice to use:

def main():
    createGrid()
    createButtons()
    reset = ...
    ...

if __name__ == "__main__":
    main()

If you haven't seen this before, look it up for a good explanation. It's
weird syntax but has to do with how Python's internals work when running
scripts.
"""
