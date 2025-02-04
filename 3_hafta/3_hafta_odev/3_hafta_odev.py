### 3.Hafta Odev ###

# Moduller Ve Kutuphaneler

# math kutuphanesini kullanarak bir hesap makinesi olustur.

import math

# dort islem icin hesap makinesi


def toplama(a, b):   # toplama islemi
    return a + b

def cikarma(a, b):   # cikarma islemi
    return a - b

def carpma(a, b):    # carpma islemi
    return a * b

def bolme(a, b):    # bolme islemi
    if b == 0:     # sifira bolerken hata kontrolu
        raise ValueError("sifira bolme hatasi")
    return a / b

def sayial(x):
    while True:
        try:
            return float(input(x))   # sayi sayisal degilse hata kontrolu
        except Exception as e:
            print("lutfen sayisal ifade girin...")

def islemler():
    print("Islemler:")
    print("1: toplama")
    print("2: cikarma")
    print("3: carpma")
    print("4: bolme")

    
def hesapmakinesi():     
    while True:
        
        islemler()
        
        islem = input("yapmak istenen islem (1-4) veya bitirmek icin x girin: ")
            
        if islem == 'x':
            print("Hesap makinesi kapatılıyor...")
            break
    
        try:
            if islem in ['1', '2', '3', '4']:  # islem secme
                    
                sayi1 = sayial("sayi1 girin: ")
                sayi2 = sayial("sayi2 girin: ")
    
                if islem == '1':
                    print(f"Sonuc: {toplama(sayi1, sayi2)}")
                elif islem == '2':
                    print(f"Sonuc: {cikarma(sayi1, sayi2)}")
                elif islem == '3':
                    print(f"Sonuc: {carpma(sayi1, sayi2)}")
                elif islem == '4':
                    print(f"Sonuc: {bolme(sayi1, sayi2)}")
                else:
                    print("gecersiz secim...")
                        
        except ValueError as e:
            print(f"Hata: {e}")
        except Exception as e:
            print(f"Beklenmeyen bir hata oluştu: {e}")
            
    
hesapmakinesi()



# kendi modulunu olustur ve icinde birkac matematiksel fonk. tanimla,daha sonra bu modulu kullan.

import mymodule as me # kendi modulumu import ettim

print(me.aricmeticort(1,2,3,4,5))    # sayilarin aritmetik ort.

print(me.geometricort(1,2,3,4,5))    # sayilarin geometrik ort.






# Hata Yonetimi

# kullanicidan 2 sayi alarak bolme islemi yapan program yaz. Sifira bolme hatalarini onle.

sayi1 = int(input("ilk sayi :"))
sayi2 = int(input("ikinci sayi :"))

def bolme(a,b):
     
    try:
        return a / b
    except ZeroDivisionError :
        print("sifira bolme hatasi")
        return None   # hata durumunda none dondurur.

bolme(sayi1,sayi2)

# kendi ozel hata sinifini olustur (negativenumbererror) ve negatif sayi girildiginde hata firlatan fonksiyon yaz.

from negativenumbererror import  Negativenumbererror  # hata sinifini import etme

def control():
    while True:
        try:
            sayi = int(input("sayi girin:"))
            if sayi < 0 :
                raise Negativenumbererror
            return sayi
        except Negativenumbererror as e: 
            print(e)
       
   
print(control())





# Dosya Yonetimi

# Kullanicin girdigi verileri data.txt dosyasina kaydedip,
# daha sonra dosyadan okuyarak ekrana yazdiran bir program yaziniz.

file = open("C:/Users/berra/OneDrive/Masaüstü/AI Camp Cerebrum/3_hafta/3_hafta_odev/data.txt","a")  # dosya olusturma

file.write(input("bilgi girin:"))

file = open("C:/Users/berra/OneDrive/Masaüstü/AI Camp Cerebrum/3_hafta/3_hafta_odev/data.txt","r") # dosya okuma
content = file.read()
print(content)  # yazdirma


# Bir JSON dosyasi olustur ve icindeki verileri python ile oku,degistir ve tekrar kaydet.

import json

with open("C:/Users/berra/OneDrive/Masaüstü/AI Camp Cerebrum/3_hafta/3_hafta_odev/data.json","r+") as data:
    data = json.load(data) # sozluk gibi yukler

print(data)  # okuma

data["isim"] = "Berra Nur"
data["diller"].append("javascript")
print(data)




# İleri Fonksiyonel Programlama

# map(),filter(),reduce() fonksiyonlarini kullanarak bir liste uzerinde islemler yapan fonksiyonlar yaz.

# map()

from math import pow

sayilar = [1, 2, 3, 4, 5]

karelisayilar = list(map(lambda x:pow(x,2), sayilar))  # map ile karesini al

print(karelisayilar)  


# filter()

from math import factorial

sayilar = [1, 2, 3, 4, 5]

ciftsayilar = list(filter(lambda sayi:sayi % 2 == 0, sayilar))  # filter ile filtrelendi
faktoriyelli = list(map(lambda x:factorial(x), ciftsayilar))  # faktoriyeli alindi
print(faktoriyelli)

# reduce()

from functools import reduce

def carp(a,b):
    return a*b

sayilar = [1, 2, 3, 4, 5]

carpim = reduce(carp,sayilar)   # tum sayilar reduce ile carpildi
print(carpim)



# Lambda fonksiyonlariyla sorted() fonksiyonu kullanarak bir listeyi ozellestirilmis sekilde sirala.

sirasizliste = [87,34,324,1,7,0,3,2,455,77]

siraliliste = list(sorted(sirasizliste))
print(siraliliste)



# Iterator ve Generator Kullanimi

# Kendi iterator sinifini olustur evennumbers ve yanlizca cift sayilar ureten bir iterator yaz.

class evennumbers:   # cift sayi sinifimiz
    def __init__(self,start,stop):
        if start % 2 == 0:   # baslangic cift mi
            self.start = start
        else:
            self.start = start + 1
        self.stop = stop
        
    def __iter__(self):
        return self
    
    def __next__(self):
         if self.start <= self.stop:
            x = self.start
            self.start += 2
            return x 
         else:
             raise StopIteration
             
             
list = evennumbers(3, 21)      # aradaki cift sayilar
myiter  = iter(list)

while True:
    try:
        element = next(myiter)
        print(element)
    except StopIteration:
        break

# Fibonacci serisi ureten bir generator yaz ve ilk 10 sayiyi yazdir.

def Fibonacci():
    a,b = 0,1 
    while True:
        yield a+b  # yer kaplamamak icin
        a,b = b,a+b    
        
generator = Fibonacci()

for i in range(10):  # ilk on sayi
    print(next(generator))































































