from tkinter import *
import random

number = random.randint(1, 1000)
running, num, nmax, nmin = True, 0, 1000, 1


def btnClose(event):
    w.destroy()  # 退出主窗口


def btnGuess(event):
    global nmax, nmin, num, running
    if running:
        val1 = int(ent.get())
        if val1 == number:
            lbl_qv("恭喜，答对了！")
            num += 1
            running = False
            numGuess()
        elif val1 < number:
            if val1 > nmin:
                nmin = val1
                num += 1
                lbl_min.config(lbl_min, text=nmin)
            lbl_qv("猜小了，请重新输入！")
        else:
            if val1 < nmax:
                nmax = val1
                num += 1
                lbl_max.config(lbl_max, text=nmax)
            lbl_qv("猜大了，请重新输入！")
    else:
        lbl_qv("已经答对了！")


def numGuess():
    if num == 1:
        lbl_qv("恭喜，一次答对！")
    elif num <= 15:
        lbl_qv("答对了，尝试次数：" + str(num))
    else:
        lbl_qv("超过15次了")


def lbl_qv(vtxt):
    lbl_q.config(lbl_q, text=vtxt)


w = Tk()
w.title("猜数字游戏")
w.geometry("300x120+200+200")
frm1 = LabelFrame(w, text="数字范围")
lbl_max = Label(frm1, text=nmax)
lbl_max.pack(side=TOP, fill=X)
lbl_min = Label(frm1, text=nmin)
lbl_min.pack(side=BOTTOM, fill=X)
frm1.pack(side=LEFT, fill=X)
frm2 = LabelFrame(w)
lbl_q = Label(frm2, width=25)
lbl_qv("请输入[1,1000]之间的整数：")
lbl_q.pack(side=TOP)
ent = Entry(frm2, width=10)
ent.pack(side=BOTTOM)
ent.bind("<Return>", btnGuess)
frm2.pack(side=LEFT, fill=X)
frm3 = Frame(w, relief="groove")
btnG = Button(frm3, text="开  始")
btnG.bind("<Button-1>", btnGuess)
btnG.pack(side=TOP)
btnC = Button(frm3, text="退  出")
btnC.bind("<Button-1>", btnClose)
btnC.pack(side=BOTTOM)
frm3.pack(side=LEFT, fill=X)
ent.focus_set()
w.mainloop()
