from tkinter import *
window=Tk()
window.title("Library Catalogue")
window.geometry(f"{720}x{480}")

def ShowFrame(currPage, newPage):
    if currPage is not None:
        currPage.destroy()
    if callable(newPage):
        newPage()
def mainPage():
    frame = LabelFrame(window, text='main', height=720, width=480,
                       bd=3, relief='groove',
                       padx=5, pady=5)
    frame.grid()
    bt = Button(frame, text='Borrow', command=lambda: ShowFrame(frame, borrowBookPage))
    bt.grid(column=0, row=0)
    bt = Button(frame, text='Return', command=lambda: ShowFrame(frame, returnBookPage))
    bt.grid(row=1, column=0)
def borrowBookPage():
    frame = LabelFrame(window, text='borrow', height=720, width=480,
                       bd=3, relief='groove',
                       padx=5, pady=5)
    frame.grid()
    label=Label(frame,text='What book you want to borrow?')
    label.grid(column=0,row=0)
    Button(frame, text='back', command=lambda: ShowFrame(frame, mainPage)).grid(column=0,row=1)
def returnBookPage():
    frame = LabelFrame(window, text='return', height=720, width=480,
                       bd=3, relief='groove',
                       padx=5, pady=5)
    frame.grid()
    label=Label(frame,text='Return the book')
    label.grid(column=0,row=0)
    Button(frame, text='back', command=lambda: ShowFrame(frame, mainPage)).grid(column=0, row=1)
if __name__ == '__main__':
    mainPage()
    window.mainloop()







