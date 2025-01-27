### Donguler ###

# Dizi icinde dolasmak

## For

Numbers = [1,2,3,4,5,6]

for Number in Numbers:
    print(Number)
    
Names = ["Berra","Nur","Sena","Enes"]

for Name in Names:
    print(' my name is {n} '.format(n=Name))

Children = {"Berra":22,"Nur":21,"Sena":27,"Enes":25}

for ChildKey,ChildValue in Children.items():
    print(ChildKey + "***"+ str(ChildValue))
    
    
    
    
# Uygulama

Sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayilar 3'un katidir ?

for Sayi in Sayilar:
    if(Sayi % 3 == 0):
        print(Sayi)

# 2- Sayilar listesinde sayilarin toplami kactir ?

Toplam = 0

for Sayi in Sayilar:
    Toplam += Sayi

print("Toplam: \n" , Toplam)

# 3- Sayilar listesindeki tek sayilarin karesini aliniz.

print("Tek sayilarin karesi : " )
for Sayi in Sayilar:
    if(Sayi % 2 != 0):
        print(Sayi ** 2)
        
        

Sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']

# 4- Sehirlerden hangileri en fazla 5 karakterlidir ?

print("Sehirler :")
for Sehir in Sehirler:
    if(len(Sehir) <= 5):
        print(Sehir)


Urunler = [
{'name': 'samsung S6', 'price': 3000 },
{'name':'samsung S7', 'price': 4000 },
{'name':'samsung S8', 'price': 5000 },
{'name':'samsung S9', 'price':6000 },
{'name':'samsung S10', 'price':7000 }
]

# 5- Urunlerin fiyatlari toplami nedir ?

Toplam = 0

for Urun in Urunler:
    Fiyat = Urun["price"]
    Toplam  += Fiyat
    
print("Toplam : " + str(Toplam))
    
# 6- Urunlerden fiyati en fazla 5000 olan urunleri gosteriniz 

print("Urunler: ")
for Urun in Urunler:
    if(Urun["price"] <= 5000):
        print(Urun["name"])





## While

x = 1

while(x < 100):
    print(str(x) + ".nci sayi")
    x +=  1

# Uygulama

SayilarArr = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdirin.

x = 0

while (x < len(SayilarArr)):
    print(SayilarArr[x])
    x += 1

# 2: Baslangic ve bitis degerlerini kullanicidan alip aradaki tum tek sayilari ekrana yazdirin.

Baslangic = int(input("Baslangic degeri : "))
Bitis = int(input("Bitis degeri : "))

TekSayi = Baslangic

while TekSayi < Bitis :
    if(TekSayi % 2 != 0):
        print(TekSayi)
        TekSayi += 2
     
# 3: 1-100 arasindaki sayilari azalan sekilde yazdirin.

y = 100
while y >= 1 :
    print(y)
    y -= 1






## Break ve Continue

BreakTxt = "my name is berranur"

for letter in BreakTxt:
    if letter == 'r':
        break
    print(letter)

for letter in BreakTxt:
    if letter == 'a':
        continue
    print(letter)

# Uygulama

# 1-100 e kadar tek sayilarin toplami

TekToplam = 0

z = 1
while (z <= 100):
    z += 1
    if z % 2 == 1:
       continue
    TekToplam += z
    
print(TekToplam)





## Dongu Metodlari

# range()

for item in range(10):       # 0 -10 a kadar sayilari yazar.
    print(item)


for item in range(5,25,3):       # range(baslangic,bitis,artis)
    print(item)

# enumerate

Greeting = "hello python"

for index,letter in enumerate(Greeting):
    print(f"index: {index} letter : {letter}" )


# zip

List1 = [1,2,3,4,5]
List2 = ["a","b","c","d","e"]

print(list(zip(List1,List2)))


## List Comprehensions

ListComp = [x for x in range(10)]
print(ListComp)

ListComp3 = [x for x in range(10) if x%3==0]
print(ListComp3)


# Uygulama

# 1-100 arasinda rastgele uretilecek bir sayiyi asagı yukari ifadeleri ile buldurmaya calisin.

import numpy as np

Target = np.random.randint(1,100,1)




for item in range(1,100,1):
    Guess = int(input("Tahmin giriniz: "))
    if Target < Guess:
        print("Tahmininizi kucultun. ")
    elif( Target > Guess):
        print("Tahmininizi buyultun. ")
    else:
        print("sayi bulundu. ")
        break













