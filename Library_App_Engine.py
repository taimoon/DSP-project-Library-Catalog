import sqlite3 as sql
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
            Book_Name       TEXT,
            IC      TEXT DEFAULT  "LIBRARY_IC",
            FOREIGN KEY(IC) REFERENCES USER(IC)
        )
    """)
    con.commit()
    con.close()
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
            INSERT INTO BOOK(ISBN, Book_Name) VALUES
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
def SearchBook(BookName = None, ISBN = None):
    con=sql.connect(DBName)
    cursor = con.cursor()
    if BookName != None:
        cursor.execute(f"""
                    SELECT * FROM BOOK
                    WHERE Book_Name LIKE \"{BookName}\"
                """)
    elif ISBN != None:
        cursor.execute(f"""
                    SELECT * FROM BOOK
                    WHERE ISBN LIKE \"{ISBN}\"
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