import tkinter as tk
eq=''

def number(a):
    global eq
    eq+=a
    ans.set(eq)
    return

def clear():
    global eq
    eq=''
    ans.set(eq)
    
def solve():
    global eq
    try:
        ans.set(str(eval(eq)))
        eq=''
    except:
        ans.set("ERROR")
        eq=''
    return

wm=tk.Tk()
wm.title("Simple Arithmetic Calculator")
wm.configure(bg="white")
eq=''
ans=tk.StringVar()
l1=tk.Label(wm,textvariable=ans,bg="white",width=19,height=3,fg="darkblue",font=("calibria",30))
b1=tk.Button(wm,text='1',command=lambda:number('1'),font=("calibria",41),width=3,padx=3,pady=2,bg="lightpink",fg="darkblue")
b2=tk.Button(wm,text='2',command=lambda:number('2'),font=("calibria",41),width=3,padx=3,pady=2,bg="lightpink",fg="darkblue")
b3=tk.Button(wm,text='3',command=lambda:number('3'),font=("calibria",41),width=3,padx=3,pady=2,bg="lightpink",fg="darkblue")
b4=tk.Button(wm,text='4',command=lambda:number('4'),font=("calibria",41),width=3,padx=3,pady=2,bg="lightpink",fg="darkblue")
b5=tk.Button(wm,text='5',command=lambda:number('5'),font=("calibria",41),width=3,padx=3,pady=2,bg="lightpink",fg="darkblue")
b6=tk.Button(wm,text='6',command=lambda:number('6'),font=("calibria",41),width=3,padx=3,pady=2,bg="lightpink",fg="darkblue")
b7=tk.Button(wm,text='7',command=lambda:number('7'),font=("calibria",41),width=3,padx=3,pady=2,bg="lightpink",fg="darkblue")
b8=tk.Button(wm,text='8',command=lambda:number('8'),font=("calibria",41),width=3,padx=3,pady=2,bg="lightpink",fg="darkblue")
b9=tk.Button(wm,text='9',command=lambda:number('9'),font=("calibria",41),width=3,padx=3,pady=2,bg="lightpink",fg="darkblue")
b0=tk.Button(wm,text='0',command=lambda:number('0'),font=("calibria",41),width=3,padx=3,pady=2,bg="lightpink",fg="darkblue")
badd=tk.Button(wm,text='+',command=lambda:number('+'),font=("calibria",41),width=3,padx=3,pady=2,bg="skyblue",fg="darkblue")
bmin=tk.Button(wm,text='-',command=lambda:number('-'),font=("calibria",41),width=3,padx=3,pady=2,bg="skyblue",fg="darkblue")
bdiv=tk.Button(wm,text='/',command=lambda:number('/'),font=("calibria",41),width=3,padx=3,pady=2,bg="skyblue",fg="darkblue")
bmul=tk.Button(wm,text='*',command=lambda:number('*'),font=("calibria",41),width=3,padx=3,pady=2,bg="skyblue",fg="darkblue")
bdot=tk.Button(wm,text='.',command=lambda:number('.'),font=("calibria",41),width=3,padx=3,pady=2,bg="skyblue",fg="darkblue")
bequ=tk.Button(wm,text='=',command=solve,font=("calibria",41),width=3,padx=3,pady=2,bg="skyblue",fg="red")
bclear=tk.Button(wm,text='CLEAR',command=clear,bg="skyblue",fg="blue",font=("calibria",20,"bold"))

l1.grid(row=0,columnspan=4)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
bdiv.grid(row=1,column=3)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
bmul.grid(row=2,column=3)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
bmin.grid(row=3,column=3)
b0.grid(row=4,column=0)
badd.grid(row=4,column=1)
bdot.grid(row=4,column=2)
bequ.grid(row=4,column=3)
bclear.grid(row=5,columnspan=4)

wm.mainloop()