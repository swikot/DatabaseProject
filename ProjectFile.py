__author__ = 'snow'


import sqlite3

db_connection=sqlite3.connect("PENGUIN.db")
db_cursor=db_connection.cursor()

try:
    db_connection.execute("CREATE TABLE IF NOT EXISTS Client(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,Client_name TEXT,Phone TEXT,Email TEXT  )")
    db_connection.commit()
    print("table created")
except sqlite3.OperationalError:
    print(" Client table not created")

try:
    db_connection.execute("CREATE TABLE IF NOT EXISTS Orders(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,Client_id INTEGER NOT NULL,Product TEXT ,Weight INTEGER,date_time DATETIME)")
    db_connection.commit()
    print("table created")
except sqlite3.OperationalError:
    print("order table not created")






def Client_create():



    try:
        names=input("name:")
        phone=input("phone:")
        email=input("email:")
        # db_connection.execute("INSERT INTO Client VALUES (?, ?, ?);",(names, phone,email))
        db_connection.execute("INSERT INTO Client(Client_name,Phone,Email) VALUES (?,?,?);",(names,phone,email))
        db_connection.commit()
        result=db_cursor.execute("SELECT ID FROM Client WHERE Email=(?);",(email,))
        for i in result:
            print("Welcome to our courier company. Client Id is {{",list(i)[0] ," }}" )

        print(" Client Created")
    except sqlite3.OperationalError:
        print("No Client Created")


    menu()

def Client_list():
    try:
        c_list= db_cursor.execute("SELECT * FROM Client ORDER BY Client_name")
        for i in c_list:
            print(list(i))
    except sqlite3.OperationalError:
        print("Client list not created")

    menu()


def Order_create():
    print("Order Created")

def Order_list():
    try:
        c_list= db_cursor.execute("SELECT * FROM Orders ORDER BY date_time DESC")
        for i in c_list:
            print(list(i))
    except sqlite3.OperationalError:
        print("Client list not created")

    menu()

def Export():
    print("Export")



def menu():
    print()
    print()
    print("-------Menu-------")
    print("1:Client Creating")
    print("2:Client List")
    print("3:Order Create")
    print("4:Order List")
    print("5:Export Order")
    print()
    print("Enter the number")
    p=int(input())
    if p==1:
       Client_create()
    elif p==2:
       Client_list()
    elif p==3:
       Order_create()
    elif p==4:
       Order_list()
    else:
       Export()


menu()


