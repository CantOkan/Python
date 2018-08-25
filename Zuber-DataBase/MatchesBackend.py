import  psycopg2 as ps

def connect():
    connection = ps.connect(database="Uber", user="postgres", password="123456", host="localhost")
    cur=connection.cursor()
    cur.execute("Create Table IF NOT EXISTS Matches (Id integer PRIMARY KEY, title text, author text, year integer, isbn integer)")
    connection.commit()
    connection.close()

def view():
    connection = ps.connect(database="Uber", user="postgres", password="123456", host="localhost")
    cur=connection.cursor()
    cur.execute("Select m.id,c.driversurname,c.carmodel,u.username,u.surname,m.payment from matches m INNER JOIN Cars c on c.cid=m.cid INNER JOIN Users u On u.UId=m.uid")
    rows=cur.fetchall()
    connection.close()
    return rows

def search(CID="",UID=""):
    connection = ps.connect(database="Uber", user="postgres", password="123456", host="localhost")
    cur=connection.cursor()
    if(UID.isnumeric()):
        cur.execute("select * from matches where uid=%s ",(UID))
    elif(CID.isnumeric()):
        cur.execute("select * from matches where cid=%s", (CID,))
    elif(CID.isnumeric() and UID.isnumeric()):
        cur.execute("select * from matches where cid=%s or uid=%s", (CID,UID,))
    rows=list(cur)
    connection.close()
    return rows


def insert(CID,UID,Payment):
    connection = ps.connect(database="Uber", user="postgres", password="123456", host="localhost")
    cur=connection.cursor()
    cur.execute("INSERT INTO public.matches(cid, uid, payment) VALUES ( %s, %s,%s)",(CID,UID,Payment))
    connection.commit()
    connection.close()

def delete(id):
    connection = ps.connect(database="Uber", user="postgres", password="123456", host="localhost")
    cur=connection.cursor()
    cur.execute("Delete from matches where id=%s",(id,))
    connection.commit()
    connection.close()
