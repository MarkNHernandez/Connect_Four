from tkinter import *
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
    global turn
    if turn == True:
        for i in range(len(button)):
            button[i]['image'] = imgY
    else:
        for i in range(len(button)):
            button[i]['image'] = imgR
    
# def checkWinner(index):
#     global turn
#     buffer =[]
#     conditions = np.array([[0, -7, -14, -21], [0, -1, -2, -3], [0, 5, 10, 15], [0, 6, 12, 18], [0, 7, 14, 21], [0, 1, 2, 3], [0, -5, -10, -15], [0, -6, -12, -18]])
#     buffer = conditions + index
#     for i in range(len(buffer)):
#         for j in range(len(buffer[i])):
#             if all(board.itemcget(buffer[i][j], "fill") == 'red'):
#                 print('winner')

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
            board.create_oval(75*(i+1), 75*(j+1), (75*(i+1)-r), (75*(j+1)-r), fill='black')

def resetGrid():
    global col
    global turn
    global button
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
    changeButtons()
    if c == 0:
        board.itemconfig((c*6)+col[c], fill=turnSelect())
        col[0] -=1
        print(((c*6)+col[c]))
    elif c == 1:
        board.itemconfig((c*6)+col[c], fill=turnSelect())
        col[1] -=1
        print(col[1])
    elif c == 2:
        board.itemconfig((c*6)+col[c], fill=turnSelect())
        col[2] -=1
        print(col[2])
    elif c == 3:
        board.itemconfig((c*6)+col[c], fill=turnSelect())
        col[3] -=1
        print(col[3])
    elif c == 4:
        board.itemconfig((c*6)+col[c], fill=turnSelect())
        col[4] -=1
        print(col[4])
    elif c == 5:
        board.itemconfig((c*6)+col[c], fill=turnSelect())
        col[5] -=1
        print(col[5])
    elif c == 6:
        board.itemconfig((c*6)+col[c], fill=turnSelect())
        col[6] -=1
        print(col[6])
    if any(t == 0 for t in col):
        col[c] = 6
        button[c]['state'] = 'disabled'



createGrid()
createButtons()
reset = Button(root, command=resetGrid, image=imgRe, width=240)
reset.pack()
reset.place(x=270, y=700)
root.mainloop()
