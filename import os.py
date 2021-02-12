'''import os
choice = 0
filename = ''

def menu():
    global choice 
    print('Menu\n 1.Open Calculator\n 2.Open Notepad\n 3.Exit ')
    choice = input('Select Menu : ')

def opennotepad():
    filename = 'C:\\Windows\\system32\\notepad.exe'
    print('Memorandum writing %s'%filename)
    os.system(filename)

def opencalculator():
    filename = 'C:\\Windows\\System32\\calc.exe'
    print('Calculate Number %s'%filename)
    os.system(filename)

while True:
    menu()
    if choice == '1':
        opencalculator()
    elif choice == '2':
        opennotepad()
    else:
        break'''
    

'''choice = 0
i=1
lt=[0,0,0,0,0]
def menu():
    global choice 
    print('โปรแกรมร้านค้า\n 1.แสดงรายการสินค้า\n 2.หยิบสินค้าใส่ตะกร้า\n 3.แสดงจำนวนและราคาของสินค้าที่หยิบ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม\n')
    choice = input('Select Menu : ')
def openproduct():
    print('รายการสินค้า\n 1.ยาดม ราคา 15 บาท\n 2.น้ำเป่ลา ราคา 10 บาท\n 3.มาม่า ราคา 6 บาท\n 4.สบู่ ราคา 30 บาท\n 5.แปรงสีฟัน ราคา 25 บาท\n')

def puss():
    print('กรุณาเลือกรายการสินค้า\n 1.ยาดม ราคา 15 บาท\n 2.น้ำเป่ลา ราคา 10 บาท\n 3.มาม่า ราคา 6 บาท\n 4.สบู่ ราคา 30 บาท\n 5.แปรงสีฟัน ราคา 25 บาท\n 6.สิ้นสุดการเลือก')
    while(i>0):
        a=int(input("เลือกสินค้าหมายเลข :"))
        if a==1:
            lt[0] +=1
        elif a==2:
            lt[1] +=1
        elif a==3:
            lt[2] +=1
        elif a==4:
            lt[3] +=1
        elif a==5:
            lt[4] +=1
        elif a==6:
            break
def show():
    print("สินค้าของคุณมีดังนี้")
    print('สินค้า..........จำนวน............ราคา')
    print('1.ยาดม.......',lt[0],'.....',lt[0]*15,'.....')
    print('2.น้ำเป่ลา......',lt[1],'.....',lt[1]*10,'....')
    print('3.มาม่า........',lt[2],'.....',lt[2]*6,'....')
    print('4.สบู่..........',lt[3],'.....',lt[3]*30,'....')
    print('5.แปรงสีฟัน....',lt[4],'.....',lt[4]*25,'....')

def delete():
    print('กรุณาเลือกรายการสินค้า\n 1.ยาดม ราคา 15 บาท\n 2.น้ำเป่ลา ราคา 10 บาท\n 3.มาม่า ราคา 6 บาท\n 4.สบู่ ราคา 30 บาท\n 5.แปรงสีฟัน ราคา 25 บาท\n 6.สิ้นสุดการเลือก')
    while(i>0):
        a=int(input("เลือกสินค้าหมายเลข :"))
        if a==1:
            lt[0] -=1
        elif a==2:
            lt[1] -=1
        elif a==3:
            lt[2] -=1
        elif a==4:
            lt[3] -=1
        elif a==5:
            lt[4] -=1
        elif a==6:
            break

while True:
    menu()
    if choice == '1':
        openproduct()
    elif choice == '2':
        puss()
    elif choice == '3':
        show()
    elif choice == '4':
        delete()
    else : 
        break'''

'''choice=0        
dictionary=[]
par=[]
word=[]
def menu():
    global choice 
    print('พจนานุกรม\n 1.เพิ่มคำศัพท์\n 2.แสดงคำศัพท์\n 3.ลบคำศัพท์\n 4.ออกจากโปรแกรม\n')
    choice = input('Select Menu : ')

def puss():
    dictionary.insert(0,input('เพิ่มคำศัพท์'))
    par.insert(0,input('ชนิดคำศัพท์(n. v. adj. adv. :)'))
    word.insert(0,input("ความหมาย"))
    print("เพิ่มคำศัพท์เรียนร้อยเเล้ว")

def show():
    print("คำศัพท์ของคุณมีดังนี้",len(dictionary))
    print('คำศัพท์.....ประเภท......ความหมาย')
    x=0
    while x<len(dictionary):
        print(dictionary[x],' ',par[x],' ',word[x])
        x=x+1
def delete():
    x=str(input("พิมพ์คำศัพท์ที่ต้องการลบ :"))
    z=0
    while z<len(dictionary):
        if x== dictionary[z]:
            del par[z]
            del word[z]
        z=z+1
    dictionary.remove(x)

while True:
    menu()
    if choice == '1':
        puss()
    elif choice == '2':
        show()
    elif choice == '3':
        delete()
    else:
        break'''

#แบบฝึกหัดที่4.3 ยิงปืน
import time
def wela():
    vantee = time.localtime()
    d1 = time.strftime("%d %B %Y, %H:%M:%S", vantee)
    print(d1)
NAME = []
SC = []
TT = []
HIT = []
num = int(input("Plese Enter Num of Compettitor : "))
for i in range(num):
    name = input("Plese Enter Compettitor Name : ")
    pts = float(input("Enter PTS Score : "))
    tim = float(input("Enter Time : "))
    NAME.append(name)
    SC.append(pts)
    TT.append(tim)
    HIT.append(pts/tim)
for i in range(num):
    j = i
    for j in range(num):
        if HIT[i] > HIT[j]:
            z,x,c,v = HIT[i],SC[i],TT[i],NAME[i]
            HIT[i],SC[i],TT[i],NAME[i] = HIT[j],SC[j],TT[j],NAME[j]
            HIT[j],SC[j],TT[j],NAME[j] = z,x,c,v
vantee = time.localtime()
a = time.strftime("%A", vantee)
b = time.strftime("%Y", vantee)
print("Shortgun "+a+"Training",b,"\nCondition : 1")
wela()
print("_"*100)
print("{0:-<6}{1:-<6}{2:-<8}{3:-<17}{4:-<12}{5:-<15}{6}".format("NO.","PTS","TIME","COMPETITOR#Name","HIT FACTOR","STATE POINTS","STATE PERCENT"))
print("_"*100)
for i in range(num):
    PO = (HIT[i]/HIT[0])*50
    PE = (PO/(HIT[0]/HIT[0]*50))*100
    print("{0:_<6}{1:_<6}{2:_<8}{3:_<17}{4:_<12}{5:_<15}{6}".format(i+1,int(SC[i]),"%.2f"%TT[i],NAME[i],"%.4f"%HIT[i],"%.4f"%PO,"%.2f"%PE))

    