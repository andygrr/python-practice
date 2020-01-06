from tkinter import *

def showMes():
    Message(w, text = 'hello uestc!').grid(row = 0, sticky = E+W)
w=Tk()
w.title('show')
w.geometry("250x100")
btn = Button(w, command = showMes, text = 'OK')
btn.pack(side = LEFT)