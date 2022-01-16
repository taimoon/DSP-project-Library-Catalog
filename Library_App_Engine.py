import sqlite3 as sql
from datetime import date
DBName = 'Library Database.db'
def LibraryDBInit():
    con = sql.connect(DBName)
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE USER(
            IC      TEXT NOT NULL PRIMARY KEY,
            Name    TEXT NOT NULL
        )""")
    cursor.execute("""
        INSERT INTO USER(IC, Name) VALUES ("LIBRARY_IC","LIBRARY")
    """)
    cursor.execute("""
        CREATE TABLE BOOK(
            ISBN            TEXT NOT NULL PRIMARY KEY,
            BookName       TEXT,
            BorrowingDate   TEXT,
            IC      TEXT DEFAULT  "LIBRARY_IC",
            CONSTRAINT FK_IC FOREIGN KEY(IC) REFERENCES USER(IC)
        )
    """)
    con.commit()
    con.close()
def LibraryAppInit():
    import os
    try:
        os.remove('Library Database.db')
        LibraryDBInit()
        AddUser('001103140327', 'Leong Teng Man')
        AddUser('010815990001', 'Hakurei Reimu')
        AddBook('666666', '6 is the strongest number')
        AddBook('666666666666', 'Tales of The Strongest Cirno')
    except:
        pass
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
    res=[]
    for i in cursor:
        resDict={}
        FieldName=[elem[0] for elem in cursor.description]
        idx=0
        for j in i:
            resDict[FieldName[idx]]=j
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
def AddUser(IC, Name):
    con = sql.connect(DBName)
    cursor = con.cursor()
    cursor.execute("""
        INSERT INTO USER(IC, Name) VALUES
        (?, ?);
    """, (IC, Name))
    con.commit()
    con.close()
def AddBook(ISBN, Name):
    con = sql.connect(DBName)
    cursor = con.cursor()
    try:
        cursor.execute("""
            INSERT INTO BOOK(ISBN, BookName) VALUES
            (?, ?);
        """, (ISBN, Name))
    except:
        return False
    con.commit()
    con.close()
def SearchUser(Name = None, IC = None):
    con=sql.connect(DBName)
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
def SearchBook(BookName = None, ISBN = None, ExactMatch = False, LIMIT = 5):
    con=sql.connect(DBName)
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
    res=CursorToDict(cursor)
    con.close()
    return res
def GetBookStatus(BookName = None, ISBN = None):
    book = SearchBook(BookName, ISBN)
    user = SearchUser(IC=book['IC'])
    return user['Name']
def IsBookAvailable(BookName = None, ISBN = None):
    temp = SearchBook(BookName, ISBN)
    return temp['IC']=="LIBRARY_IC"
def GetUserBorrowedBook(Name = None, IC = None):
    user=SearchUser(Name, IC)
    if not (user == None):
        con = sql.connect(DBName)
        cursor = con.cursor()
        cursor.execute(f"""
            SELECT ISBN, BookName, BorrowingDate FROM BOOK
            WHERE IC like \"{user['IC']}\"
        """)
        res=CursorToDict(cursor)
        con.close()
        return res
    return None
def UpdateData(Table, CurrPK, PKName, NewInstance):
    con = sql.connect(DBName)
    cursor = con.cursor()
    query = f"UPDATE {Table} SET "
    for i in NewInstance:
        query += f"{i} = "
        if  isinstance(NewInstance[i], str) == True:
            query += f"\"{NewInstance[i]}\""
        else:
            query += f"{NewInstance[i]}"
        query +=", "
    query=query[:-2:]
    query+=f"WHERE {PKName} ="
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
def UpdateBook(ISBN, IC, Date=date.today()):
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
    except:
        return False