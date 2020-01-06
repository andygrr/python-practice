from tkinter import *
global list_hobby;list_hobby = []
def add_hobby(hobby):
    global list_hobby
    if hobby.get() == 1:
        list_hobby.append(hobby)
w = Tk()
w.title('信息统计')
Label(w, text = '1.性别').pack(fill = X, side = TOP, expand = YES)
fra1 = Frame(w)
sexuality = StringVar()
sexuality.set('0')
Radiobutton(fra1, text = '男' ,variable = sexuality, value = '1' ).pack(side = LEFT, expand = YES)
Radiobutton(fra1, text = '女' ,variable = sexuality, value = '2' ).pack(side = LEFT, expand = YES)
fra1.pack(expand = YES,fill = X, side = TOP)
Label(w, text = '2.兴趣爱好').pack(fill = X, expand = YES)
fra2 = Frame(w)
hobby1 = StringVar();hobby2 = StringVar();hobby3 = StringVar()
hobby1.set('0');hobby2.set('0');hobby3.set('0');
Checkbutton(fra2, text = '游泳',  variable = hobby1, command = add_hobby(hobby1)).pack(side = LEFT, expand = YES)
Checkbutton(fra2, text = '乒乓球',  variable = hobby2, command = add_hobby(hobby2)).pack(side = LEFT, expand = YES)
Checkbutton(fra2, text = '唱歌',  variable = hobby3, command = add_hobby(hobby3)).pack(side = LEFT, expand = YES)
fra2.pack(expand = YES,fill = X, side = TOP)
w.mainloop()