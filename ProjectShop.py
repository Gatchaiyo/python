#สร้างtable
"""
import sqlite3
conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
c = conn.cursor()
#ตารางUser
c.execute ('''CREATE TABLE User (No integer PRIMARY KEY AUTOINCREMENT,
    Username varchar(30) NOT NULL,
    Password varchar(30) NOT NULL)''')
#ตารางPreduct
c.execute ('''CREATE TABLE product (No integer PRIMARY KEY AUTOINCREMENT,
    Productname varchar(30) NOT NULL,
    Price integer(30) NOT NULL)''')
#ตารางตะกร้า
c.execute ('''CREATE TABLE Basket (No integer PRIMARY KEY AUTOINCREMENT,
    Productname varchar(30) NOT NULL,
    Price integer(30) NOT NULL,
    Num integer(30) NOT NULL)''')
conn.commit()
conn.close()

import sqlite3
conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
c = conn.cursor()
def insertTousers (Username,Password):
    try:
        conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
        c = conn.cursor()
        sql = '''INSERT INTO User (Username,Password) VALUES(?,?)'''
        data = (Username,Password)
        c.execute(sql,data)
        conn.commit()
        c.close
    except sqlite3.Error as e:
        print('Fail to insert :',e)
    finally :
        if conn :
            conn.close()
insertTousers("sing","1234")
"""
#สินค้าทั้งหมด
"""
import sqlite3
conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
c = conn.cursor()
def insertTousers (Productname,Price):
    try:
        conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
        c = conn.cursor()
        sql = '''INSERT INTO product (Productname,Price) VALUES(?,?)'''
        data = (Productname,Price)
        c.execute(sql,data)
        conn.commit()
        c.close
    except sqlite3.Error as e:
        print('Fail to insert :',e)
    finally :
        if conn :
            conn.close()
insertTousers("CPU i3","2500")
insertTousers("CPU i5","4500")
insertTousers("CPU i7","5500")
insertTousers("CPU i9","8500")
insertTousers("GPU RX570","4000")
insertTousers("GPU GTX1050","4000")
insertTousers("GPU GTX1050TI","4200")
insertTousers("GPU GTX1060","5000")
insertTousers("GPU GTX1060TI","5300")
insertTousers("GPU GTX1650","4700")
insertTousers("RAM 4 GB x1","980")
insertTousers("RAM 4 GB x2","1960")
insertTousers("RAM 4 GB DDR4 x1","1150")
insertTousers("RAM 4 GB DDR4 x2","2300")
insertTousers("RAM 8 GB DDR4 x1","1600")
insertTousers("RAM 8 GB DDR4 x2","3200")
"""
#ตะกร้า
"""
import sqlite3
conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
c = conn.cursor()
def insertTousers (Productname,Price,Num):
    try:
        conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
        c = conn.cursor()
        sql = '''INSERT INTO Basket (Productname,Price,Num) VALUES(?,?,?)'''
        data = (Productname,Price,Num)
        c.execute(sql,data)
        conn.commit()
        c.close
    except sqlite3.Error as e:
        print('Fail to insert :',e)
    finally :
        if conn :
            conn.close()
insertTousers("CPU i3","2500","0")
insertTousers("CPU i5","4500","0")
insertTousers("CPU i7","5500","0")
insertTousers("CPU i9","8500","0")
insertTousers("GPU RX570","4000","0")
insertTousers("GPU GTX1050","4000","0")
insertTousers("GPU GTX1050TI","4200","0")
insertTousers("GPU GTX1060","5000","0")
insertTousers("GPU GTX1060TI","5300","0")
insertTousers("GPU GTX1650","4700","0")
insertTousers("RAM 4 GB x1","980","0")
insertTousers("RAM 4 GB x2","1960","0")
insertTousers("RAM 4 GB DDR4 x1","1150","0")
insertTousers("RAM 4 GB DDR4 x2","2300","0")
insertTousers("RAM 8 GB DDR4 x1","1600","0")
insertTousers("RAM 8 GB DDR4 x2","3200","0")

"""


def Status():
    global choice
    print("*"*40,"\n----------welcome to smileIT----------\n","*"*40,"\n=====Please login to enter the program=====")
    choice=input("\n\t#Register [n] \n\t#Login [y] \n\t#Exit programe [q] \n\tPlease select : ")


#Register
def Register():
    print('***Register***')
    Newuser = str(input('Username : '))
    Newpassword = str(input('Passworsd : '))
    import sqlite3
    conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
    c = conn.cursor()
    try:
        data = (str(Newuser),str(Newpassword))
        c.execute('''insert into User (Username,Password) VAlUES(?,?)''',data)
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print('Register Failed',e)
    finally:
        if conn:
            conn.close()

#Login
def Login():
    print("\n***Login***")
    us = str(input("USERNAME :"))
    pas = str(input("PASSWORD :"))
    nologin = 0
    try :
        import sqlite3
        conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
        c = conn.cursor()
        data = (str(us),str(pas))
        c.execute('select No FROM user WHERE username =? and password =?',data)
        result = c.fetchall()
        for x in result:
            nologin = x[0] #ให้ตัวแปรมีค่าเท่ากับตัวที่อยู่ในตาราง ตามเงื่อนไข
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :
        if conn :
            conn.close()
    if nologin > 0 :
        def Menu():#เมนูร้านค้า
            global choice
            print('\n=======Menu=======\n','\nShow all products [1] \nPick up products [2] \nShow basket [3] \nExit programe [4] ')
            choice = input('\nPlease select Menu :')

        #แสดงข้อมูลสินค้า
        def show(): 
            print("\n----------All Product----------\n","="*32)
            print("No---Product Name---Price---\n","="*32)
            import sqlite3

            conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
            c = conn.cursor()
            c.execute('''SELECT * FROM product''')

            result = c.fetchall()
            for x in result :
                print(x)
        #หยิบสินค้าลงตะกร้า  
        def Pick():
            print("\n----------All Product----------\n","="*32)
            print("No---Product Name---Price---\n","="*32)
            z = "y"
            while z == "y":
                import sqlite3
                conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
                c = conn.cursor()
                c.execute('''SELECT * FROM Basket''')
                result = c.fetchall()
                for x in result :
                    print(x)
                conn.commit()
                c.close()

                c = conn.cursor()
                p = int(input("Select item : "))
                p2 = str(p)
                if p2 == "x":
                    break
                conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
                c = conn.cursor()
                numitem = int(input("number you want to pick : "))
                try:
                    data = int(p),
                    c.execute('SELECT Num FROM Basket WHERE No =?',data)
                    result = c.fetchall()
                    for x in result:
                        numx = x[0]
                    conn.commit()
                    c.close()
                except sqlite3.Error as e:
                    print(e)
                finally:
                    if conn :
                        conn.close()
                conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
                c = conn.cursor()
                try:
                    numupdate = numitem + numx
                    data2 = (numupdate,p)
                    c.execute('''UPDATE Basket SET Num =? WHERE No =?''',data2)
                    conn.commit()
                    c.close()
                except sqlite3.Error as e:
                    print(e)
                finally:
                    if conn :
                        conn.close()

                z = str(input("Do you want to pick up again ?(y/n : )"))
        #แสดงสินค้าในตะกร้า+คำนวนราคา
        def showbk():
            print("\n------------Basket-------------\n","="*32)
            print("No---Product Name---Price---Num--\n","="*32)

            import sqlite3
            conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
            c = conn.cursor()
            c.execute('select * from Basket where Num != 0')
            result = c.fetchall()
            for x in result :
                print(x)
            conn.commit()
            c.close()

            z = 1
            y = 1
            allsum = 0
            sum = 0
            while z <=16 :
                import sqlite3
                conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
                c = conn.cursor()
                data = y,
                c.execute('select Num from Basket where No =?',data)
                result = c.fetchall()
                for x in result :
                    a = x[0]
                data = y,
                c.execute('select Price from Basket where No =?',data)
                result = c.fetchall()
                for x in result :
                    b = x[0]
                sum = int(a)*int(b)
                allsum = allsum + sum
                z = z+1
                y = y+1
                conn.commit()
                c.close()
            print("*"*20,"\nTotal product price : ",allsum,)
            #แก้ไขรายการสินค้า
            receipt=str(input("Would you like to change your basket ? (y/n) : "))
            x="y"
            while x == "y":
                if receipt == "y":
                    print("\n-----==============Busket==========-----\n","="*32)
                    print("\n-----plese select product to change-----\n","="*32)
                    print("No---Product Name---Price---Num--\n","="*32)
                    import sqlite3
                    conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
                    c = conn.cursor()
                    c.execute('select * from Basket where Num != 0')
                    result = c.fetchall()
                    for x in result :
                        print(x)
                    conn.commit()
                    c.close()

                    z = 1
                    y = 1
                    allsum = 0
                    sum = 0
                    while z <=16 :
                        import sqlite3
                        conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
                        c = conn.cursor()
                        data = y,
                        c.execute('select Num from Basket where No =?',data)
                        result = c.fetchall()
                        for x in result :
                            a = x[0]
                        data = y,
                        c.execute('select Price from Basket where No =?',data)
                        result = c.fetchall()
                        for x in result :
                            b = x[0]
                        sum = int(a)*int(b)
                        allsum = allsum + sum
                        z = z+1
                        y = y+1
                        conn.commit()
                        c.close()
                    print("*"*20,"\nTotal product price : ",allsum,)
                    import sqlite3
                    conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
                    c = conn.cursor()
                    c.execute('''SELECT * FROM Basket''')

                    result = c.fetchall()
                    for x in result :  
                        print(x)
                    n2 = str(input("\nplese select 'No' product to change "))
                    print("change to ? ")
                    b1 = input("Num ")
                    conn.commit()
                    conn.close()
                    import sqlite3
                    conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
                    c = conn.cursor()
                    try :
                        data = (str(b1),str(n2))
                        c.execute('''UPDATE Basket SET Num =? WHERE No =?''',data)
                        conn.commit()
                        conn.close()

                    except sqlite3.Error as e:
                        print('Failed to insert : ',e)
                    finally :
                        if conn :
                            conn.close()
                    print("Change complete")
                    x = str(input("Do you want to change another one ?(y/n : )"))
            else :
            #สลีปสินค้า
                receipt=str(input("Would you like to print a receipt ? (y/n) : "))
                if receipt == "y":
                    print("\n----------SmileIT----------\n","="*32)
                    print("\n----------All Product----------\n","="*32)
                    print("No---Product Name---Price---Num--\n","="*32)

                    import sqlite3
                    conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
                    c = conn.cursor()
                    c.execute('select * from Basket where Num != 0')
                    result = c.fetchall()
                    for x in result :
                        print(x)
                    conn.commit()
                    c.close()

                    z = 1
                    y = 1
                    allsum = 0
                    sum = 0
                    while z <=16 :
                        import sqlite3
                        conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
                        c = conn.cursor()
                        data = y,
                        c.execute('select Num from Basket where No =?',data)
                        result = c.fetchall()
                        for x in result :
                            a = x[0]
                        data = y,
                        c.execute('select Price from Basket where No =?',data)
                        result = c.fetchall()
                        for x in result :
                            b = x[0]
                        sum = int(a)*int(b)
                        allsum = allsum + sum
                        z = z+1
                        y = y+1
                        conn.commit()
                        c.close()
                    print("*"*32,"\nTotal product price : ",allsum,)
                    print("\n=====Create receipt complete=====\n")
                    #เลือกวิธีการชำระเงิน
                    payment=str(input("\nPlease select a payment method\n \n\tCash on Delivery [1] \n\tBank transfer [2] \n \t: "))
                    if payment == "1":
                        location = str(input("plese enter your location : "))
                        phone = str(input("plese enter your phone number : "))
                        print("-----Please wait to pick up the parcel.-----")
                        print("Thank you for using the service >_< ")
                    else:
                        pay=input("plese enter amount to be paid : ")
                        location = str(input("plese enter your location : "))
                        phone = str(input("plese enter your phone number : "))
                        print("-----Please wait to pick up the parcel.-----")
                        print("Thank you for using the service >_< ") 

                    #รีค่าในตะกร้า
                    import sqlite3
                    conn = sqlite3.connect(r"D:\Gatchaiyo_python\project.db")
                    c = conn.cursor()
                    try :
                        c.execute('UPDATE Basket SET Num = 0')
                        conn.commit()
                        conn.close()
                    except sqlite3.Error as e:
                        print('Failed to insert : ',e)
                    finally :
                        if conn :
                            conn.close()
                else:
                    print("Return to program")
        #ช็อยเมนู    
        while True:
            Menu()
            if choice == "1":
                show()
            elif choice =="2":
                Pick()
            elif choice == "3":
                showbk()
            elif choice == "4":
                q = str(input("Do you want to quit program ? (y/n) : "))
                if q =="y":
                    print("Exit the program.")
                    return
                else:
                    print("Return to program")
            else:
                return
    else:
        print("error")
#ช็อยสเตตัส
while True:
    Status()
    if choice == "n":
        Register()
    elif choice == "y":
        Login()
    elif choice == "x":
        q = str(input("Do you want to quit program ? (y/n) : "))
        if q =="y":
            print("Exit the program.")
            break
        else:
            print("Return to program")
