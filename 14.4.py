from tkinter import *
from tkinter.messagebox import *


def log_in(event):
    file = open('infromation.txt', 'r')
    i = 0
    global user_name, user_code
    name = user_name.get()
    code = user_code.get()
    while True:
        username = file.readline()
        password = file.readline()
        if username == '':
            if i == 0:
                print(i)
                break
            else:
                i += 1
            break
        if name == username[:-1]:
            if code == password[:-1]:
                showinfo(title='提示！', message='登入成功！')
            else:
                showinfo(title='提示！', message='密码错误！')
        else:
            showinfo(title='提示！', message='不存在用户名！')

    file.close()


def log_up(event):
    global user_name, user_code
    name = user_name.get()
    code = user_code.get()
    file = open('infromation.txt', 'a')
    file.write(name)
    file.write('\n')
    file.write(code)
    file.write('\n')
    file.close()
    showinfo(title='提示！', message='注册成功！')

w = Tk()
w.title('Log In')
Label(w, text='请输入用户名和密码').pack(side=TOP, expand=YES)

fra1 = Frame(w)
user_name = StringVar()
Label(fra1, text='用户名').pack(side=LEFT, expand=YES)
Entry(fra1, textvariable=user_name).pack(side=RIGHT, expand=YES)
fra1.pack(side=TOP, fill=BOTH, expand=YES)

fra2 = Frame(w)
user_code = StringVar()
Label(fra2, text='密码').pack(side=LEFT, expand=YES)
Entry(fra2, textvariable=user_code).pack(side=RIGHT, expand=YES)
fra2.pack(side=TOP, fill=BOTH, expand=YES)

btn1 = Button(text='登录')
btn2 = Button(text='注册')
btn1.bind('<Button-1>', log_in)
btn2.bind('<Button-1>', log_up)
btn1.pack(side=LEFT)
btn2.pack(side=RIGHT)
w.mainloop()