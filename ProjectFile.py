__author__ = 'snow'


import sqlite3
import csv

from datetime import date, datetime

db_connection=sqlite3.connect("FLAPPY.db",detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
db_cursor=db_connection.cursor()

try:
    db_connection.execute("CREATE TABLE IF NOT EXISTS Client(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,Client_name TEXT,Phone TEXT,Email TEXT  )")
    db_connection.commit()
    print("table created")
except sqlite3.OperationalError:
    print(" Client table not created")

try:
    db_connection.execute("CREATE TABLE IF NOT EXISTS Orders(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,Client_id INTEGER NOT NULL,Product TEXT ,Weight INTEGER,date_time DATE)")
    db_connection.commit()
    print("table created")
except sqlite3.OperationalError:
    print("order table not created")


def mail_serviece():
    pass





def Client_create(i):

    Mark=i

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

    if Mark==2:
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
    try:
        ids=int(input("Give a Client's ID:"))
        id_finding=db_cursor.execute("SELECT ID FROM Client WHERE ID=(?)",(ids,))
        # print(tuple(id_finding)!=())
        pk=tuple(id_finding)
        if pk!=():
            print("good client is in our db")
            try:
                    product=input("ProductName:")
                    weight=int(input("Weight:"))
                    today=date.today()
                    db_connection.execute("INSERT INTO Orders(Client_id,Product,Weight,date_time) VALUES (?,?,?,?);",(ids,product,weight,today))
                    db_connection.commit()
                    print("order placed")
            except sqlite3.OperationalError:
                    print("Not placed the order")
        else:
            print("bad client is not in our db")
            try:
                    # names=input("name:")
                    # phone=input("phone:")
                    # email=input("email:")
                    # # db_connection.execute("INSERT INTO Client VALUES (?, ?, ?);",(names, phone,email))
                    # db_connection.execute("INSERT INTO Client(Client_name,Phone,Email) VALUES (?,?,?);",(names,phone,email))
                    # db_connection.commit()
                    i=1
                    Client_create(i)
                    print("-----now make the order---")
                    product=input("ProductName:")
                    weight=int(input("Weight:"))
                    today=date.today()
                    try:
                        db_connection.execute("INSERT INTO Orders(Client_id,Product,Weight,date_time) VALUES (?,?,?,?);",(ids,product,weight,today))
                        db_connection.commit()
                        print("\n \n \n  order placed for missing id")
                    except sqlite3.OperationalError:
                        print("Not placed the order for missing id")

            except sqlite3.OperationalError:
                    print("Something inside else is not good")











    except sqlite3.OperationalError:
        print("problems")

    menu()


def Order_list():
    try:
        c_list= db_cursor.execute("SELECT * FROM Orders ORDER BY date_time DESC")
        for i in c_list:
            print(list(i))
    except sqlite3.OperationalError:
        print("Order list not created")

    menu()

def Export():


    #to export as csv file



    # with open("wub.csv", "wb") as write_file:
    #
    #       for row in db_cursor.execute("SELECT * FROM Orders "):
    #              writeRow = " ".join([str(i) for i in row])
    #              write_file.write(writeRow.encode())
    #
    #       print("File Created")

     data=db_cursor.execute("SELECT * FROM Orders")
     with open('output.csv', 'w') as f:
          writer = csv.writer(f)
          writer.writerow(['Id','Client_id','Product_Name','Weight','Date'])
          writer.writerows(data)
     menu()





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
    print()
    p=int(input("Enter the number:"))
    if p==1:
       i=2

       Client_create(i)
    elif p==2:
       Client_list()
    elif p==3:
       Order_create()
    elif p==4:
       Order_list()
    elif p==5:
       Export()
    else:
        db_cursor.close()
        db_connection.close()


menu()


