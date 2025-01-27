### Fonksiyonlar ###

# method: Cesitli gorevleri yerine getiren fonksiyon benzeri yapilardir.

""" 
- Class yapisi icerisinde tanimlanan fonksiyonlar 
- Metotlar nesneler uzerinden cagrilir.
- Metotlar parametre alabilirler.
- Metotlar sadece kullanici tarafindan olusturulur.
"""

# fonksiyon: Cesitli gorevleri yerine getiren yapilardir.

"""
- Fonksiyon olusturmak icin def (definition) anahtar sozcugu kullanilir.
- Class yapisi icerisinde tanimlanmamistir.
- Class icerisinde tanimli olmadıgı icin bagimsizdir.
- Fonksiyonlar adlari ile cagrilir.
- Fonksiyonlar parametre alabilir ve aldiklari parametreleri islevlerinde kullanabilir.
"""

# Fonksiyon Kullanimi



Sayi1 = int(input("Ilk sayi :"))
Sayi2 = int(input("Ikinci sayi :"))

def Toplama (num1,num2):
    return  num1 + num2
    
    
print(Toplama(Sayi1,Sayi2))


# Fonksiyon Parametreleri

# bunun yerine
def Toplama (num1,num2,num3=0):        #parametre sayisi degisirse
    return  num1 + num2 + num3

# bu daha kullanisli
def Toplama (*params):
    Toplam = 0
    for n in params:
        Toplam += n
    return Toplam

print(Toplama(10,21,55,66))

# Uygulama

# Gönderilen bir kelimeyi belirtilen kez ekranda gosteren fonksiyonu yazin.

def Tekrarla(TekrarSayi,*kelime):
    for item in range(TekrarSayi):
        print(*kelime)


Tekrar = int(input("tekrar sayisi: "))
Metin = input("metin gir: ")    

Tekrarla(Tekrar,Metin)

# Lambda Experssions

# map 

def Karesi(num): return num**2

Numbers = [1,3,5,9]

Result = list(map(Karesi,Numbers))   # her elemanin dolasilmasi

print(Result)

# lambda

NumbersC = [2,4,6,8]

Result = list(map(lambda num:num**2,NumbersC)) 

print(Result)


# Fonksiyon Kapsami

Degisken = "Globalim"

def MyFunc():
    Degisken = "Localim"     # fonksiyondaa varsa onu kullanilir.
    print(Degisken)
MyFunc()
print(Degisken)


Degisken2 = "Globalim"

def MyFunc2():
    # Degisken2 = "Localim"     # yoksa globali kullanilir
    print(Degisken2)
MyFunc2()
print(Degisken2)


# Bankamatik

HesapA = {"ad:":"Berra",
         "HesapNo":"12345",
         "bakiye:":3000,
         "ekhesap:":200}

HesapB = {"ad:":"Enes",
         "HesapNo":"65432",
         "bakiye:":2000,
         "ekhesap:":5000}


def ParaCek(Hesap,miktar):
    
    ToplamHesap = Hesap["bakiye:"] + Hesap["ekhesap:"]
    print("merhaba {n}".format(n = Hesap["ad:"]))
    if Hesap["bakiye:"] >= miktar:
        print("para veriliyor...")
    else:
        EkKontrol = input("Ek hesap kullanilsin mi: E/H")
        
        if (EkKontrol) == "E":
            if(ToplamHesap) >= miktar :
                print("ekhesaptan veriliyor...")
            
            else:
                print("bakiye yetersiz...")
        else:
            print("islem iptal.")
            
ParaCek(HesapA,3100)










