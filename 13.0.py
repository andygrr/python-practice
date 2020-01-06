from tkinter import *
from tkinter.ttk import *


# 将框架（Frame ）的共同属性作为默认值，以简化创建过程
def my_frame(master):
    w = Frame(master)
    w.pack(side=TOP, expand=YES, fill=BOTH)
    return w


# 将按钮（Button ）的共同属性作为默认值，以简化创建过程
def my_button(master, text, command):
    w = Button(master, text=text, command=command, width=6)
    w.pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2)
    return w


# 将数字串最末的字符删除并返回
def back(text):
    if len(text) > 0:
        return text[:-1]
    else:
        return text


# 利用eval 函数计算表达式字符串的值
def calc(text):
    global sep_flag
    try:
        if sep_flag.get() == 0:
            return eval(del_sep(text))
        else:
            return add_sep(str(eval(del_sep(text))))
    except (SyntaxError, ZeroDivisionError, NameError):
        return 'Error'


# 向参数传入的数字串中添加千位分隔符，分三种情况：纯小数 部份、
# 纯整数部份、同时有整数和小数部份。由于字符串是不可改变的，所以
# 先由字符串生成列表，以便执行insert 操作和extend 操作，操作完成后
# 再由列表生成字符串 返回
def add_sep(text):
    dot_index = text.find('.')
    if dot_index > 0:
        text_head = text[:dot_index]
        text_tail = text[dot_index:]
    elif dot_index < 0:
        text_head = text
        text_tail = ''
    else:
        text_head = ''
        text_tail = text
    list_ = [char for char in text_head]
    length = len(list_)
    tmp_index = 3
    while length - tmp_index > 0:
        list_.insert(length - tmp_index, ',')
        tmp_index += 3
    list_.extend(text_tail)
    new_text = ''
    for char in list_:
        new_text += char
    return new_text


# 删除数字串中所有的千位分隔符
def del_sep(text):
    return text.replace(',', '')


# 开始计算器界面的实现
def main():
    global sep_flag
    wind = Tk()
    wind.title(" 简易计算器")  # 设置主窗口标题
    main_menu = Menu(wind)  # 创建最上层主菜单
    # 创建“计算”菜单项，并加入到主菜单
    calc_menu = Menu(main_menu, tearoff=0)
    calc_menu.add_command(label=' 退出', command=lambda: exit())
    main_menu.add_cascade(label=' 计算', menu=calc_menu)
    # 创建“视图”菜单，并加入到主菜单，其中“显示千位分隔符”菜单项
    # 是一个Checkbutton
    text = StringVar()
    sep_flag = IntVar()
    sep_flag.set(0)
    view_menu = Menu(main_menu, tearoff=0)
    view_menu.add_checkbutton(label=' 显示千位分隔符', variable=sep_flag, command=lambda t=text: t.set(add_sep(t.get())))
    main_menu.add_cascade(label=' 视图', menu=view_menu)
    wind['menu'] = main_menu
    # 将主菜单与主窗口wind 绑定
    # 创建文本框
    Entry(wind, textvariable=text).pack(expand=YES, fill=BOTH, padx=2, pady=4)
    # 创建ttk 子模块的Style 对象，设置按钮内边距
    style = Style()
    style.configure('TButton', padding=3)
    # 创建第一行三个 按钮
    fedit = my_frame(wind)
    my_button(fedit, 'Backspace', lambda t=text: t.set(back(t.get())))
    my_button(fedit, 'Clear', lambda t=text: t.set(''))
    my_button(fedit, ' ±', lambda t=text: t.set('-(' + t.get() + ')'))
    # 创建其余四行按钮，每行四个
    for key in ('789/', '456*', '123-', '0.=+'):
        fsymb = my_frame(wind)
        for char in key:
            if char == '=':
                my_button(fsymb, char, lambda t=text: t.set(calc(t.get())))
            else:
                my_button(fsymb, char, lambda t=text, c=char: t.set(t.get() + c))
    wind.mainloop()


main()
