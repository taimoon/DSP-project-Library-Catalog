print("Hello world by hafiz")

print("test github")

import tkinter as tk
from tkinter import*
window=tk.Tk()
window.title("Library Catalogue")

# my_menu=Menu()
# window.config(menu=my_menu)
#
# filemenu=Menu(my_menu)
# my_menu.add_cascade(label="Select",menu=filemenu)
# filemenu.add_command(label="Borrow")
# filemenu.add_command(label="Return")
# filemenu.add_separator()
# filemenu.add_command(label="Exit")

window.geometry("1000x1000")

frame=tk.Frame(window)
frame.place(relx=0.2,rely=0.2,relheight=0.6,relwidth=0.6)

def page1():
    label=tk.Label(frame,text='What book you want to borrow?')
    label.place(relx=0.3,rely=0.4)

def page2():
    label=tk.Label(frame,text='Return the book')
    label.place(relx=0.3,rely=0.4)



bt=tk.Button(window,text='Borrow',command=page1)
bt.grid(column=0,row=0)

bt1=tk.Button(window,text='Return',command=page2)
bt1.grid(row=0,column=1)



window.mainloop()






