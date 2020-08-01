from tkinter import *

board_width = 750
board_height = 750
r = 50
def createGrid():
    img = PhotoImage(file="redDot.gif")
    for i in range(8):
        for j in range(7):
            board.create_oval(100*i, 100*j, (100*i)-50, (100*j)-50)

root = Tk()

board = Canvas(width=board_width, height=board_height)
board.pack()
createGrid()
root.mainloop()