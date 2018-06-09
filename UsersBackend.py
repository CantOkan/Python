import  psycopg2

def connect():
    connection = psycopg2.connect(database="Uber", user="postgres", password="123456", host="localhost")
    cur=connection.cursor()
    cur.execute("Create Table IF NOT EXISTS book (Id integer PRIMARY KEY, title text, author text, year integer, isbn integer)")
    connection.commit()
    connection.close()
def view():
    connection = psycopg2.connect(database="Uber", user="postgres", password="123456", host="localhost")
    cur = connection.cursor()
    cur.execute("Select * from users")
    rows=cur.fetchall()
    connection.close()
    return rows

def search(ID="",UserName="",SurName="",age=""):
    connection = psycopg2.connect(database="Uber", user="postgres", password="123456", host="localhost")
    cur=connection.cursor()
    cur.execute("select * from users where uid=%s or username=%s or surname=%s or age=%s",(ID,UserName,SurName,age))
    rows=list(cur)
    connection.close()
    return rows

def delete(id):
    connection = psycopg2.connect(database="Uber", user="postgres", password="123456", host="localhost")
    cur=connection.cursor()
    cur.execute("Delete from users where uid=%s",(id,))
    connection.commit()
    connection.close()

def insert(ID,UserName,SurName,age):
    connection = psycopg2.connect(database="Uber", user="postgres", password="123456", host="localhost")
    cur=connection.cursor()
    cur.execute("Insert Into users Values(%s,%s,%s,%s)",(ID,UserName,SurName,age))
    connection.commit()
    connection.close()

def update(ID,UserName,SurName,age):
    connection = psycopg2.connect(database="Uber", user="postgres", password="123456", host="localhost")
    cur = connection.cursor()
    cur.execute("UPDATE users SET username=%s, surname=%s, age=%s WHERE uid=%s",(UserName,SurName,age,ID))
    connection.commit()
    connection.close()