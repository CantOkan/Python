import  psycopg2

def connect():
    connection = psycopg2.connect(database="Uber", user="postgres", password="123456", host="localhost")
    cur=connection.cursor()
    cur.execute("Create Table IF NOT EXISTS cars (Id integer PRIMARY KEY, title text, author text, year integer, isbn integer)")
    connection.commit()
    connection.close()

def view():
    connection = psycopg2.connect(database="Uber", user="postgres", password="123456", host="localhost")
    cur = connection.cursor()
    cur.execute("Select * from Cars")
    rows=cur.fetchall()
    connection.close()
    return rows

def search(ID="",DriverName="",DriverSurname="",CarModel=""):
    connection = psycopg2.connect(database="Uber", user="postgres", password="123456", host="localhost")
    cur=connection.cursor()
    cur.execute("select * from cars where cid=%s or drivername=%s or driversurname=%s or carmodel=%s",(ID,DriverName,DriverSurname,CarModel))
    rows=list(cur)
    connection.close()
    return rows

def insert(ID,DriverName,DriverSurname,CarModel):
    connection = psycopg2.connect(database="Uber", user="postgres", password="123456", host="localhost")
    cur=connection.cursor()
    cur.execute("Insert Into cars Values(%s,%s,%s,%s)",(ID,DriverName,DriverSurname,CarModel))
    connection.commit()
    connection.close()

def delete(id):
    connection = psycopg2.connect(database="Uber", user="postgres", password="123456", host="localhost")
    cur=connection.cursor()
    cur.execute("Delete from cars where cid=%s",(id,))
    connection.commit()
    connection.close()

def update(ID,DriverName,DriverSurname,CarModel):
    connection = psycopg2.connect(database="Uber", user="postgres", password="123456", host="localhost")
    cur = connection.cursor()
    cur.execute("UPDATE cars SET drivername=%s, driversurname=%s, carmodel=%s WHERE cid=%s",(DriverName,DriverSurname,CarModel,ID))
    connection.commit()
    connection.close()