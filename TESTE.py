from tkinter import *
window = Tk()
window.grid()
window.array = []
canvas = Canvas(window, width = 1320, height=700)
canvas.grid(row=0, column=0, sticky="news")
produtos_frame = Frame(canvas)
canvas.create_window((0, 0), window=produtos_frame, anchor='ne')
