from tkinter import *
from Library_App_Engine import *
from tkinter import messagebox


window=Tk()
window.title("Library Catalogue")
window.minsize(width=400,height=400)
window.geometry(f"{600}x{500}")


def ShowFrame(CurrPage, NewPage):
    if CurrPage is not None:
        CurrPage.destroy()
    if callable(NewPage):
        NewPage()
def MainPage():
    frame = Frame(window, bg="#FFBB00", bd=5)
    frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    FrameLabel = Label(frame, text="Welcome to \n Library Catalogue", bg='black', fg='white',
                         font=('Courier', 15))
    FrameLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    bt = Button(frame, text='Borrow',bg='black', fg='white',command=lambda: ShowFrame(frame, BorrowBookPage))
    bt.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.5)
    bt = Button(frame, text='Return',bg='black', fg='white', command=lambda: ShowFrame(frame, ReturnBookPage))
    bt.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.5)
    bt = Button(frame, text='Register New User', bg='black', fg='white',command=lambda: ShowFrame(frame, RegisterUserPage))
    bt.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.5)
    bt = Button(frame, text='Add New Book', bg='black', fg='white', command=lambda: ShowFrame(frame, AddNewBook))
    bt.place(relx=0.28,rely=1.0, relwidth=0.45,relheight=0.1)
def BorrowBookPage():
    frame = Frame(window, bg="#FFBB00", bd=5)
    frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    FrameLabel = Label(frame, text="Fill the details below ", bg='black', fg='white',
                       font=('Courier', 15))
    FrameLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    BookLabel=Label(frame,text='Book Name: ', bg='black', fg='white')
    BookLabel.place(relx=0.05,rely=0.2, relheight=0.08)
    IdLabel=Label(frame,text='Book ID: ', bg='black', fg='white')
    IdLabel.place(relx=0.05,rely=0.35, relheight=0.08)
    Button(frame, text='back',bg='#d1ccc0', fg='black', command=lambda: ShowFrame(frame, MainPage)).place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    Entry(frame).place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
    Entry(frame).place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
def ReturnBookPage():
    frame = Frame(window, bg="#FFBB00", bd=5)
    frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    FrameLabel = Label(frame, text="Fill the details below ", bg='black', fg='white',
                       font=('Courier', 15))
    FrameLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    ReturnNamelabel=Label(frame,text='Book Name: ', bg='black', fg='white')
    ReturnNamelabel.place(relx=0.05,rely=0.2, relheight=0.08)
    ReturnIdLabel = Label(frame, text='Book ID: ', bg='black', fg='white')
    ReturnIdLabel.place(relx=0.05,rely=0.35, relheight=0.08)
    Button(frame, text='back',bg='#d1ccc0', fg='black', command=lambda: ShowFrame(frame, MainPage)).place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    Entry(frame).place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)
    Entry(frame).place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)
def RegisterUserPage():
    FontStyle = ("Arial Narrow", 20)
    frame = Frame(window, bg="#FFBB00", bd=5)
    frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    FrameLabel = Label(frame, text="Fill the details below ", bg='black', fg='white',
                       font=('Courier', 15))
    FrameLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    NameLabel = Label(frame, text="Name :", bg='black', fg='white', font=FontStyle)
    ICLabel = Label(frame, text="IC No. :", bg='black', fg='white', font=FontStyle)
    NameEntry = Entry(frame, font=FontStyle)
    ICEntry = Entry(frame,font=FontStyle)
    NameLabel.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)
    ICLabel.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)
    def GetEntryInfo():
        AddUser(ICEntry.get(), NameEntry.get())
        ShowFrame(frame, MainPage)
    Button(frame, text='Register',bg='#d1ccc0', fg='black', command=GetEntryInfo).place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    Button(frame, text='Back', command=lambda: ShowFrame(frame, MainPage)).place(relx=0.28, rely=0.98, relwidth=0.18, relheight=0.08)
def AddNewBook():
    FontStyle = ("Arial Narrow", 24)
    frame = Frame(window, bg="#FFBB00", bd=5)
    frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    FrameLabel = Label(frame, text="Fill the details below ", bg='black', fg='white',
                       font=('Courier', 15))
    FrameLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    #initialise widgets
    BookNameLabel = Label(frame, text="Book Name :", bg='black', fg='white', font=FontStyle)
    ISBNLabel = Label(frame, text="International Standard Book Number (ISBN):", bg='black', fg='white', font=FontStyle)
    BookNameEntry = Entry(frame, font=FontStyle)
    ISBNEntry = Entry(frame, font=FontStyle)
    #putting widgets
    BookNameLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)#i dont know what is the range for this display
    BookNameEntry.place(relx=0, rely=0, relwidth=1, relheight=1)
    ISBNLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    ISBNEntry.place(relx=0, rely=0, relwidth=1, relheight=1)
    def GetEntryInfo():
        if AddBook(ISBNEntry.get(), BookNameEntry.get()) == False:
            messagebox.showinfo(message="The Book is already registered in the library")
        ShowFrame(frame, MainPage)
    Button(frame, text='Add', bg='#d1ccc0', fg='black', command=GetEntryInfo).place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    Button(frame, text='back', command=lambda: ShowFrame(frame, MainPage)).place(relx=0.28, rely=0.98, relwidth=0.18, relheight=0.08)
if __name__ == '__main__':
    MainPage()
    window.mainloop()
    print(GetBookStatus(ISBN='666666'))