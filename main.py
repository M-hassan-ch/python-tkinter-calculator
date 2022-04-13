from tkinter import *
# import tkinter.messagebox as tb

root=Tk()
root.geometry("450x500")
root.resizable(False, False)
root.title("Calculator by Hassan")
root.configure(bg="black")
root.wm_iconbitmap("1.ICO")

#!--- Functions

def cal(event):
    val=event.widget.cget("text")
    if val=="=":
        try:
            screenVal.set(eval(screenVal.get()))
            screen.update()
        except:
            screenVal.set("Invalid input")
            screen.update()
            import time
            time.sleep(1)
            screenVal.set("")
            screen.update()
        pass
    elif val=="C":
        screenVal.set("")
        screen.update()
        pass
    elif val=="x":
        screenVal.set(screenVal.get() + "*")
        screen.update()
        pass
    elif val=="÷":
        screenVal.set(screenVal.get() + "/")
        screen.update()
        pass
    else:
        screenVal.set(screenVal.get()+val)
        screen.update()
        pass
    pass

#!--- input screen

screenVal=StringVar()
screen=Entry(root,font="Centaur 26 bold",relief=SUNKEN,textvariable=screenVal,justify=RIGHT,bg="grey")
screen.pack(ipady=25,fill=BOTH,padx=10,pady=8)

#!--- Numbers of calculator

num1=Frame(root,bg="black")
b=Button(num1,font="calibri 26 normal",text="7",bg="grey")
b.bind("<Button-1>",cal)
b.pack(ipadx=15,ipady=5,padx=3,pady=3)
b=Button(num1,font="calibri 26 normal",text="4",bg="grey")
b.bind("<Button-1>",cal)
b.pack(ipadx=15,ipady=5,padx=3,pady=3)
b=Button(num1,font="calibri 26 normal",text="1",bg="grey")
b.bind("<Button-1>",cal)
b.pack(ipadx=15,ipady=5,padx=3,pady=3)
b=Button(num1,font="calibri 26 normal",text=".",bg="grey")
b.bind("<Button-1>",cal)
b.pack(ipadx=19,ipady=5,padx=3,pady=3)
num1.pack(side=LEFT,padx=10,pady=8)


num1=Frame(root,bg="black")
b=Button(num1,font="calibri 26 normal",text="8",bg="grey")
b.bind("<Button-1>",cal)
b.pack(ipadx=15,ipady=5,padx=3,pady=3)
b=Button(num1,font="calibri 26 normal",text="5",bg="grey")
b.bind("<Button-1>",cal)
b.pack(ipadx=15,ipady=5,padx=3,pady=3)
b=Button(num1,font="calibri 26 normal",text="2",bg="grey")
b.bind("<Button-1>",cal)
b.pack(ipadx=15,ipady=5,padx=3,pady=3)
b=Button(num1,font="calibri 26 normal",text="0",bg="grey")
b.bind("<Button-1>",cal)
b.pack(ipadx=15,ipady=5,padx=3,pady=3)
num1.pack(side=LEFT,padx=0,pady=8)

num1=Frame(root,bg="black")
b=Button(num1,font="calibri 26 normal",text="9",bg="grey")
b.bind("<Button-1>",cal)
b.pack(ipadx=15,ipady=5,padx=3,pady=3)
b=Button(num1,font="calibri 26 normal",text="6",bg="grey")
b.bind("<Button-1>",cal)
b.pack(ipadx=15,ipady=5,padx=3,pady=3)
b=Button(num1,font="calibri 26 normal",text="3",bg="grey")
b.bind("<Button-1>",cal)
b.pack(ipadx=15,ipady=5,padx=3,pady=3)
b=Button(num1,font="calibri 26 normal",text="%",bg="grey")
b.bind("<Button-1>",cal)
b.pack(ipadx=12,ipady=5,padx=3,pady=3)
num1.pack(side=LEFT,padx=10,pady=8)

num1=Frame(root,bg="black")
b=Button(num1,font="calibri 26 normal",text="+",bg="grey")
b.bind("<Button-1>",cal)
b.pack(ipadx=15,ipady=5,padx=3,pady=3)
b=Button(num1,font="calibri 26 normal",text="-",bg="grey")
b.bind("<Button-1>",cal)
b.pack(ipadx=18,ipady=5,padx=3,pady=3)
b=Button(num1,font="calibri 26 normal",text="x",bg="grey")
b.bind("<Button-1>",cal)
b.pack(ipadx=16,ipady=5,padx=3,pady=3)
b=Button(num1,font="calibri 26 normal",text="÷",bg="grey")
b.bind("<Button-1>",cal)
b.pack(ipadx=15,ipady=5,padx=3,pady=3)
num1.pack(side=LEFT,padx=0,pady=8)

num1=Frame(root,bg="black")
b=Button(num1,font="calibri 26 normal",text="C",bg="grey")
b.bind("<Button-1>",cal)
b.pack(ipadx=15,ipady=5,padx=3,pady=3)
b=Button(num1,font="calibri 26 normal",text="E",command=quit,bg="grey").pack(ipadx=15,ipady=5,padx=3,pady=3)
b=Button(num1,font="calibri 26 normal",text="=",bg="grey")
b.bind("<Button-1>",cal)
b.pack(ipadx=15,ipady=50,padx=3,pady=3)
num1.pack(side=LEFT,padx=0,pady=8)


root.mainloop()