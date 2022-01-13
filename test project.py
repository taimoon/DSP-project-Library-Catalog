print("Hello world by hafiz")

print("test github")

import tkinter as tk
from tkinter import*
window=tk.Tk()
window.title("Library Catalogue")
window.geometry("1000x1000")

frame=tk.Frame(window)
frame.place(relx=0.2,rely=0.2,relheight=0.6,relwidth=0.6)

#input


def page1():
    label=tk.Label(frame,text='What book you want to borrow?')
    label.place(relx=0.3,rely=0.4)

def page2():
    label2=tk.Label(frame,text='Return the book')
    label2.place(relx=0.4,rely=0.5)

L1 = Label(window, text = "Name : ")
L1.place(x = 10,y = 10, width ='50')
E1 = Entry(window, bd = 3, width ='50')
E1.place( x = 60,y = 10)

L2 = Label(window,text = "Book ID :  ")
L2.place(x = 10,y = 50, width = '50')
E2 = Entry(window,bd = 3, width ='50')
E2.place(x = 60,y = 50)

B1 = Button(window, text = "Borrow", command=page1)
B1.place(x = 225, y = 100, width = '50', anchor ="c")


B2 = Button(window, text = "Return", command=page2)
B2.place(x = 225, y = 130, width = '50', anchor ="c")
window.geometry("250x250+10+10")


# def page1():
#     label=tk.Label(frame,text='What book you want to borrow?')
#     label.place(relx=0.3,rely=0.4)
#
# def page2():
#     label=tk.Label(frame,text='Return the book')
#     label.place(relx=0.3,rely=0.4)
#
#
#
# bt=tk.Button(window,text='Borrow',command=page1)
# bt.grid(column=0,row=0)
#
# bt1=tk.Button(window,text='Return',command=page2)
# bt1.grid(row=0,column=1)
#


window.mainloop()






