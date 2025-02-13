from tkinter import *
import tkinter as tk

frame = tk.Tk()

frame.geometry("300x300")
frame.title("Tic-Tac-Toe")
canvas=Canvas(frame, width=500, height=300)

cross = False
circle = True

board = [['' for _ in range(3)] for _ in range(3)]

def on_click(event):
    global cross, circle

    row = event.y // 100
    col = event.x // 100

    if board[row][col] != '':
        return

    if (cross == False and circle == True):
        game_shape = "O"
    elif (cross == True and circle == False):
        game_shape = "X"

    if col == 0:
        if row == 0:
            canvas.create_text(70, 70, text=game_shape, font=("Courier", 40))
        elif row == 1:
            canvas.create_text(70, 150, text=game_shape, font=("Courier", 40))
        elif row == 2:
            canvas.create_text(70, 235, text=game_shape, font=("Courier", 40))
    elif col == 1:
        if row == 0:
            canvas.create_text(150, 70, text=game_shape, font=("Courier", 40))
        elif row == 1:
            canvas.create_text(150, 150, text=game_shape, font=("Courier", 40))
        elif row == 2:
            canvas.create_text(150, 235, text=game_shape, font=("Courier", 40))
    elif col == 2:
        if row == 0:
            canvas.create_text(229, 70, text=game_shape, font=("Courier", 40))
        elif row == 1:
            canvas.create_text(229, 150, text=game_shape, font=("Courier", 40))
        elif row == 2:
            canvas.create_text(229, 235, text=game_shape, font=("Courier", 40))

    board[row][col] = game_shape

    circle = not circle
    cross = not cross

canvas.pack()
canvas.create_line(50, 200, 250, 200, fill="black", width=5)
canvas.create_line(50, 100, 250, 100, fill="black", width=5)
canvas.create_line(100, 50, 100, 250, fill="black", width=5)
canvas.create_line(200, 50, 200, 250, fill="black", width=5)
canvas.bind("<Button-1>", on_click)
frame.mainloop()
