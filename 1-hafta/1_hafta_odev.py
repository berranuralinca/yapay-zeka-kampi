### 1.Hafta Odev ###

# İlk Python Uygulamaniz:
    
# Python’da “Merhaba Yapay Zeka!” yazan bir program yazin.

print("Merhaba Yapay Zeka!")

# Kullanicinin adini soran ve “Merhaba, [isim]! Python ogrenmeye hos
# geldin.” mesajini veren bir program gelistirin.

KullaniciAdi = input("Isminiz: ")

print("Merhaba,{n} ! Python ogrenmeye hos geldin. ".format(n=KullaniciAdi))



# Degiskenler ve Veri Tipleri Uygulamasi:

# Farkli veri tiplerinde (string, integer, float, boolean) degiskenler tanimlayin
# ve bu degiskenlerle islemler yaparak ciktilari gozlemleyin.

UserName = "Berra"      # string
UserAge = 22            # integer
UserWeight = 54.6       # float
UserSex = True          # boolean true == kadın

if UserSex == True:
    print("My name is {name}.I am {age} and my weight is {w}.I am a woman.".format(name=UserName,age=UserAge,w=UserWeight ))
else:
    print("My name is {name}.I am {age} and my weight is {w}.I am a man.".format(name=UserName,age=UserAge,w=UserWeight))

# Kullanicidan iki sayi alarak bu sayilarin toplamini, farkini ve carpimini
# hesaplayan bir program yazin.

Sayi1 = int(input("ilk sayi: "))
Sayi2 = int(input("ikinci sayi: "))

print("toplam: " + str(Sayi1 + Sayi2) )
print("fark: " + str(Sayi1 - Sayi2) )
print("carpim: " + str(Sayi1 * Sayi2) )

# Farkli degisken turlerini birbirine donusturmeyi deneyin ( En az iki tane )

Number = int("12")
print(Number)
Text = str(11) + str(345)
print(Text)



# String İslemleri ve Listeler:
    
# Kullanicinin girdigi bir cumlenin tum harflerini buyuk yaparak ekrana yazdirin.

Experision = input("Cumle giriniz: ")
Experision = Experision.upper()
print(Experision)

# Bir alisveris listesi (ornegin: meyve isimleri) olusturarak, listeye yeni urunler ekleyin, bir urunu silin ve listeyi ekrana yazdirin.

ShopList =  ["2 Bread","Tomato","Milk","Oil"]
ShopList.append("Ginger")
ShopList.append("Banana")
ShopList.pop(0)
print(ShopList)



# Kosul Ifadeleri:
    

# Kullanicidan yasini isteyin. Yası 18’den buyukse “Ehliyet alabilirsiniz.”,
# kucukse “Ehliyet almak icin yasiniz tutmuyor.” seklinde mesaj veren bir
# program yazin.


DriverAge = int(input("Yas: "))

if (DriverAge > 18):
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet almak icin yasiniz tutmuyor.")

# Bir sayi tahmin oyunu olusturun:
# Kullanicidan 1-10 arasinda bir sayi tahmin etmesini isteyin ve dogru tahmin edip etmedigini kontrol edin.

KeepNumber = 6

GuessNumber = int(input("1-10 arasi sayi girin: "))

if KeepNumber == GuessNumber:
    print("sayiyi buldunuz...")
else:
    print("tekrar deneyin...")

"""

    Basit bir Amiral Batti oyunu tasarlayin. Asagidaki adimlari takip ederek
    oyunu gelistirin:
        
        1. Oyun Kurallari:
        - Oyun 5x5 bir tahtada oynanacaktir.
        - Bilgisayar, gizli bir sekilde bir kareye gemi yerlestirecektir. (ornegin (3,2) koordinatina)
        - Kullanici, geminin oldugu kareyi tahmin etmeye calısacaktir.
        
        2. Oyun Akisi:
        - Kullanicidan bir sira (1-5 arasi) ve bir sutun (1-5 arasi) girmesini isteyin.
        - Kullanicinin tahmini dogruysa “Tebrikler, gemiyi vurdunuz!” mesajı verin.
        - Yanlıssa “Yanlıs tahmin, tekrar dene!” mesajı verin ve kullanicinin yeni bir giriş yapmasina izin verin.
        
        
        Ekstra Özellikler:
        - Kullanicinin 5 tahmin hakki olsun. Dogru tahmin yapamazsa oyun sona ersin ve geminin yeri acıklansin.
        - Kullaniciya her yanlis tahmin sonrasi kac hakkinin kaldigini bildirin.
        - 0Daha zor bir seviyede 2 farkli gemi koyun ve ikisinin de yerini bulana kadar oyunu devam ettirin.

"""
"""
GameArea = 5
print("Oyun basliyor...Seviye 1: ")
print(f"Oyun {5}x{5} den olusmaktadir.")

Target = {"Row":4,"Column":5}

i=1
while i <= 5:
    CoordinateRow = int(input("satir girin: "))
    CoordinateColumn = int(input("sutun girin: "))
    
    if Target["Row"] == CoordinateRow:
        if Target["Column"] == CoordinateColumn:
            print("Tebrikler, gemiyi vurdunuz!")
            break
        else:
            print("satir dogru...Tekrar dene")
            print(str(5 - i ) + "hakkiniz kaldi.")
            i += 1
    else:
        if  Target["Column"] == CoordinateColumn:
            print("Satir yanlis,sutun dogru...")
            print(str(5 - i ) + "hakkiniz kaldi.")
            i += 1 
        else:
            print("ikisi de yanlis...")
            print(str(5 - i ) + "hakkiniz kaldi.")
            i += 1

print("sayiyi bulamadin...Hedef " + Target["Row"] + Target["Column"])
"""

# 2 gemi

GameArea = 5
print("Oyun basliyor...Seviye 2: ")
print(f"Oyun {5}x{5} den olusmaktadir.")

Target1 = {"Row":4,"Column":5}
Target2 = {"Row":3,"Column":3}


i=1
while i <= 5 and not( Target1 is None and Target2 is None):
    CoordinateRow = int(input(" satir girin: "))
    CoordinateColumn = int(input(" sutun girin: "))
    
    # 1. Gemi kontrolu
    if Target1 and Target1["Row"] == CoordinateRow and Target1["Column"] == CoordinateColumn :
        print("Tebrikler, 1.gemiyi vurdunuz!")
        Target1 = None  # Gemi vuruldugunda hedef gecersiz hale getirilir.
    
    # 2. Gemi kontrolü
    elif Target2 and Target2["Row"] == CoordinateRow and Target2["Column"] ==  CoordinateColumn:
            print("Tebrikler, 2.gemiyi vurdunuz!")
            Target2 = None  # Gemi vuruldugunda hedef gecersiz hale getirilir.
    
    else:
        print("Hedefi kacirdin.")
    
    i += 1


if Target1 is None and Target2 is None:
    print("Her iki gemiyi de vurdunuz! Tebrikler!")
else:
    print("Oyunu kaybettiniz.")
    if Target1 is not None:
        print("1. Geminin koordinatları:", Target1["Row"], Target1["Column"])
    if Target2 is not None:
        print("2. Geminin koordinatları:", Target2["Row"],Target2["Column"])










