### Fonksiyonlarin İleri Seviye Ozellikleri ###

# İc İce Fonsiyon Kullanimi

def outer(num1):
    print("outer calisti...")
    
    def azalt(num1):
        print("inner calisti...")
        return num1+1
    
    num2 = azalt(num1)
    print(num1,num2)
    
outer(6)



# faktoriyel alma

def factorial(number):
    
    def inner_fac(number):
        if number <= 1:
            return 1  
        return number  * inner_fac(number - 1 )
    
    return inner_fac(number)

factorial(5)


# Fonksiyondan Fonksiyon Dondurme

def islem(islemadi):
    
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    
    if islemadi == "toplama":
        return toplama 
    else:
        return carpma

toplama = islem("toplama")
print(toplama(2,3,4,5,67,7))

carpma = islem("carpma")
print(carpma(1,2,3,4,5))

# Fonksiyona Fonksiyonu Parametre Gonderme

def bolme(a,b):
    return a / b

def islem(fonk1,a,b):  # bolme fonk parametre olarak gonderildi.
    print(fonk1(a,b))
    
    
islem(bolme,8,2)

# Decorator Fonksiyonlar

# Bir fonksiyona bir ozellik ekleme
import math
import time

# decorator kullanmadan

def usalma(a,b):
    start = time.time()
    time.sleep(1)
    print(math.pow(a,b))
    finish = time.time()
    print("fonksiyon "+ str(finish-start)+ " saniye surdu.")

usalma(4, 2)


def faktoriyel(a):
    start = time.time()
    time.sleep(1)
    print(math.factorial(a))
    finish = time.time()
    print("fonksiyon "+ str(finish-start)+ " saniye surdu.")

faktoriyel(4)



# decarator kullanarak

def calculatetime(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)  # esnek yapi
        finish = time.time()
        print("fonksiyon "+ func.__name__ + str(finish-start)+ " saniye surdu.")
    return inner

@calculatetime 
def usalma(a,b):
    print(math.pow(a, b))
    
@calculatetime 
def faktoriyel(a):
    print(math.factorial(a))    

usalma(4, 2)

































