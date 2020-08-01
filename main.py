from tkinter import *

root = Tk()
root.geometry("800x800")
#variables
board_width = 530
board_height = 600
r = 65
img = PhotoImage(file="redDot.gif")

#change the color of the dot
def changeColor():
    board.itemconfig(1, fill='yellow')
    board.itemconfig(2, fill='yellow')
    board.itemconfig(3, fill='yellow')
    board.itemconfig(4, fill='yellow')
    board.itemconfig(5, fill='yellow')
    board.itemconfig(11, fill='yellow')
    board.itemconfig(12, fill='yellow')
    board.itemconfig(13, fill='yellow')
    board.itemconfig(14, fill='yellow')
    board.itemconfig(15, fill='yellow')

#create the grid of circles
def createGrid():
    for i in range(1,8,1):
        for j in range(1,7,1):
            dot = board.create_oval(75*i, 75*j, (75*i)-r, (75*j)-r, fill='black')


board = Canvas(width=board_width, height=board_height, bg='blue')
board.pack()
board.place(x=135, y=61)
createGrid()
B = Button(root, command=changeColor, image=img, width=60)
B.pack()
B.place(x=145, y=0)
root.mainloop()