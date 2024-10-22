
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "library")

def clear():
  for _ in range(3):
     print()

def addbook():
    title = input("Enter book name: ")
    author = input("Enter author name: ")
    bcode = input("Enter book code: ")
    total = input("Total books: ")
    genre = input("Enter genre: ")
    data = (title,author,bcode,total,genre)
    sql = "insert into books(title,author,bcode,total,genre) values(%s,%s,%s,%s,%s)"
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print(".............")
    
    print("Data entered successfully")
    main()


def issueb():
    name = input("Enter name:")
    rno  = input("Enter rno:")
    code = input("Enter book code:")
    date = input("Enter date (DD/MM/YY):")
    sql  = "insert into issue(name,rno,code,date) values(%s,%s,%s,%s)"
    data =(name,rno,code,date)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print("...............")
    print("Book issued to :",name)
    main()
    bookup(code,-1)


def submitb():
    name = input("Enter name:")
    regno  = input("Enter registration no:")
    code = input("Enter book code:")
    sdate = input("Enter date:")
    sql = "insert into submit(name,regno,code,sdate) values(%s,%s,%s,%s)"
    data = (name,regno,code,sdate)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print("...............")
    print("Book submitted from :",name)


def bookup(co,u):
    sql = "select TOTAL from books where BCODE = %s"
    data = (co,)
    c = mydb.cursor()
    c.execute(sql,data)
    myresult = c.fetchone()
    t = myresult[0] + u
    sql = "update books set TOTAL = %s where BCODE = %s"
    d = (t,co)
    c.execute(sql,d)
    mydb.commit()
    main()


def dbook():
    ac = input("Enter book code:")
    sql = "delete from books where BCODE = %s"
    data = (ac,)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    main()
    print("Done")


def dispbook():
    sql = "select * from books"
    c = mydb.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    for i in myresult:
        print("Book name:",i[0])
        print("Book Author:",i[1])
        print("Book code:",i[2])
        print("................")
    main()


def main():
  while True:
    clear()
    print(' L I B R A R Y    M E N U')
    print("\n1.  Add Books")
    print('\n2.  Issue book')
    print('\n3.  Submit book')
    print('\n4.  Delete book')
    print('\n5.  Display book')
    print('\n')
    choice = input("Enter task no:")
    print("............................")
    if(choice == '1'):
        addbook()
    elif(choice == '2'):
        issueb()
    elif(choice == '3'):
        submitb()
    elif(choice == '4'):
        dbook()
    elif(choice == '5'):
        dispbook()
    else:
        print("wrong choice")
        main()


def password():
    user = input("Enter Username: ")
    ps = user
    print("This is Library Managment: ")

    if  user == ps:
        main()
    else:
        user != ps
        print("Access Denied: ")
        password()

password()
