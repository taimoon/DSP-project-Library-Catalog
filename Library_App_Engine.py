import sqlite3 as sql
from datetime import date

DBName = 'Library Database.db'
def LibraryDBInit():
    con = sql.connect(DBName)
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE USER(
            IC      TEXT NOT NULL PRIMARY KEY,
            Name    TEXT NOT NULL,
            Email   TEXT,
            Privilege TEXT NOT NULL DEFAULT "Normal"
        )""")
    cursor.execute("""
        INSERT INTO USER(IC, Name, Privilege) VALUES ("LIBRARY_IC","LIBRARY", "HIGHEST")
    """)
    cursor.execute("""
        CREATE TABLE BOOK(
            ISBN            TEXT NOT NULL PRIMARY KEY,
            BookName       TEXT,
            BorrowingDate   TEXT,
            IC      TEXT DEFAULT  "LIBRARY_IC",
            Status  TEXT DEFAULT "Normal",
            CONSTRAINT FK_IC FOREIGN KEY(IC) REFERENCES USER(IC)
        )
    """)
    con.commit()
    con.close()


def LibraryAppInit():
    import os
    os.remove('Library Database.db')
    LibraryDBInit()
    AddUser('001103140327', 'Leong Teng Man', 'leongahman@gmail.com')
    AddUser('010815990001', 'Hakurei Reimu', None)
    AddUser('004214111999', 'Ahmad haikal bin syuib', 'Kall34@gmail.com')
    AddUser('010321218999', 'Muhammad Syakur Bin Ali', 'Syah56@gmail.com')
    AddUser('010711454415', 'Yep Lean Wan', 'siozo89@gmail.com')
    AddUser('010321308615', 'M. Umasundari', 'linda.wah@gmail.com')
    AddUser('010607639037', 'Hao Kai Leang ', 'fgee@gmail.com')
    AddUser('002109286007', 'Nurul Izzah Binti Arif', 'izhere67@gmail.com')
    AddUser('002918114919', 'Husna Binti Abdullah', 'Hush2235@gmail.com')
    AddUser('010814062399', 'Aizat Amirul Bin Zakir', 'Aizatte34@gmail.com')
    AddUser('099319044380', 'Aezul Bin Mat Zin', 'Aus695@gmail.com')
    AddUser('010709637876', 'Aiman Nabilah Binti Said', 'Aizatte34@gmail.com')
    AddBook('9781603090254', 'Alec: The Years Have Pants,','Available')
    AddBook('9781603094955', 'Better Place','Available')
    AddBook('1735322342', 'Dont Close Your Eyes','Available')
    AddBook('0346148936', 'Complicated Moonlight','Available')
    AddBook('1400096898', 'Memoirs of a Geisha','Available')
    AddBook('0399155341', 'The Help','Available')
    AddBook('0316166685', 'The Lovely Bones','Available')
    AddBook('1594633665', 'The Girl on the Train','Available')
    AddBook('0063093575', 'The Girl with the Dragon Tattoo','Restricted')
    AddBook('0385547129', 'Murder Under Her Skin','Available')
    AddBook('1496736249', 'The Spanish Daughter','Restricted')
    AddBook('666666666666', 'Tales of The Strongest Cirno', 'Restricted')
    


def ShowAllTable():
    con = sql.connect(DBName)
    cursor = con.cursor()
    cursor.execute("""
        SELECT 
            name
        FROM 
            sqlite_schema
        WHERE 
            type ='table' AND 
            name NOT LIKE 'sqlite_%';
        """)
    for i in cursor:
        print(i)
    con.close()


def TestDB():
    con = sql.connect(DBName)
    cursor = con.cursor()
    cursor.execute("""
        SELECT 
            sql
        FROM 
            sqlite_schema
        WHERE 
            name LIKE "BOOK";
    """)
    for i in cursor:
        print(i)
    con.close()


def CursorToDict(cursor):
    res = []
    for i in cursor:
        resDict = {}
        FieldName = [elem[0] for elem in cursor.description]
        idx = 0
        for j in i:
            resDict[FieldName[idx]] = j
            idx = idx + 1
        res.append(resDict)
    if len(res) == 0:
        return None
    elif len(res) == 1:
        return res[0]
    else:
        return res


def PrintUserTable():
    con = sql.connect(DBName)
    cursor = con.cursor()
    cursor.execute("""
        SELECT * FROM USER;
    """)
    for i in cursor:
        print(i)
    con.close()


def PrintBookTable():
    con = sql.connect(DBName)
    cursor = con.cursor()
    cursor.execute("""
        SELECT * FROM BOOK;
    """)
    for i in cursor:
        print(i)
    con.close()


def AddUser(IC, Name, Email, Privilege="Normal"):
    con = sql.connect(DBName)
    cursor = con.cursor()
    cursor.execute("""
        INSERT INTO USER(IC, Name, Email, Privilege) VALUES
        (?, ?, ?, ?);
    """, (IC, Name, Email, Privilege))
    con.commit()
    con.close()


def AddBook(ISBN, Name, Status=None):
    con = sql.connect(DBName)
    cursor = con.cursor()
    try:
        if Status is not None:
            cursor.execute("""
                            INSERT INTO BOOK(ISBN, BookName, Status) VALUES
                            (?, ?, ?);
            """, (ISBN, Name, Status))
        else:
            cursor.execute("""
                INSERT INTO BOOK(ISBN, BookName) VALUES
                (?, ?);
            """, (ISBN, Name))
    except:
        return False
    con.commit()
    con.close()


def SearchUser(Name=None, IC=None):
    con = sql.connect(DBName)
    cursor = con.cursor()
    if Name != None:
        cursor.execute(f"""
                    SELECT * FROM USER
                    WHERE Name LIKE \"{Name}\"
                """)
    elif IC != None:
        cursor.execute(f"""
                    SELECT * FROM USER
                    WHERE IC LIKE \"{IC}\"
                """)
    res = CursorToDict(cursor)
    con.close()
    return res


def SearchBook(BookName=None, ISBN=None, ExactMatch=False, LIMIT=5):
    con = sql.connect(DBName)
    cursor = con.cursor()
    if ExactMatch == False:
        if BookName != None:
            cursor.execute(f"""
                        SELECT * FROM BOOK
                        WHERE BookName LIKE '%{BookName}%'
                        LIMIT {LIMIT}
                    """)
        elif ISBN != None:
            cursor.execute(f"""
                        SELECT * FROM BOOK
                        WHERE ISBN LIKE '%{ISBN}%'
                        LIMIT {LIMIT}
                    """)
    else:
        if BookName != None:
            cursor.execute(f"""
                        SELECT * FROM BOOK
                        WHERE BookName LIKE '{BookName}'
                        LIMIT {LIMIT}
                    """)
        elif ISBN != None:
            cursor.execute(f"""
                        SELECT * FROM BOOK
                        WHERE ISBN LIKE '{ISBN}'
                        LIMIT {LIMIT}
                    """)
    res = CursorToDict(cursor)
    con.close()
    return res


def GetBookCurrBorrower(BookName=None, ISBN=None):
    book = SearchBook(BookName, ISBN, ExactMatch=True)
    if book is not None:
        user = SearchUser(IC=book['IC'])
    if user is not None:
        return user['Name']
    return None


def IsBookAvailable(BookName=None, ISBN=None):
    temp = SearchBook(BookName, ISBN, ExactMatch=True)
    if temp is None:
        return False
    return temp['IC'] == "LIBRARY_IC" and temp['Status'] != 'Restricted'

def GetBookStatus(BookName=None, ISBN=None):
    temp = SearchBook(BookName, ISBN, ExactMatch=True)
    if temp is None:
        return "No record"
    elif temp['Status'] == 'Restricted':
        return "Only Internal Reading"
    elif temp['IC'] == "LIBRARY_IC":
        return "Available for borrowing"
    else:
        return "No Available"

def GetUserBorrowedBook(Name=None, IC=None):
    user = SearchUser(Name, IC)
    if not (user == None):
        con = sql.connect(DBName)
        cursor = con.cursor()
        cursor.execute(f"""
            SELECT ISBN, BookName, BorrowingDate FROM BOOK
            WHERE IC like \"{user['IC']}\"
        """)
        res = CursorToDict(cursor)
        con.close()
        return res
    return None


def UpdateData(Table, CurrPK, PKName, NewInstance):
    con = sql.connect(DBName)
    cursor = con.cursor()
    query = f"UPDATE {Table} SET "
    for i in NewInstance:
        query += f"{i} = "
        if isinstance(NewInstance[i], str) == True:
            query += f"\"{NewInstance[i]}\""
        else:
            query += f"{NewInstance[i]}"
        query += ", "
    query = query[:-2:]
    query += f"WHERE {PKName} ="
    if isinstance(NewInstance[PKName], str) == True:
        query += f"\"{CurrPK}\""
    else:
        query += f"{CurrPK}"
    cursor.execute(query)
    con.commit()
    con.close()


def UpdateBook(CurrISBN, NewInstance):
    UpdateData("BOOK", CurrISBN, "ISBN", NewInstance)


def UpdateUser(CurrIC, NewInstance):
    UpdateData("USER", CurrIC, "IC", NewInstance)


def DeleteUser(IC):
    con = sql.connect(DBName)
    cursor = con.cursor()
    cursor.execute(f"""
            DELETE FROM USER
            WHERE IC=\"{IC}\"
        """)
    con.commit()
    con.close()


def DeleteBook(ISBN):
    con = sql.connect(DBName)
    cursor = con.cursor()
    cursor.execute(f"""
            DELETE FROM BOOK
            WHERE ISBN=\"{ISBN}\"
        """)
    con.commit()
    con.close()


def BorrowBook(ISBN, IC,  Date=date.today()):
    con = sql.connect(DBName)
    con.execute("PRAGMA foreign_keys = 1")
    cursor = con.cursor()
    try:
        cursor.execute(f"""
            UPDATE BOOK 
            SET IC = \"{IC}\",
                BorrowingDate = \"{Date}\"
            WHERE ISBN = \"{ISBN}\"
        """)
        con.commit()
        con.close()
        return True
    except sql.IntegrityError:
        return "IC Error"
    except:
        return False


def ReturnBook(ISBN, Date=None):
    return BorrowBook(ISBN,"LIBRARY_IC")
