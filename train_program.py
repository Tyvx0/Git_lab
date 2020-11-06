from tkinter import *
import random
from compute import compute
from achievement import achievement
import time

def main():
    a=random.randint(1,20)
    if a<5:
        b=random.randint(1,50)
        c=random.randint(1,50)
        C = compute(b,c)
        d = C.add()
        result="%d  +  %d" %(b,c)
        return (result,d)
    if a>=5 and a<10:
        b=random.randint(1,50)
        c=random.randint(b,100)
        C = compute(c,b)
        d = C.sub()
        result="%d  -  %d" %(c,b)
        return (result,d)
    if a>=10 and a<15:
        b=random.randint(1,20)
        c=random.randint(1,5)
        C = compute(c,b)
        d = C.mul()
        result="%d  *  %d" %(c,b)
        return(result,d)
    else:
        b=random.randint(1,9)
        c=random.randint(1,9)
        C = compute(c,b)
        d = C.mul()
        result="%d  /  %d" %(d,b)
        return(result,c)
        

def check():
    global rn, wn, t, time_start
    time_end=time.time()
    time_length.set(str(round(time_end-time_start,2))+"秒")
    if int(result.get())==int(t[1]):
        h="回答正确"
        rn = rn + 1
        hint.set(h)
        right_num.set(rn)
        A = achievement(rn,wn)
        accuracy.set(A.get_accuracy())
        t=main()
        e.set(t[0])
        result.set('')
    else:
        h="回答错误"
        wn = wn + 1
        hint.set(h)
        wrong_num.set(wn)
        if rn>0:
            A = achievement(rn,wn)
            accuracy.set(A.get_accuracy())
        t=main()
        e.set(t[0])
        result.set('')
    time_start=time.time() 

master = Tk()
master.geometry('350x250+100+100')
master.title("运算训练程序")
Label(master,text="题目").grid(row=0)
Label(master,text="答案").grid(row=1)
Label(master,text="信息").grid(row=4)
Label(master,text="正确数").grid(row=5)
Label(master,text="错误数").grid(row=6)
Label(master,text="正确率").grid(row=7)
Label(master,text="单题用时").grid(row=8)
e = StringVar()
result = StringVar()
hint = StringVar()
right_num = StringVar()
wrong_num = StringVar()
accuracy = StringVar()
time_length = StringVar()
e1 = Entry(master,textvariable=e)
e2 = Entry(master,textvariable=result)
e3 = Entry(master,textvariable=hint)
e4 = Entry(master,textvariable=right_num)
e5 = Entry(master,textvariable=wrong_num)
e6 = Entry(master,textvariable=accuracy)
e7 = Entry(master,textvariable=time_length)
t=main()
e.set(t[0])
rn = 0
wn = 0
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=4, column=1)
e4.grid(row=5, column=1)
e5.grid(row=6, column=1)
e6.grid(row=7, column=1)
e7.grid(row=8, column=1)
btn=Button(master,text = '确定',command = check)
btn.grid(row=2,column=2)
time_start=time.time() 
master.mainloop()