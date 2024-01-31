##1



#try:
#    a=int(input("sisesta arv"))
#    if 1<=a<=9:
#        for i in range (a):
#            print("   /V\       " , end=" ")
#        print()
#        for i in range (a):
#            print("  / V \      " , end=" ")
#        print()
#        for i in range (a):
#            print(" / V V \     " , end=" ")
#        print()
#        for i in range (a):
#            print("/VV V VV\    " , end=" ")
#        print()
#    else:("uuesti")
#except ValueError:
#    print("uuesti")
##2


#try:
#    a= int(input("sisestaarv"))
#    b=1
#    for i in range(a+1):
#        if i%2!=0:
#            b*=i
#    print("Resultat", b)
#except ValueError:
#    print("uuesti")
#5



#a=int(input("press num1:"))
#b=int(input("press num2:"))
#total=0
#current= a
#while True:
#    try:
#        total+= current
#        current+=1
#        if current>b:
#            break
#    except ValueError:
#        print("gogogogogogo")
#print("sum {} do {}: {}".format(a,b, total))
##3



#import random
#a=random.randint(1,10)
#b=0
#for i in range(a):
#    if random.randint(-10,10)>0:
#        b+=1
#print(f"kokku random arvud: {a}")
#print(f"koli4estvo polozitelnih arvud: {b}")
##4

#number=int(input("pick a number"))
#count=0
#counter=0
#while number> 0:
#    digit=number%10
#    if digit%2==0:
#        count+=1
#    else:
#        counter+=1
#    number//=10
#print("count ", count)
#print("counter ", counter)

#print("*** ИГРЫ С ЧИСЛАМИ ***")
#print()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#while 1:
#    try:
#        a = abs(int(input("Введите целое число => ")))
#        break
#    except ValueError:
#         print("Это не целое число")
##'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#if a==0:
#    print("Нет смысла ничего делать с нулём")
#else:
##'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
#    print()
#    c=a
#    b=a
#    paaris = 0
#    paaritu = 0
#    while b > 0:
#        if b % 2 == 0:
#            paaris += 1
#        else:
#            paaritu += 1
#        b = b // 10
    
#    print("Чётных цифр:"+str(paaris))
#    print("Нечётных цифр:"+str(paaritu))
#    print()
##''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#    print("*Переворачиваем* введённое число")
#    print()
#    b=0
#    while a > 0:
#        number = a % 10
#        a = a // 10
#        b = b * 10
#        b += number
#    print("*Перевёрнутое* число", b)
#    print()
##''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#    print("Проверяем гипотезу Сиракуз")
#    print()
#    if c % 2 == 0:
#        print(f"{c} - чётное число. Делим на 2.")
#    else:
#        print(f"{c} - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
#    while c != 1:
#            if c % 2 == 0:
#                    c = c / 2
#            else:
#                    c = (3*c + 1) / 2
#            print(int(c) ,end=" ")
#    print()
#    print("Гипотеза верна")