from tkinter import *


# 将框架（Frame ）的共同属性作为默认值，以简化创建过程
def my_frame(master):
    w = Frame(master)
    w.pack(side=TOP, expand=YES, fill=BOTH)
    return w


# 按下回车键开始加密
def change_code(event):
    global text, key, text1
    a = text.get()
    b = ''
    for i in range(len(a)):
        kk = eval(key.get())
        t = a[i]    # 变量传递
        if 'a' <= t <= 'z':     # 当t是小写字母时，往后顺延kk
            if ord(t) <= ord('z')-kk:
                t = chr(ord(t)+kk)
            else:               # 当顺延kk时超出范围，回到开头
                t = chr(ord(t)+kk-26)
        if 'A' <= t <= 'Z':     # 当t是大写字母，同样的操作
            if ord(t) <= ord('Z')-kk:
                t = chr(ord(t)+kk)
            else:
                t = chr(ord(t)+kk-26)
        b += t
    text1.set(b)


w = Tk()
w.title('凯撒密码')
fra1 = my_frame(w)
key = StringVar()
key.set('')
Label(fra1, text='密匙（Key）').pack(side=LEFT)
Entry(fra1, textvariable=key).pack(side=RIGHT)
fra2 = my_frame(w)
text = StringVar()
text.set('')
Label(fra2, text='明文').pack(side=LEFT)
Entry(fra2, textvariable=text).pack(side=RIGHT)
text1 = StringVar()
w.bind('<Return>', change_code)
fra3 = my_frame(w)
Label(fra3, text='密文').pack(side=LEFT)
Entry(fra3, textvariable=text1).pack(side=RIGHT)
w.mainloop()