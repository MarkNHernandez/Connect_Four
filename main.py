from tkinter import *

#canvas settings
root = Tk()
root.geometry("800x800")

#variables
board_width = 530
board_height = 600
r = 65
img = PhotoImage(file="redDot.gif")
button = []
col = [6,6,6,6,6,6,6]
#turn 0: red turn 1: yellow
turn = True

#create the board
board = Canvas(width=board_width, height=board_height, bg='blue')
board.pack()
board.place(x=135, y=61)

##DON'T JUDGE THIS, IT'S A WORK IN PROGRESS

# def checkWinner(index):
#     #back and to the left
#     conditions = [[0, -7, -14, -21], [0, -1, -2, -3], [0, 5, 10, 15], [0, 6, 12, 18], [0, 7, 14, 21], [0, 1, 2, 3], [0, -5, -10, -15], [0, -6, -12, -18]]
#     for i in range(len(conditions)):
#         for j in range(len(conditions[i])):
#             if any(board.itemcget(index+j, "fill") == 'red'):
#                 print('winner')
#     color = board.itemcget(index, "fill")
#     print(color)

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
    for i in range(1,43,1):
        board.itemconfig(i, fill='black')
        col = [6,6,6,6,6,6,6]
        turn = True


#create the array of buttons and place on the canvas
def createButtons():
    for i in range(7):
        button.append(Button(root, command=lambda c=i: changeColor(c), image=img, width=60))
        button[i].pack()
        button[i].place(x=(145+(75*i)), y=0)

#change the color of the dot
def changeColor(c):
    #place the coin
    global col
    global button
    if c == 0:
        board.itemconfig((c*6)+col[c], fill=turnSelect())
        col[0] -=1
        #checkWinner(((c*6)+col[c])+1)
        print(((c*6)+col[c]))
    elif c == 1:
        board.itemconfig((c*6)+col[c], fill=turnSelect())
        col[1] -=1
        #checkWinner(((c*6)+col[c])+1)
        print(col[1])
    elif c == 2:
        board.itemconfig((c*6)+col[c], fill=turnSelect())
        col[2] -=1
        #checkWinner(((c*6)+col[c])+1)
        print(col[2])
    elif c == 3:
        board.itemconfig((c*6)+col[c], fill=turnSelect())
        col[3] -=1
        #checkWinner(((c*6)+col[c])+1)
        print(col[3])
    elif c == 4:
        board.itemconfig((c*6)+col[c], fill=turnSelect())
        col[4] -=1
        #checkWinner(((c*6)+col[c])+1)
        print(col[4])
    elif c == 5:
        board.itemconfig((c*6)+col[c], fill=turnSelect())
        col[5] -=1
        #checkWinner(((c*6)+col[c])+1)
        print(col[5])
    elif c == 6:
        board.itemconfig((c*6)+col[c], fill=turnSelect())
        col[6] -=1
        #checkWinner(((c*6)+col[c])+1)
        print(col[6])
    if any(t == 0 for t in col):
        col[c] = 6
        button[c]['state'] = 'disabled'



createGrid()
createButtons()
reset = Button(root, command=resetGrid, image=img, width=60)
reset.pack()
reset.place(x=370, y=700)
root.mainloop()
