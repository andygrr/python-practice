from tkinter import *


def callb():
    w.config(bg=tf[int(v.get())])


w = Tk()
w.title("改变窗口背景颜色")
w.geometry("250x100")
v = StringVar()
v.set('2')  # 将第三个单选按钮设为默认按钮
f = Frame(w, bd=4, relief=GROOVE)  # 建立框架
f.pack()
tf = ['red', 'blue', 'yellow']
for n in range(len(tf)):
    r = Radiobutton(f, variable=v, text=tf[n], value=n, command=callb)
    r.grid(row=n, column=1, sticky=W)  # 靠左放
w.mainloop()
