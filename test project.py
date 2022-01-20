from tkinter import *
from tkinter import messagebox
from tkinter import ttk #to use the comboboxafsd
import datetime as datetime
from Library_App_Engine import *
from tkcalendar import Calendar


window = Tk()
window.title("Library Catalogue")
window.geometry(f"{2000}x{1000}")
window.config(bg="LightBlue1")


def ShowFrame(CurrPage, NewPage):
    if CurrPage is not None:
        CurrPage.destroy()
    if callable(NewPage):
        NewPage()

def MainPage(Criteria='BookName'):
    PrintBookTable()
    PrintUserTable()
    frame = LabelFrame(window, text='WELCOME TO LIBRARY CATALOGUE !!!!\n')

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
    BookLiBox.bind( '<<ListboxSelect>>',BookLiBoxSel )
    SearchLbl=Label(frame)
    ChgSearchBt = Button(frame, text='Change Search Criteria')

    if Criteria=='BookName':
        SearchLbl['text']="Enter the Book Name: "
        SearchBt['command']=lambda *args: SearchBtCmd(BookName=SearchEntry.get())
        ChgSearchBt['command']=lambda: ShowFrame(frame, MainPage('ISBN'))
        SearchEntry.bind('<KeyPress>', lambda *args: SearchBtCmd(BookName=SearchEntry.get()))
    else:
        SearchLbl['text']="Enter the ISBN: "
        SearchBt['command']=lambda *args: SearchBtCmd(ISBN=SearchEntry.get())
        ChgSearchBt['command'] = lambda: ShowFrame(frame, MainPage('BookName'))
        SearchEntry.bind('<KeyPress>', lambda *args: SearchBtCmd(ISBN=SearchEntry.get()))

    #button frame
    def InstanceCtor():
        return SearchBook(ISBN=ISBNVar.get(), ExactMatch=True)
    EditBtn = Button(frame, text='Edit',command=lambda: ShowFrame(frame.destroy(),EditBookPage(InstanceCtor())))
    ReturnBtn = Button(frame, text='Return', command=lambda: ShowFrame(frame.destroy(), ReturnBookPage(InstanceCtor())))
    BorrowBtn = Button(frame, text='Borrow', command=lambda: ShowFrame(frame.destroy(), BorrowBookPage(ISBNVar.get(), BookNameVar.get())))
    RegisterBtn = Button(frame, text='Register New User', command=lambda: ShowFrame(frame, RegisterUserPage))
    AddBookBtn = Button(frame, text='Add New Book', command=lambda: ShowFrame(frame, AddNewBook))


    #styling
    FontStyle = ("Arial narrow", 21)
    FontStyle1 = ("halvetica", 21, "bold")
    fgColor = "midnight blue"
    bgColor = "LightBlue1"
    frame.config(height=1000, width=1000,bd=10, relief='groove',bg=bgColor, fg=fgColor, font=FontStyle1)
    SearchEntry.config(font=FontStyle)
    SearchLbl.config(font=FontStyle, bg=bgColor)
    BookLiBox.config(relief='sunken',width=55)

    #button styling
    BtnBgColor="#24d1bc"
    AddBookBtn.config(bg=BtnBgColor, width=20)
    RegisterBtn.config( bg=BtnBgColor, width=20)
    ChgSearchBt.config(bg=BtnBgColor, width=20)
    BorrowBtn.config(bg=BtnBgColor,width=10)
    ReturnBtn.config(bg=BtnBgColor,width=10)
    EditBtn.config(bg=BtnBgColor,width=10)
    SearchBt.config(bg=BtnBgColor,width=10)

    #positioning
    frame.grid(padx=400, pady=250)
    SearchLbl.grid(row=0)
    SearchEntry.grid(row=0, column=1, padx=5)
    BookLiBox.grid(row=1)
    BookInfoFrame.grid(row=1, column=1)
    SearchBt.grid(column=1)
    BorrowBtn.grid(column=1)
    EditBtn.grid(column=1)
    ReturnBtn.grid(column=1)
    ReturnBtn.grid(column=1)
    ChgSearchBt.grid(column=0, row=2)
    RegisterBtn.grid(column=0, row=3)
    AddBookBtn.grid(column=0, row=4)

def BorrowBookPage(ISBN=None, BookName=None):
    frame = LabelFrame(window, text='BORROW\n')
    frame.grid(padx=400, pady=250)
    BookLabel = Label(frame, text='Book ID: ')
    ISBNLbl = Label(frame, text='Book Name: ')
    BackBtn = Button(frame, text='Back', command=lambda: ShowFrame(frame, MainPage))
    ISBNEntry = Entry(frame)
    BookNameEntry = Entry(frame)
    BorrowerICEntry = Entry(frame)
    BorrowerICEntry.bind('<Return>', lambda *args: Borrow())
    def Borrow():
        msgbx = messagebox.askyesno(message="Confirm?")
        if msgbx == False:
            ShowFrame(frame, MainPage)
        else:
            if(BorrowBook(ISBN=ISBNEntry.get(), IC=BorrowerICEntry.get())=='IC Error'):
                msgbx=messagebox.askyesnocancel(message="The IC is not recorded in the system. Enter yes proceed to register or cancel to correct")
                if msgbx is False:
                    ShowFrame(frame,MainPage)
                elif msgbx is True:
                    ShowFrame(frame, RegisterUserPage)
            else:
                ShowFrame(frame, MainPage)
    BorrowBtn = Button(frame, text='Borrow', command=lambda: Borrow())

    if ISBN != None:
        ISBNEntry.insert(0, ISBN)
    if BookName != None:
        BookNameEntry.insert(0, BookName)
    ISBNEntry['state'] = "readonly"
    BookNameEntry['state'] = "readonly"
    ICLbl = Label(frame, text="IC: ")

    #styling
    FontStyle = ("Arial Narrow", 21)
    FontStyle1 = ("halvetica", 21, "bold")
    fgColor = "midnight blue"
    bgColor = "LightBlue1"
    BtnBgColor="#24d1bc"
    frame.config(height=1000, width=1000,bd=10, relief='groove',bg=bgColor, fg=fgColor, font=FontStyle1)
    ICLbl.config(fg=fgColor, bg=bgColor,font=FontStyle)
    BookLabel.config(fg=fgColor, bg=bgColor, font=FontStyle)
    ISBNLbl.config(fg=fgColor, bg=bgColor, font=FontStyle)
    ISBNEntry.config(font=FontStyle)
    BookNameEntry.config(fg=fgColor, font=FontStyle)
    BorrowerICEntry.config(font=FontStyle)
    BorrowBtn.config(bg=BtnBgColor, width=10)
    BackBtn.config(bg=BtnBgColor, width=10)

    #postioning
    BookLabel.grid(column=0, row=0)
    ISBNLbl.grid(column=0, row=1)
    ISBNEntry.grid(row=0, column=1, padx=5, pady=5)
    BookNameEntry.grid(row=1, column=1, padx=5, pady=5)
    ICLbl.grid(column=0, row=3)
    BorrowerICEntry.grid(column=1, row=3)
    BackBtn.grid(column=0, row=4)
    BorrowBtn.grid(column=1,row=4)

    if ISBN is None or BookName is None or ISBN == "None" or BookName == "None":
        ShowFrame(frame, MainPage)
    elif IsBookAvailable(BookName, ISBN) == False:
        messagebox.showinfo(message="The Book is not available for borrowing")
        ShowFrame(frame, MainPage)

def GetBookInfoFrame(parent, ISBNVar, BookNameVar, StatusVar):
    frame = LabelFrame(parent)
    Label(frame, text="ISBN :").grid(row=0)
    Label(frame, textvariable=ISBNVar).grid(row=0, column=1)
    Label(frame, text="Book Name :").grid(row=1)
    Label(frame, textvariable=BookNameVar).grid(row=1, column=1)
    Label(frame, text="Status :").grid(row=2)
    Label(frame, textvariable=StatusVar).grid(row=2, column=1)
    return frame

def ReturnBookPage(instance=None):
    FontStyle = ("Arial Narrow", 21)
    FontStyle1 = ("halvetica", 21, "bold")
    fgColor = "midnight blue"
    bgColor = "LightBlue1"

    frame = LabelFrame(window, text='RETURN\n', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor, font=FontStyle1)
    frame.grid(padx=400, pady=250)

    BookNameLbl = Label(frame, text='Book Name:', fg=fgColor, bg=bgColor, font=FontStyle)
    ISBNLbl = Label(frame, text='ISBN:', fg=fgColor, bg=bgColor, font=FontStyle)
    DateLbl = Label(frame, text=" Return Date :", bg=bgColor, font=FontStyle)
    ISBNSearchLbl = Label(frame, text='ISBN Search: ', fg=fgColor, bg=bgColor, font=FontStyle)
    cal = Calendar(frame, selectmode='day',
                   year=datetime.date.today().year, month=datetime.date.today().month,
                   day=datetime.date.today().day)
    ISBNVar = StringVar()
    ISBNSearchEntry = Entry(frame, font=("Arial Narrow", 16))
    def ISBNSearch():
        BookRes = SearchBook(ISBN=ISBNSearchEntry.get(), ExactMatch=False)
        if type(BookRes) is list:
            for i in BookRes:
                BookNameLbl['text'] = f"Book Name:\t{i['BookName']}"
                ISBNLbl['text']= f"Book Name:\t{i['ISBN']}"
                ISBNVar.set(value=i['ISBN'])
                break
        elif type(BookRes) is dict:
            BookNameLbl['text'] = f"Book Name: {BookRes['BookName']}"
            ISBNLbl['text'] = f"Book Name: {BookRes['ISBN']}"
            ISBNVar.set(value=BookRes['ISBN'])
    def Return():
        ISBN = ISBNVar.get()
        if IsBookAvailable(ISBN=ISBN) is True:
            messagebox.showinfo(message="The Book is in the library")
        else:
            BookRes = SearchBook(ISBN=ISBN, ExactMatch=True)
            BorrowingDate = datetime.datetime.strptime(BookRes['BorrowingDate'], '%Y-%m-%d')
            ReturnDate = datetime.datetime.strptime(cal.get_date(),'%m/%d/%y')
            datediff =ReturnDate-BorrowingDate
            dayUnit = datetime.timedelta(days=1)
            if datediff> dayUnit*7:
                messagebox.showinfo(message=f"""Overdue and please immediately pay the fine.
                The fine amount: RM0.20*{int(datediff//dayUnit)}days = RM{datediff//dayUnit*0.2:.2f}
                """)
            ReturnBook(ISBN)
            messagebox.showinfo(message=f"The book have been successfully returned")
            ShowFrame(frame, MainPage)
    ISBNSearchEntry.bind("<KeyPress>", lambda *args:ISBNSearch())
    if type(instance) is dict:
        ISBNVar.set(value=instance['ISBN'])
        BookNameLbl['text']=f"Book Name: {instance['BookName']}"
        ISBNLbl['text']=f"ISBN: {instance['ISBN']}"
        ISBNSearchEntry.insert(0, instance['ISBN'])
    BookNameLbl.grid(column=0, row=0)
    ISBNLbl.grid(column=0, row=1)
    ISBNSearchLbl.grid(column=0, row=2)
    ISBNSearchEntry.grid(row=2, column=1, padx=25)
    DateLbl.grid(row=3,column=0)
    cal.grid(row=3,column=1, padx=20, pady=4)
    Button(frame, text='Back', bg="#24d1bc",width=10, command=lambda: ShowFrame(frame, MainPage)).grid(column=0)
    Button(frame, text='Return', bg="#24d1bc", width=10, command=Return).grid(column=1, row=4)

def RegisterUserPage():
    FontStyle = ("Arial Narrow", 24)
    FontStyle1 = ("halvetica", 21, "bold")
    fgColor = "midnight blue"
    bgColor = "LightBlue1"
    frame = LabelFrame(window, text='REGISTRATION', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor, font=FontStyle1)
    frame.grid(padx=400, pady=250)

    def GetEntryInfo():
        IC=ICEntry.get()
        Name=NameEntry.get()
        Email=EmailEntry.get()
        if IC=='' or Name=='':
            return
        if Email == '':
            Email=None
        AddUser(IC, Name, Email)
        ShowFrame(frame, MainPage)
    RegBtn = Button(frame, text='Register',bg=bgColor, command=GetEntryInfo)
    BackBtn = Button(frame, text='Back', command=lambda: ShowFrame(frame, MainPage))

    RegBtn.config(bg="#24d1bc", width=10)
    NameLabel = Label(frame, text="Name :", fg=fgColor, bg=bgColor, font=FontStyle)
    ICLabel = Label(frame, text="IC No. :", fg=fgColor, bg=bgColor, font=FontStyle)
    EmailLabel = Label(frame, text="Email :", fg=fgColor, bg=bgColor, font=FontStyle)
    NameEntry = Entry(frame, font=FontStyle)
    ICEntry = Entry(frame, font=FontStyle)
    EmailEntry = Entry(frame, font=FontStyle)
    BackBtn.config(bg="#24d1bc", width=10)

    #positioning
    NameLabel.grid(row=0, column=0)
    NameEntry.grid(row=0, column=1, padx=50)
    ICLabel.grid(row=1, column=0)
    ICEntry.grid(row=1, column=1, padx=50)
    EmailLabel.grid(row=2, column=0)
    EmailEntry.grid(row=2,column=1)
    RegBtn.grid(row=3, column=1, padx=50)
    BackBtn.grid(row=3, column=0)

#if instance is None, then it is a adding new book page
def AddNewBook(instance=None):
    FontStyle = ("Arial Narrow", 21)
    FontStyle1 = ("halvetica", 21, "bold")
    fgColor = "midnight blue"
    bgColor = "LightBlue1"
    frame = LabelFrame(window, text='ADD NEW BOOK\n', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor, font=FontStyle1)
    if instance is not None:
        frame['text']='EDIT BOOK'
    frame.grid(padx=400, pady=250)
    # initialise widgets
    BookNameLabel = Label(frame, text="Book Name :", font=FontStyle)
    ISBNLabel = Label(frame, text="ISBN:",font=FontStyle)
    BookNameEntry = Entry(frame)
    ISBNEntry = Entry(frame)
    StatusBox = ttk.Combobox(frame, values=('Normal', 'Restricted'))
    StatusBox.state(["readonly"])
    BackBtn = Button(frame, text='Back',bg="#24d1bc", command=lambda: ShowFrame(frame, MainPage))

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

    AddBtn = Button(frame, text='Add', command=GetEntryInfo)
    if instance is not None:
        StatusBox.set(instance['Status'])
        BookNameEntry.insert(0, instance['BookName'])
        ISBNEntry.insert(0, instance['ISBN'])
        AddBtn['text'] = "Edit"

    #styling the widgets
    AddBtn.config(bg="#24d1bc", width=10)
    BackBtn.config(bg="#24d1bc", width=10)
    BookNameLabel.config(fg=fgColor, bg=bgColor, font=FontStyle)
    ISBNLabel.config(fg=fgColor, bg=bgColor, font=FontStyle)
    BookNameEntry.config(font=FontStyle)
    ISBNEntry.config(font=FontStyle)
    # putting widgets
    BookNameLabel.grid(row=0, column=0, padx=50)
    BookNameEntry.grid(row=0, column=1, padx=50)
    ISBNLabel.grid(row=1, column=0)
    ISBNEntry.grid(row=1, column=1)
    StatusBox.grid(row=2)
    BackBtn.grid()
    AddBtn.grid()

def EditBookPage(instance=None):
    if instance is None:
        MainPage()
    else:
        AddNewBook(instance)

if __name__ == '__main__':
    LibraryAppInit()
    MainPage()
    window.mainloop()