from tkinter import *
from tkinter.messagebox import *


# 将框架（Frame ）的共同属性作为默认值，以简化创建过程
def my_frame(master):
    w = Frame(master)
    w.pack(side=TOP, expand=YES, fill=BOTH)
    return w


# 将标签（Label）的共同属性作为默认值，以简化创建过程
def my_entry(master, labelname, val):
    label = Label(master, text=labelname)
    label.pack(side=LEFT, expand=YES)
    entry = Entry(master, textvariable=val)
    entry.pack(side=RIGHT, expand=YES)
    return


def add_data(event):
    global name, phone_number, e_mail
    file = open('tongxunlu.txt', 'a')
    file.write(name.get()+'\n')
    file.write(phone_number.get() + '\n')
    file.write(e_mail.get() + '\n')
    file.close()
    showinfo(title='提示', message='创建成功!')


# 删除/创建联系人 功能
def create(event):
    top_wind = Toplevel()
    global name, phone_number, e_mail

    fra_top1 = my_frame(top_wind)
    name = StringVar()
    my_entry(fra_top1, '姓名', name)

    fra_top2 = my_frame(top_wind)
    phone_number = StringVar()
    my_entry(fra_top2, '电话号码', phone_number)

    fra_top3 = my_frame(top_wind)
    e_mail = StringVar()
    my_entry(fra_top3, '邮箱', e_mail)

    btn_top1 = Button(top_wind,text='确认')
    btn_top1.bind('<Button-1>', add_data)
    btn_top1.pack(side=LEFT)
    btn_top2 = Button(top_wind, text='取消')
    btn_top2.bind('<Button-1>', lambda event: top_wind.quit())
    btn_top2.pack(side=LEFT)


global name, phone_number, e_mail
main_wind = Tk()
main_wind.title('通讯录')

btn1 = Button(main_wind, text='创建联系人')
btn1.pack(side=LEFT)
btn1.bind('<Button-1>', create)
main_wind.mainloop()