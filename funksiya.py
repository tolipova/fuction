# import time
# def f(a,b,c):
#     natija = a * b + c
#     return natija
# hisob = f (4,8,2)
# print(hisob)

# time.sleep(5)

# def h ():
#     print("matematik misol")
# h()    

import time
color=['red','yellow','green']
while True :
    a = input("svetaforning rangini kursating: ")
    if a == 'red' :
        print("Qizil rang yondi va 20sekund kuting:")  
        # time.sleep(20)
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('4')
        time.sleep(1)
        print('5')
        time.sleep(1)
        print('6')
        time.sleep(1)
        print('7')
        time.sleep(1)
        print('8')
        time.sleep(1)
        print('9')
        time.sleep(1)
        print('10')
        time.sleep(1)
        print('11')
        time.sleep(1)
        print('12')
        time.sleep(1)
        print('13')
        time.sleep(1)
        print('14')
        time.sleep(1)
        print('15')
        time.sleep(1)
        print('16')
        time.sleep(1)
        print('17')
        time.sleep(1)
        print('18')
        time.sleep(1)
        print('19')
        time.sleep(1)
        print('20')
        break
for a in color:
    print("Sz sariq ranga tushdiz")
    if a == 'yellow':
        print("Sariq rang yondi va 5sekund kutib yurishni boshlang: ")
        time.sleep(5)
        print(1)
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('4')
        time.sleep(1)
        print('5')
        time.sleep(1)
        print('Yurish mumkin')
        print("Siz yashil rangdasz kutish shart emas")  
        continue  
    else:
        print('Boshqa xatolik bor')



def oylik_maosh(ishchi_soni,soat,s_maosh) :
    return  ishchi_soni * soat * soatlik_maosh
while True :
    ishchi_soni = int(input('Ishchilar sonini kiriting: '))
    soat = float(input("ish soati: "))
    soatlik_maosh =float(input("har bir ishchining maoshini kiriting: "))

    maosh=oylik_maosh(ishchi_soni,soat,soatlik_maosh)
    print(f"Ishchilar oylik maoshi: {maosh}so'm")
    yana=inout("yana davom etish ha/yoq")
    if yana.lower() != 'ha':
        break
    else:
        print("xatolik bot")
