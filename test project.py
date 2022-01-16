from tkinter import *
from tkinter import messagebox
from tkinter import ttk #to use the comboboxafsd

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
    for i in range(1,100): print('-', end='')
    print()
    PrintUserTable()
    for i in range(1,100): print('-', end='')
    print()
    PrintBookTable()
    FontStyle = ("halvetica", 21)
    fgColor = "midnight blue"
    bgColor = "LightBlue1"

    frame = LabelFrame(window, text='WELCOME TO LIBRARY CATALOGUE !!!!\n', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor, font=FontStyle)
    frame.grid(padx=400, pady=250)
    greet = Label(frame, text="----MENU----------------------------------------------------------------------------\n",
                  bg=bgColor, fg=fgColor)
    greet.grid(column=0, row=0)
    # button
    bt = Button(frame, text='Search Book', fg=fgColor, bg=bgColor, width=50,
                command=lambda: ShowFrame(frame, SearchBookPage))
    bt.grid(column=0)
    bt = Button(frame, text='Borrow', fg=fgColor, bg=bgColor, width=50,
                command=lambda: ShowFrame(frame, BorrowBookPage))
    bt.grid(column=0)
    bt = Button(frame, text='Return', fg=fgColor, bg=bgColor, width=50,
                command=lambda: ShowFrame(frame, ReturnBookPage))
    bt.grid(column=0)
    bt = Button(frame, text='Register New User', fg=fgColor, bg=bgColor, width=50,
                command=lambda: ShowFrame(frame, RegisterUserPage))
    bt.grid(column=0)
    bt = Button(frame, text='Add New Book', fg=fgColor, bg=bgColor, width=50,
                command=lambda: ShowFrame(frame, EditBookPage))
    bt.grid(column=0)
    bt = Button(frame, text='Edit Book', fg=fgColor, bg=bgColor, width=50,
                command=lambda: ShowFrame(frame, EditBookPage))
    bt.grid(column=0)


def BorrowBookPage(ISBN=None, BookName=None):
    FontStyle = ("Arial Narrow", 21)
    fgColor = "midnight blue"
    bgColor = "LightBlue1"
    frame = LabelFrame(window, text='BORROW\n', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor, font=FontStyle)
    frame.grid(padx=400, pady=250)
    BookLabel = Label(frame, text='Book Name: ', fg=fgColor, bg=bgColor, font=FontStyle)
    ISBNLbl = Label(frame, text='Book ID: ', fg=fgColor, bg=bgColor, font=FontStyle)
    BackBtn = Button(frame, text='back', command=lambda: ShowFrame(frame, MainPage))
    ISBNEntry = Entry(frame, font=FontStyle)
    BookNameEntry = Entry(frame, font=FontStyle)
    BorrowerICEntry = Entry(frame,font=FontStyle)
    BorrowerICEntry.bind('<Return>', lambda *args: Borrow())
    def Borrow():
        msgbx = messagebox.askyesno(message="Confirm?")
        if msgbx == False:
            ShowFrame(frame, SearchBookPage)
        else:
            if(BorrowBook(ISBN=ISBNEntry.get(), IC=BorrowerICEntry)=='IC Error'):
                msgbx=messagebox.askyesnocancel(message="The IC is not recorded in the system. Enter yes proceed to register or cancel to correct")
                if msgbx is False:
                    ShowFrame(frame,MainPage)
                elif msgbx is True:
                    ShowFrame(frame, RegisterUserPage)

    BorrowBtn = Button(frame, text='borrow', command=lambda: Borrow())

    if ISBN != None:
        ISBNEntry.insert(0, ISBN)
    if BookName != None:
        BookNameEntry.insert(0, BookName)
    BookLabel.grid(column=0, row=0)
    ISBNLbl.grid(column=0, row=1)
    ISBNEntry.grid(row=0, column=1, padx=5, pady=5)
    BookNameEntry.grid(row=1, column=1, padx=5, pady=5)
    Label(frame, text="IC: ", font=FontStyle, fg=fgColor, bg=bgColor).grid(column=0, row=3)
    BorrowerICEntry.grid(column=1, row=3)
    BackBtn.grid(column=0, row=4)
    BorrowBtn.grid(column=1,row=4)

    if ISBN is None or BookName is None or ISBN == "None" or BookName == "None":
        ShowFrame(frame, SearchBookPage)
    elif IsBookAvailable(BookName, ISBN) == False:
        messagebox.showinfo(message="The Book is not available for borrowing")
        ShowFrame(frame, SearchBookPage)


def GetBookInfoFrame(parent, ISBNVar, BookNameVar, StatusVar):
    frame = LabelFrame(parent)
    Label(frame, text="ISBN :").grid(row=0)
    Label(frame, textvariable=ISBNVar).grid(row=0, column=1)
    Label(frame, text="Book Name :").grid(row=1)
    Label(frame, textvariable=BookNameVar).grid(row=1, column=1)
    Label(frame, text="Status :").grid(row=2)
    Label(frame, textvariable=StatusVar).grid(row=2, column=1)
    return frame

def SearchBookPage(Criteria='BookName'):
    frame = LabelFrame(window, text='main', height=720, width=480,
                       bd=15, relief='groove',
                       padx=5, pady=5)
    frame.grid()
    BookChoiceVar = StringVar(value=[])
    def SearchBtCmd(ISBN=None, BookName=None):
        BookRes = SearchBook(ISBN=ISBN, BookName=BookName)
        temp = []
        if type(BookRes) is list:
            for i in BookRes:
                temp.append(i['BookName'])
        elif type(BookRes) is dict:
            temp.append(BookRes['BookName'])
        BookChoiceVar.set(temp)
    SearchBt = Button(frame, text='Search')
    SearchEntry = Entry(frame)
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
    SearchLbl=Label(frame)
    ChgSearchBt = Button(frame, text='Change Search Criteria', bg="navajo white")
    if Criteria=='BookName':
        SearchLbl['text']="Enter the BookName: "
        SearchBt['command']=lambda *args: SearchBtCmd(BookName=SearchEntry.get())
        ChgSearchBt['command']=lambda: ShowFrame(frame, SearchBookPage('ISBN'))
        SearchEntry.bind('<KeyPress>', lambda *args: SearchBtCmd(BookName=SearchEntry.get()))
    else:
        SearchLbl['text']="Enter the ISBN: "
        SearchBt['command']=lambda *args: SearchBtCmd(ISBN=SearchEntry.get())
        ChgSearchBt['command'] = lambda: ShowFrame(frame, SearchBookPage('BookName'))
        SearchEntry.bind('<KeyPress>', lambda *args: SearchBtCmd(ISBN=SearchEntry.get()))
    SearchLbl.grid(row=0)
    SearchEntry.grid(row=0, column=1)
    BookLiBox.grid(row=1)
    if BookInfoFrame != None:
        BookInfoFrame.grid(row=1, column=1)
    SearchBt.grid(row=2, column=1)
    Button(frame, text='Back', bg="navajo white", command=lambda: ShowFrame(frame, MainPage)).grid(column=0, row=2)
    ChgSearchBt.grid(column=0, row=3)
    Button(frame, text='Borrow', bg="navajo white", command=lambda: ShowFrame(frame.destroy(), BorrowBookPage(ISBNVar.get(), BookNameVar.get()))).grid(column=1, row=3)
    instance = lambda: SearchBook(ISBN=ISBNVar.get(), ExactMatch=True)
    Button(frame, text='Edit', bg="navajo white",
           command=lambda: ShowFrame(frame.destroy(),EditBookPage(instance()))).grid(column=1, row=4)

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
    Button(frame, text='Back', bg="navajo white", command=lambda: ShowFrame(frame, MainPage)).grid(column=0, row=2)
    Entry(frame).grid(row=0, column=1, padx=50)
    Entry(frame).grid(row=1, column=1, padx=50)


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
    EmailLabel = Label(frame, text="Email :", fg=fgColor, bg=bgColor, font=FontStyle)
    NameEntry = Entry(frame, font=FontStyle)
    ICEntry = Entry(frame, font=FontStyle)
    EmailEntry = Entry(frame, font=FontStyle)
    NameLabel.grid(row=0, column=0)
    NameEntry.grid(row=0, column=1, padx=50)
    ICLabel.grid(row=1, column=0)
    ICEntry.grid(row=1, column=1, padx=50)
    EmailLabel.grid(row=2, column=0)
    EmailEntry.grid(row=2,column=1)

    def GetEntryInfo():
        AddUser(ICEntry.get(), NameEntry.get(), EmailEntry.get())
        ShowFrame(frame, MainPage)

    Button(frame, text='Register', bg="navajo white", width=10, command=GetEntryInfo).grid(row=3, column=1, padx=50)
    Button(frame, text='Back', bg="navajo white", width=10, command=lambda: ShowFrame(frame, MainPage)).grid(row=3,
                                                                                                             column=0,
                                                                                                             padx=50)

#if instance is None, then it is a adding new book page
def EditBookPage(instance=None):
    FontStyle = ("Arial Narrow", 21)
    fgColor = "midnight blue"
    bgColor = "LightBlue1"
    frame = LabelFrame(window, text='ADD NEW BOOK\n', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor, font=FontStyle)
    frame.grid(padx=400, pady=250)
    # initialise widgets
    BookNameLabel = Label(frame, text="Book Name :", fg=fgColor, bg=bgColor, font=FontStyle)
    ISBNLabel = Label(frame, text="ISBN:", fg=fgColor, bg=bgColor, font=FontStyle)
    BookNameEntry = Entry(frame, font=FontStyle)
    ISBNEntry = Entry(frame, font=FontStyle)
    StatusBox = ttk.Combobox(frame, values=('Normal', 'Restricted'))
    StatusBox.state(["readonly"])
    if instance is not None:
        StatusBox.set(instance['Status'])
        BookNameEntry.insert(0, instance['BookName'])
        ISBNEntry.insert(0, instance['ISBN'])
    # putting widgets
    BookNameLabel.grid(row=0, column=0, padx=50)
    BookNameEntry.grid(row=0, column=1, padx=50)
    ISBNLabel.grid(row=1, column=0)
    ISBNEntry.grid(row=1, column=1)
    StatusBox.grid(row=2)


    def GetEntryInfo():
        ISBN = ISBNEntry.get()
        BookName = BookNameEntry.get()
        Status = StatusBox.get()
        if len(ISBN) < 1 or len(BookName) < 1 or len(Status) < 1:
            return
        if instance is not None:
            UpdateBook(instance['ISBN'], dict(ISBN=ISBN, BookName=BookName, Status=Status))
        elif AddBook(ISBN=ISBN, Name=BookName, Status=Status) == False:
            messagebox.showinfo(message="The Book is already registered in the library")
        ShowFrame(frame, MainPage)

    Button(frame, text='Add', bg="navajo white", width=10, command=GetEntryInfo).grid()
    Button(frame, text='back', bg="navajo white", width=10, command=lambda: ShowFrame(frame, MainPage)).grid()

def AddNewBook():
    SearchBookPage()


if __name__ == '__main__':
    LibraryAppInit()
    MainPage()
    window.mainloop()
