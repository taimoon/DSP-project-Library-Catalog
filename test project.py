from tkinter import *
from Library_App_Engine import *
from tkinter import messagebox


window=Tk()
window.title("Library Catalogue")
<<<<<<< HEAD
window.geometry(f"{720}x{480}")
window.resizable()
=======
window.geometry(f"{1000}x{1000}")
window.config(bg='#afeeee')

>>>>>>> parent of fcc6258 (Revert "Merge pull request #10 from hafizsem/main")

def ShowFrame(CurrPage, NewPage):
    if CurrPage is not None:
        CurrPage.destroy()
    if callable(NewPage):
        NewPage()
def MainPage():
    FontStyle = ("halvetica", 21)
    fgColor="midnight blue"
    bgColor="LightBlue1"

    frame = LabelFrame(window, text='WELCOME TO LIBRARY CATALOGUE !!!!\n', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg= bgColor,fg=fgColor, font=FontStyle)
    frame.grid(padx=400, pady=250)
    greet=Label(frame, text="----MENU----------------------------------------------------------------------------\n",bg= bgColor,fg=fgColor )
    greet.grid(column=0, row=0)
    #button
    bt = Button(frame, text='Borrow',fg=fgColor,bg=bgColor,width=50,command=lambda: ShowFrame(frame, BorrowBookPage))
    bt.grid(column=0, row=1)
    bt = Button(frame, text='Return',fg=fgColor,bg=bgColor,width=50, command=lambda: ShowFrame(frame, ReturnBookPage))
    bt.grid(column=0, row=2)
    bt = Button(frame, text='Register New User',fg=fgColor,bg=bgColor,width=50, command=lambda: ShowFrame(frame, RegisterUserPage))
    bt.grid(column=0, row=3)
    bt = Button(frame, text='Add New Book', fg=fgColor,bg=bgColor,width=50,command=lambda: ShowFrame(frame, AddNewBook))
    bt.grid(column=0)
    bt = Button(frame, text='Search Book', fg=fgColor, bg=bgColor, command=lambda: ShowFrame(frame, SearhBookPage))
    bt.grid(column=0)
def BorrowBookPage():
    FontStyle = ("Arial Narrow", 21)
    fgColor = "midnight blue"
    bgColor = "LightBlue1"

    frame = LabelFrame(window, text='BORROW\n', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor,font=FontStyle)
    frame.grid(padx=400, pady=250)

    BookLabel=Label(frame,text='Book Name: ',fg=fgColor,bg=bgColor,font=FontStyle)
    BookLabel.grid(column=0,row=0)
    IdLabel=Label(frame,text='Book ID: ',fg=fgColor,bg=bgColor,font=FontStyle)
    IdLabel.grid(column=0,row=1)
<<<<<<< HEAD
    Button(frame, text='back', command=lambda: ShowFrame(frame, MainPage)).grid(column=0,row=4)
    Entry(frame).grid(row= 0, column=1)
    Entry(frame).grid(row=1, column=1)
def GetBookInfoFrame(parent, instance):
    frame = LabelFrame(parent)
    Label(frame, text=f"ISBN :{instance['ISBN']}").grid(row=0)
    Label(frame, text=f"Book Name:{instance['BookName']}").grid(row=1)
    return frame
def SearhBookPage(BookInsta):
    frame = LabelFrame(window, text='main', height=720, width=480,
                       bd=15, relief='groove',
                       padx=5, pady=5)
    frame.grid()
    ISBNEntry = Entry(frame)
    choicevar = StringVar(value=[])
    def SearchBtCmd():
        BookRes = SearchBook(ISBN=ISBNEntry.get())
        temp = []
        for i in BookRes:
            temp.append(i['BookName'])
        choicevar.set(temp)
    SearchBt = Button(frame, text='Search', command=SearchBtCmd)
    BookLiBox = Listbox(frame, height=5, listvariable=choicevar)
    def BookLiBoxSel(BookInfoFrame=None):
        idxs = BookLiBox.curselection()[0]
        instance = SearchBook(BookName=BookLiBox.get(idxs), ExactMatch=True)
        if BookInfoFrame != None:
            BookInfoFrame.destroy()
        BookInfoFrame = GetBookInfoFrame(frame, instance)
        ShowFrame(frame, lambda : SearhBookPage(BookInfoFrame))
    BookLiBox.bind('<<ListboxSelect>>', lambda *args: BookLiBoxSel(BookInfoFrame))

    Label(frame, text="Enter the ISBN: ").grid(row=0)
    ISBNEntry.grid(row=0, column=1)
    BookLiBox.grid(row=1)
    SearchBt.grid(row=2, column=1)
    Button(frame, text='Back', command= lambda: ShowFrame(frame, MainPage())).grid(row=2,column=0)
=======
    Button(frame, text='Back',bg="navajo white", command=lambda: ShowFrame(frame, MainPage)).grid(column=1,row=4)
    Entry(frame).grid(row= 0, column=1,padx=30)
    Entry(frame).grid(row=1, column=1,padx=30)
>>>>>>> parent of fcc6258 (Revert "Merge pull request #10 from hafizsem/main")
def ReturnBookPage():
    FontStyle = ("Arial Narrow", 21)
    fgColor = "midnight blue"
    bgColor = "LightBlue1"

    frame = LabelFrame(window, text='RETURN\n', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor,font=FontStyle)
    frame.grid(padx=400, pady=250)

    ReturnNamelabel=Label(frame,text='Book Name: ',fg=fgColor,bg=bgColor,font=FontStyle)
    ReturnNamelabel.grid(column=0,row=0)
    ReturnIdLabel = Label(frame, text='Book ID: ',fg=fgColor,bg=bgColor,font=FontStyle)
    ReturnIdLabel.grid(column=0, row=1)
    Button(frame, text='Back',bg="navajo white", command=lambda: ShowFrame(frame, MainPage)).grid(column=1, row=4)
    Entry(frame).grid(row=0, column=1,padx=50)
    Entry(frame).grid(row=1, column=1,padx=50)

def RegisterUserPage():
<<<<<<< HEAD
    FontStyle = ("Arial Narrow", 14)
    frame = LabelFrame(window, text='Registration', height=720, width=480,
                       bd=15, relief='groove',
                       padx=5, pady=5)
    frame.grid()
    NameLabel = Label(frame, text="Name :", font=FontStyle)
    ICLabel = Label(frame, text="IC No. :", font=FontStyle)
=======
    FontStyle = ("Arial Narrow", 24)
    fgColor = "midnight blue"
    bgColor = "LightBlue1"

    frame = LabelFrame(window, text='REGISTRATION', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor, font= FontStyle )
    frame.grid(padx=400, pady=250)

    NameLabel = Label(frame, text="Name :", fg=fgColor,bg=bgColor,font=FontStyle)
    ICLabel = Label(frame, text="IC No. :", fg=fgColor,bg=bgColor, font=FontStyle)
>>>>>>> parent of fcc6258 (Revert "Merge pull request #10 from hafizsem/main")
    NameEntry = Entry(frame, font=FontStyle)
    ICEntry = Entry(frame,font=FontStyle)
    NameLabel.grid(row=0,column=0);NameEntry.grid(row=0,column=1,padx=50)
    ICLabel.grid(row=1, column=0);ICEntry.grid(row=1,column=1,padx=50)
    def GetEntryInfo():
        AddUser(ICEntry.get(), NameEntry.get())
        ShowFrame(frame, MainPage)
    Button(frame, text='Register',bg="navajo white",width=10, command=GetEntryInfo).grid(padx=50)
    Button(frame, text='Back',bg="navajo white",width=10, command=lambda: ShowFrame(frame, MainPage)).grid(padx=50)
def AddNewBook():
<<<<<<< HEAD
    FontStyle = ("Arial Narrow", 14)
    frame = LabelFrame(window, text='Registration', height=720, width=480,
                       bd=15, relief='groove',
                       padx=5, pady=5)
    frame.grid()
=======
    FontStyle = ("Arial Narrow", 21)
    fgColor = "midnight blue"
    bgColor = "LightBlue1"

    frame = LabelFrame(window, text='ADD NEW BOOK\n', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor, font=FontStyle)
    frame.grid(padx=400, pady=250)
>>>>>>> parent of fcc6258 (Revert "Merge pull request #10 from hafizsem/main")
    #initialise widgets
    BookNameLabel = Label(frame, text="Book Name :", fg=fgColor,bg=bgColor, font=FontStyle)
    ISBNLabel = Label(frame, text="International Standard Book Number (ISBN):", fg=fgColor,bg=bgColor, font=FontStyle)
    BookNameEntry = Entry(frame, font=FontStyle)
    ISBNEntry = Entry(frame, font=FontStyle)
    #putting widgets
    BookNameLabel.grid(row=0, column=0,padx=50)
    BookNameEntry.grid(row=0, column=1,padx=50)
    ISBNLabel.grid(row=1, column=0)
    ISBNEntry.grid(row=1, column=1)
    def GetEntryInfo():
        if AddBook(ISBNEntry.get(), BookNameEntry.get()) == False:
            messagebox.showinfo(message="The Book is already registered in the library")
        ShowFrame(frame, MainPage)
    Button(frame, text='Add',bg="navajo white",width=10, command=GetEntryInfo).grid()
    Button(frame, text='back',bg="navajo white",width=10, command=lambda: ShowFrame(frame, MainPage)).grid()
if __name__ == '__main__':
    LibraryAppInit()
    MainPage()
    window.mainloop()