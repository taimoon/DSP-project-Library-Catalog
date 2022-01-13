print("Hello world by hafiz")

print("test github")

import tkinter as tk
from tkinter import*
window=tk.Tk()
window.title("Library Catalogue")

frame=tk.Frame(window)
frame.place(relx=0.2,rely=0.2,relheight=0.6,relwidth=0.6)

def page1():
    label=tk.Label(frame,text='What book you want to borrow?')
    label.place(relx=0.3,rely=0.4)


def page2():
    label2=tk.Label(frame,text="Return the book")
    label2.place(relx=0.3,rely=0.4)



bt=tk.Button(window,text='Borrow',command=page1)
bt.grid(column=0,row=0)



bt1=tk.Button(window,text='Return',command=page2)
bt1.grid(row=0,column=1)



window.geometry("1000x1000")


window.mainloop()