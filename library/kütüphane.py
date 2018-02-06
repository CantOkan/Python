import sqlite3


class book():
    def __init__(self,name,author,publisher,categories,page):
        self.name=name
        self.author=author
        self.publisher=publisher
        self.categories=categories
        self.page=page
    def __str__(self):
        return self.name,self.author,self.publisher,self.categories,self.page

class libary():
    def __init__(self):
        self.connetc()
    def connetc(self):
        self.con=sqlite3.connect("library.db")
        self.cursor=self.con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books(name TEXT,author TEXT,publisher TEXT,categories TEXT,page INT)")
        self.con.commit()
    def cclose(self):
        self.con.close()
    def show(self):
        self.cursor.execute("Select * from books")
        liste=self.cursor.fetchall()
        for i in liste:
            print(i)
    def detect(self,name):
        self.cursor.execute("Select * from books where name = ?",(name,))
        liste=self.cursor.fetchall()
        for i in liste:
            print(liste)
    def Insert(self,book):
        self.cursor.execute("Insert into books Values(?,?,?,?,?)",(book.name,book.author,book.publisher,book.categories,book.page))
        self.con.commit()
    def delbook(self,name):
        self.cursor.execute("Delete From books where name=?",(name,))
        self.con.commit()
    def updatebook(self,name):
        self.cursor.execute("Select * from books where name = ?",(name,))
        b=self.cursor.fetchall()
        if(b!=None):
            ncat = input("newCategories :")
            oldcat = input("OldCategories :")
            self.cursor.execute("Update books set categories=? where categories=? AND name=? ",(ncat,oldcat,name))
            self.con.commit()
