import tkinter as tk

def mainWindow():
    window=tk.Tk()
    window.title("Library Catalogue")
    window.geometry("1000x1000")
    frame=tk.Frame(window)
    frame.place(relx=0.2,rely=0.2,relheight=0.6,relwidth=0.6)
    bt=tk.Button(window,text='Borrow',command=borrowBookPage)
    bt.grid(column=0,row=0)
    bt1=tk.Button(window,text='Return',command=ReturnBookPage)
    bt1.grid(column=0,row=1)
    window.mainloop()
    
def borrowBookPage():
    label=tk.Label(frame,text='What book you want to borrow?')
    label.place(relx=0.3,rely=0.4)

def ReturnBookPage():
    label=tk.Label(frame,text='Return the book')
    label.place(relx=0.3,rely=0.4)

mainWindow()
