from tkinter import *
from tkinter import messagebox

from Library_App_Engine import *

window = Tk()
window.title("Library Catalogue")
window.geometry(f"{1000}x{1000}")
window.config(bg='#afeeee')


def ShowFrame(CurrPage, NewPage):
    if CurrPage is not None:
        CurrPage.destroy()
    if callable(NewPage):
        NewPage()


def MainPage():
    FontStyle = ("halvetica", 21)
    fgColor = "midnight blue"
    bgColor = "LightBlue1"

    frame = LabelFrame(window, text='WELCOME TO LIBRARY CATALOGUE !!!!\n', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor, font=FontStyle)
    frame.grid(padx=400, pady=250)
    greet = Label(frame, text="----MENU---------------------------------------------------------------------------------------------------------\n",
                  bg=bgColor, fg=fgColor)
    greet.grid(column=0, row=0)
    # button
    bt = Button(frame, text='Search Book', fg=fgColor, bg="#24d1bc", width=50,
                command=lambda: ShowFrame(frame, SearhBookPage))
    bt.grid(column=0)
    bt = Button(frame, text='Borrow', fg=fgColor, bg="#24d1bc", width=50,
                command=lambda: ShowFrame(frame, BorrowBookPage))
    bt.grid(column=0)
    bt = Button(frame, text='Return', fg=fgColor, bg="#24d1bc", width=50,
                command=lambda: ShowFrame(frame, ReturnBookPage))
    bt.grid(column=0)
    bt = Button(frame, text='Register New User', fg=fgColor, bg="#24d1bc", width=50,
                command=lambda: ShowFrame(frame, RegisterUserPage))
    bt.grid(column=0)
    bt = Button(frame, text='Add New Book', fg=fgColor, bg="#24d1bc", width=50,
                command=lambda: ShowFrame(frame, AddNewBook))
    bt.grid(column=0)


def BorrowBookPage():
    FontStyle = ("Arial Narrow", 21)
    fgColor = "midnight blue"
    bgColor = "LightBlue1"
    frame = LabelFrame(window, text='BORROW\n', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor, font=FontStyle)
    frame.grid(padx=400, pady=250)
    BookLabel = Label(frame, text='Book Name: ', fg=fgColor, bg=bgColor, font=FontStyle)
    IdLabel = Label(frame, text='Book ID: ', fg=fgColor, bg=bgColor, font=FontStyle)
    BackBtn = Button(frame, text='Back',bg="#24d1bc", command=lambda: ShowFrame(frame, MainPage))
    BookLabel.grid(column=0, row=0)
    IdLabel.grid(column=0, row=1)
    BackBtn.grid(column=0, row=2)
    Entry(frame, font=FontStyle).grid(row=0, column=1, padx=5, pady=5)
    Entry(frame, font=FontStyle).grid(row=1, column=1, padx=5, pady=5)


def GetBookInfoFrame(parent, ISBNVar, BookNameVar, StatusVar):
    frame = LabelFrame(parent)
    Label(frame, text="ISBN :").grid(row=0)
    Label(frame, textvariable=ISBNVar).grid(row=0, column=1)
    Label(frame, text="Book Name :").grid(row=1)
    Label(frame, textvariable=BookNameVar).grid(row=1, column=1)
    Label(frame, text="Status :").grid(row=2)
    Label(frame, textvariable=StatusVar).grid(row=2, column=1)
    return frame


def SearhBookPage():
    FontStyle = ("Arial Narrow", 21)
    fgColor = "midnight blue"
    bgColor = "LightBlue1"

    frame = LabelFrame(window, text='SEARCH BOOK\n', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor, font=FontStyle)
    frame.grid(padx=400, pady=250)
    BookChoiceVar = StringVar(value=[])

    def SearchBtCmd(*args):
        BookRes = SearchBook(BookName=BookNameEntry.get())
        temp = []
        if type(BookRes) is list:
            
            for i in BookRes:
                temp.append(i['BookName'])
        elif type(BookRes) is dict:
            temp.append(BookRes['BookName'])
        BookChoiceVar.set(temp)

    SearchBt = Button(frame, text='Search',bg="#24d1bc", command=SearchBtCmd)
    BookNameEntry = Entry(frame)
    BookNameEntry.bind('<KeyPress>', SearchBtCmd)
    # Book Info frame
    ISBNVar = StringVar(value="None")
    BookNameVar = StringVar(value="None")
    StatusVar = StringVar(value="None")
    BookInfoFrame = GetBookInfoFrame(frame, ISBNVar, BookNameVar, StatusVar)
    BookLiBox = Listbox(frame, height=5, listvariable=BookChoiceVar)
    def BookLiBoxSel(*args):
        idxs = BookLiBox.curselection()
        if len(idxs) < 1:
            return
        idxs = idxs[0]
        instance = SearchBook(BookName=BookLiBox.get(idxs), ExactMatch=True)
        ISBNVar.set(instance['ISBN'])
        BookNameVar.set(instance['BookName'])
        StatusVar.set(GetBookStatus(ISBN=instance['ISBN']))

    BookLiBox.bind('<<ListboxSelect>>', BookLiBoxSel)
    Label(frame, text="Enter the Book Name: ", fg=fgColor, bg=bgColor, font=FontStyle).grid(row=0)
    BookNameEntry.grid(row=0, column=1, padx=5, pady=5)
    BookLiBox.grid(row=1)
    if BookInfoFrame != None:
        BookInfoFrame.grid(row=1, column=1)
    SearchBt.grid(row=2, column=1)
    Button(frame, text='Back', bg="#24d1bc", command=lambda: ShowFrame(frame, MainPage)).grid(column=0, row=2)


def ReturnBookPage():
    FontStyle = ("Arial Narrow", 21)
    fgColor = "midnight blue"
    bgColor = "LightBlue1"

    frame = LabelFrame(window, text='RETURN\n', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor, font=FontStyle)
    frame.grid(padx=400, pady=250)

    ReturnNamelabel = Label(frame, text='Book Name: ', fg=fgColor, bg=bgColor, font=FontStyle)
    ReturnNamelabel.grid(column=0, row=0)
    ReturnIdLabel = Label(frame, text='Book ID: ', fg=fgColor, bg=bgColor, font=FontStyle)
    ReturnIdLabel.grid(column=0, row=1)
    Button(frame, text='Back', bg="#24d1bc", command=lambda: ShowFrame(frame, MainPage)).grid(column=0, row=2)
    Entry(frame,font=FontStyle).grid(row=0, column=1, padx=5, pady=5)
    Entry(frame,font=FontStyle).grid(row=1, column=1, padx=5, pady=5)


def RegisterUserPage():
    FontStyle = ("Arial Narrow", 24)
    fgColor = "midnight blue"
    bgColor = "LightBlue1"
    frame = LabelFrame(window, text='REGISTRATION', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor, font=FontStyle)
    frame.grid(padx=400, pady=250)

    NameLabel = Label(frame, text="Name :", fg=fgColor, bg=bgColor, font=FontStyle)
    ICLabel = Label(frame, text="IC No. :", fg=fgColor, bg=bgColor, font=FontStyle)
    NameEntry = Entry(frame, font=FontStyle)
    ICEntry = Entry(frame, font=FontStyle)
    NameLabel.grid(row=0, column=0);
    NameEntry.grid(row=0, column=1, padx=50)
    ICLabel.grid(row=1, column=0);
    ICEntry.grid(row=1, column=1, padx=50)

    def GetEntryInfo():
        AddUser(ICEntry.get(), NameEntry.get())
        ShowFrame(frame, MainPage)

    Button(frame, text='Register', bg="#24d1bc", width=10, command=GetEntryInfo).grid(row=2, column=1, padx=50)
    Button(frame, text='Back', bg="#24d1bc", width=10, command=lambda: ShowFrame(frame, MainPage)).grid(row=2,
                                                                                                             column=0,
                                                                                                             padx=50)


def AddNewBook():
    FontStyle = ("Arial Narrow", 21)
    fgColor = "midnight blue"
    bgColor = "LightBlue1"
    frame = LabelFrame(window, text='ADD NEW BOOK\n', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor, font=FontStyle)
    frame.grid(padx=400, pady=250)
    # initialise widgets
    BookNameLabel = Label(frame, text="Book Name :", fg=fgColor, bg=bgColor, font=FontStyle)
    ISBNLabel = Label(frame, text="ISBN :", fg=fgColor, bg=bgColor, font=FontStyle)
    BookNameEntry = Entry(frame, font=FontStyle)
    ISBNEntry = Entry(frame, font=FontStyle)
    # putting widgets
    BookNameLabel.grid(row=0, column=0, padx=50)
    BookNameEntry.grid(row=0, column=1, padx=50)
    ISBNLabel.grid(row=1, column=0)
    ISBNEntry.grid(row=1, column=1)

    def GetEntryInfo():
        if AddBook(ISBNEntry.get(), BookNameEntry.get()) == False:
            messagebox.showinfo(message="The Book is already registered in the library")
        ShowFrame(frame, MainPage)

    Button(frame, text='Add', bg="#24d1bc", width=10, command=GetEntryInfo).grid()
    Button(frame, text='Back', bg="#24d1bc", width=10, command=lambda: ShowFrame(frame, MainPage)).grid()


if __name__ == '__main__':
    LibraryAppInit()
    PrintUserTable()
    PrintBookTable()
    MainPage()
    window.mainloop()