from tkinter import *
global lb,list_label
list_label=[]
def showCross(event):
    global list_label
    lb = Label(w, text='十')
    list_label.append(lb)
    lb.place(x=event.x, y=event.y)
    text = '(x,y)=('+str(event.x)+','+str(event.y)+')'
    print(text)
def cancleCross(event):
    global list_label
    if(len(list_label) > 0):
        list_label[len(list_label)-1].destroy()
w = Tk()
w.title('Mouse Cross')
w.geometry('500x500')
w.bind('<Button-1>', showCross)
w.bind('<Double-Button-1>', cancleCross)
w.mainloop()
