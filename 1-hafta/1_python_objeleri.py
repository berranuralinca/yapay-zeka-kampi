### Operatorler ###

"""
toplama +
cikarma - 
bolme /
carpma *
us alma **
"""





# Uygulama

CalisanMaas = 5000
Vergi = 0.27
print( CalisanMaas - ( CalisanMaas * Vergi ))






### Degisken Tanimlama Kurallari ###

# rakam ile baslayamaz

number1 = 22
print(number1)

# hatali 1number

# buyuk kucuk harfe duyarlı

sayi1 = 10
Sayi1 = 20
print(sayi1)
print(Sayi1)

## tek satirda tanimlama
sayi1,Sayi1 = (10,20)

# turkce karakter kullanma

# hatali sayi1=10

# string toplama
FirstName = "Berra"
LastName = "Alinca"
print( FirstName + LastName )



# Uygulama

"""
1- Bir musterinin asagidaki bilgileri icin degisken olusturunuz.

Musteri adi
Musteri soyadi
Musteri ad + soyad
Musteri cinsiyet
Musteri tc kimlik
Musteri dogum yili
Musteri adres bilgisi
Musteri yasi

"""

CurrentYear = 2025
UserName = "Berra Nur"
UserLastName = "Alinca"
UserNameLastname = UserName + UserLastName
UserSex = True    # Female
UserNumber = 12345678912
UserDate = 2003
UserAdress = "abcd st."
UserAge = CurrentYear - UserDate





### Type Conversion ###

GirilenSayi1 = input("1.sayi: ")
GirilenSayi2 = input("2.sayi: ")

# string birlestirme Toplam = GirilenSayi1 + GirilenSayi2
Toplam = int(GirilenSayi1) + int(GirilenSayi2)

print(Toplam)


# int to float
x = 33
x = float(x)
print(x)

# Uygulama

"""

Daire Alani : pi * r ** 2
Daire Cevresi : 2 * pi * r
* Yari capi verilen bir dairenin alan ve cevresini
hesaplayiniz. (: 3.14)

"""

YariCap = float( input("yaricapi giriniz: "))
pi = 3.14
DaireAlani = pi * (YariCap ** 2)
DaireCevresi = 2 * pi * YariCap

print("Daire Alani :" + str( DaireAlani ))
print("Daire cevresi:" + str( DaireCevresi ))






### String ###

UserName = "Berra Nur"
UserLastName = "Alinca"
UserAge = CurrentYear - UserDate

Meeting = "My name is " + UserName + " " + UserLastName + " and I am " + str(UserAge)

print(Meeting)
print(Meeting[4])          # string dizisi
print(len(Meeting))        # dizi uzunlugu 
print(Meeting[2:30:2])     # ikiÅŸer ikiÅŸer alÄ±r




### Format ###


print("My name is {} {}".format(UserName,UserLastName) )
print("My name is {1} {0}".format(UserName,UserLastName) )
 
Result = 200/22
print("the result is {r:1.4}".format(r=Result) )    #r:virgulden once , virgulden sonra



### String Metodlari ###

Message = "Hello.My name is July"
Message = Message.upper()
Message = Message.lower()
Message = Message.title()
Message = Message.capitalize()
Message = Message.strip()        #icindeki ifadeleri keser
Message = Message.split()        #icindekine gore ayarlar.
Message = " ".join(Message)      #karaktere gore birlestirir
print(Message)

Arananİndex = Message.find("July")
print(Arananİndex)

Baslangic = Message.startswith("H")
print(Baslangic)

Bitis = Message.endswith("x")
print(Bitis)

Degistir = Message.replace("July", "Berra")
print(Degistir)




### List ###

MyList = [ 1,2,3 ]
MyList2 = [ "one",2,"three"]
print(MyList2[2])
 
MyList3 = [ MyList , MyList2 ]
print(MyList3)
print(MyList3[0][1])



# Uygulama


# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarina sahip bir liste olusturunuz.
Cars = [ "BMW","Mercedes","Opel","Mazda" ]

# 2- Liste Kac elemanlidir ?
print(len(Cars))
 
# 3- Listenin ilk ve son elemani nedir ?
print("ilk eleman:" + Cars[0])
print("son eleman:" + Cars[3])
 
# 4- Mazda degerini Toyota ile degistirin.
Cars[3] = "Toyota"
print(Cars)
 
# 5- Mercedes listenin bir elemani midir ?
isFound = "Mercedes" in Cars
print(isFound)
 
# 6- Listenin -2 indeksindeki deger nedir?
print(Cars[-2])
 
# 7- Listenin ilk 3 elemanini alin.
print(Cars[0:3])
 
# 8- Asagidaki verileri bir liste icinde saklayiniz.
StudentA = ["YiÄŸit Bilgi", 2010, [70,60,70]]
StudentB = ["Sena Turan ",1999, [80,80,70]]
StudentC = ["Ahmet Turan",1998, [80,70,90]]
Students = [StudentA,StudentB,StudentC]

# 9- Liste elemanlarini ekrana yazdiriniz
print(Students)


### Liste Metodlari ###

Numbers = [1,324,243,4454,65,214,4]
Letters = ["a","j","d","e","b"]
print(min(Numbers))
print(min(Letters))
print(max(Numbers))
Numbers.append(5)
Numbers.insert(1,2)
Numbers.pop()
Numbers.sort()
Numbers.reverse()
print(Numbers)




# Uygulama

Names = ['Ali', 'YaÄŸmur', 'Hakan', 'Deniz']
Years = [1998, 2000, 1998, 1987]

# "Cenk" ismini listenin sonuna ekleyiniz.
Names.append("Cenk")
# "Sena" degerini listenin basina ekleyiniz.
Names.insert(0,"Sena")
#  "Deniz" ismini listeden siliniz.
Names.remove("Deniz")
#  "Ali" listenin bir elemani midir?
Names.index("Ali")
# Liste elemanlarini ters cevirin.
Names.reverse()
# Liste elemanlarini alfabetik olarak siralayiniz.
Names.sort()
# years listesini rakamsal buyukluge gore siralayiniz..
Years.sort()





### Tuple ###

NameTuple = ("damla","deniz")
# NameTuple[0] = "ahmet" yapilamaz

### Dictionary ###

CityDic = { 'Bolu': 14 ,'Istanbul': 34}
print(CityDic["Bolu"])





# Uygulama
"""
Ogrenciler = {

'120': 
{
'ad': 'Ali',
'soyad': 'Yilmaz',
'telefon': '532 000 00 01'
},

'125': 
{
'ad': 'Can',
'soyad': 'Korkmaz',
'telefon': '532 000 00 02'
},

'128':
{
'ad': 'Volkan',
'soyad': 'Yukselen',
'telefon': '532 000 00 03'
}
}
"""

# Bilgileri verilen ogrencileri kullanicidan aldiginiz bilgilerle dictionary icinde saklayiniz.
   
Ogrenciler = {}
NumberS1 = input("Numara girin:")
NameS1 = input("Isim:")
SurnameS1 = input("Soyisim:")
TelS1 = input("Telefon numarasi:")
Ogrenciler[NumberS1] = {NameS1,SurnameS1,TelS1}
print(Ogrenciler)
 
# Ogrenci numarasini kullanicidan alip ilgili ogrenci bilgisini gosterin
BilgiGetir = input("Numara giriniz:")
print(Ogrenciler[BilgiGetir])





























