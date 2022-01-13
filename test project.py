from tkinter import *
from Library_App_Engine import *
from tkinter import messagebox

window=Tk()
window.title("Library Catalogue")
window.geometry(f"{720}x{480}")
def ShowFrame(CurrPage, NewPage):
    if CurrPage is not None:
        CurrPage.destroy()
    if callable(NewPage):
        NewPage()
def MainPage():
    frame = LabelFrame(window, text='main', height=720, width=480,
                       bd=3, relief='groove',
                       padx=5, pady=5)
    frame.grid()
    bt = Button(frame, text='Borrow', command=lambda: ShowFrame(frame, BorrowBookPage))
    bt.grid(column=0, row=0)
    bt = Button(frame, text='Return', command=lambda: ShowFrame(frame, ReturnBookPage))
    bt.grid(column=0, row=1)
    bt = Button(frame, text='Register New User', command=lambda: ShowFrame(frame, RegisterUserPage))
    bt.grid(column=0, row=2)
    bt = Button(frame, text='Add New Book', command=lambda: ShowFrame(frame, AddNewBookPage))
    bt.grid(column=0)
def BorrowBookPage():
    frame = LabelFrame(window, text='borrow', height=720, width=480,
                       bd=3, relief='groove',
                       padx=5, pady=5)
    frame.grid()
    label=Label(frame,text='What book you want to borrow?')
    label.grid(column=0,row=0)
    Button(frame, text='back', command=lambda: ShowFrame(frame, MainPage)).grid(column=0,row=1)
def ReturnBookPage():
    frame = LabelFrame(window, text='return', height=720, width=480,
                       bd=3, relief='groove',
                       padx=5, pady=5)
    frame.grid()
    label=Label(frame,text='Return the book')
    label.grid(column=0,row=0)
    Button(frame, text='back', command=lambda: ShowFrame(frame, MainPage)).grid(column=0, row=1)
def RegisterUserPage():
    FontStyle = ("Arial Narrow", 24)
    frame = LabelFrame(window, text='Registration', height=720, width=480,
                       bd=3, relief='groove',
                       padx=5, pady=5)
    frame.grid()
    NameLabel = Label(frame, text="Name :", font=FontStyle)
    ICLabel = Label(frame, text="IC :", font=FontStyle)
    NameEntry = Entry(frame, font=FontStyle)
    ICEntry = Entry(frame,font=FontStyle)
    NameLabel.grid(row=0,column=0);NameEntry.grid(row=0,column=1)
    ICLabel.grid(row=1, column=0);ICEntry.grid(row=1,column=1)
    def GetEntryInfo():
        AddUser(ICEntry.get(), NameEntry.get())
        ShowFrame(frame, MainPage)
    Button(frame, text='Register', command=GetEntryInfo).grid()
    Button(frame, text='back', command=lambda: ShowFrame(frame, MainPage)).grid()
def AddNewBookPage():
    FontStyle = ("Arial Narrow", 24)
    frame = LabelFrame(window, text='Registration', height=720, width=480,
                       bd=3, relief='groove',
                       padx=5, pady=5)
    frame.grid()
    #initialise widgets
    BookNameLabel = Label(frame, text="Book Name :", font=FontStyle)
    ISBNLabel = Label(frame, text="ISBN :", font=FontStyle)
    BookNameEntry = Entry(frame, font=FontStyle)
    ISBNEntry = Entry(frame, font=FontStyle)
    #putting widgets
    BookNameLabel.grid(row=0, column=0)
    BookNameEntry.grid(row=0, column=1)
    ISBNLabel.grid(row=1, column=0)
    ISBNEntry.grid(row=1, column=1)
    def GetEntryInfo():
        if AddBook(ISBNEntry.get(), BookNameEntry.get()) == False:
            messagebox.showinfo(message="The Book is already registered in the library")
        ShowFrame(frame, MainPage)
    Button(frame, text='Add', command=GetEntryInfo).grid()
    Button(frame, text='back', command=lambda: ShowFrame(frame, MainPage)).grid()
if __name__ == '__main__':
    MainPage()
    window.mainloop()