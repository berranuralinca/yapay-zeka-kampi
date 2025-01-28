### 2.Hafta Odev ###

# 1. Temel Fonksiyonlar

# Bir sayi dizisinin ortalamasini hesaplayan bir fonksiyon yazin.

Numbers = []       # sayi dizisini olusturma
print("Sayı girin:")
print("Dizi tamam yazın.")

while True:
    Control = input()        # dizi tamam mi kontrolu
    if Control.lower() == "dizi tamam": 
        break                # dizi tamamsa donguden cıkar.
    try:                     
        Number = int(Control)  
        Numbers.append(Number)
    except ValueError:
        print("Geçersiz giriş. Lütfen bir sayı girin veya 'dizi tamam' yazın.")

def average(Numbers):  # ortalama alan fonk.
    if not Numbers:    # deger yoksa ortalama = 0
        return 0
    Total = sum(Numbers)
    NumberLen = len(Numbers)
    return Total / NumberLen

if Numbers: # boş liste kontrolü
    print(f"Ortalama: {average(Numbers)}")
else:
    print("Hiç sayı girilmedi.")



# Girilen iki sayinin en buyugunu donduren bir fonksiyon olusturun.

Sayi1 = int(input("ilk sayi giriniz: "))         # ilk sayi girdisi
Sayi2 = int(input("ikinci sayi : "))           # ikinci sayi girdisi



def BuyukMu(a,b):            # buyuk olani yazdirma
    if a > b:
        print("buyuk olan sayi:" + str(a))
    elif(a < b):
        print("buyuk olan sayi:" + str(b))
    else:
        print("sayilar esit...")

BuyukMu(Sayi1,Sayi2)



# Bir metin icindeki kelimeleri sayan bir fonksiyon yazin.

Text = input("Metin giriniz:")
def KelimeSayaci(text):
    
    Words = Text.split()    # Metni bosluklara gore kelimelere ayir

    WordNum = {}            # Kelime sayisi icin bos bir sozluk olustur
    
    for word in Words:      
        if word in  WordNum:    # Eger kelime varsa arttirir,yoksa kelimeyi ekler.
            WordNum[word] += 1  # Kelime zaten varsa sayısını artır
        else:
            WordNum[word] = 1   # Kelime yoksa sözlüğe ekle ve sayısını 1 yap

    return  WordNum
    
print(KelimeSayaci(Text))





# 2. Lambda İfadeleri, Map ve Filtre

# Bir liste icindeki tek sayilarin karesini alan bir map fonksiyonu yazin.


Numbers2 = []       # sayi dizisini olusturma
print("Sayı girin:")
print("Dizi tamam yazın.")

while True:
    Control2 = input()        # dizi tamam mi kontrolu
    if Control2.lower() == "dizi tamam": 
        break                # dizi tamamsa donguden cıkar.
    try:                     
        Number2 = int(Control2)  
        Numbers2.append(Number2)
    except ValueError:
        print("Geçersiz giriş. Lütfen bir sayı girin veya 'dizi tamam' yazın.")
        

def Karesi(Num2):              # tek sayilarin karesini alir,cift sayiysa none doner.
 if Num2 % 2 == 1:
     return Num2**2 

Result = list(map(Karesi,Numbers2 ))       # sayilar karesi fonk. gonderilir.
Result = [x for x in Result if x is not None]    # listede none deger varsa eklenmez.

print(Result)



# 0-50 arasinda yer alan cift sayilari filtrelemek icin bir filter fonksiyon kullanin.

def CiftMi(Sayi):               #  sayinin cift olup olmadigini kontrol eder.
  return Sayi % 2 == 0

Sayilar = list(range(0,50,1))   # 0-50  bir liste olusturur

CiftSayilar = list(filter(CiftMi,Sayilar))  # cift sayıları filtreler

print(CiftSayilar)  # Sonucu yazdırır



# Lambda kullanarak verilen iki sayi arasindaki tum tam sayilarin toplamini hesaplayan bir fonksiyon olusturun.

baslangic = int(input("baslangic degeri: "))
bitis = int(input("bitis degeri: "))

def Topla(a, b):
    ToplamHes = lambda a, b: sum(range(a, b + 1))  
    return ToplamHes(a, b)  

Result = Topla(baslangic, bitis)
print(Result)





# 3. Kapsam ve Degiskenler
# Global ve yerel degiskenlerle calisan bir uygulama yazin. ornegin, bir global sayacin fonksiyon icinde artirildigi bir uygulama gelistirin.

# Global degisken: ogrenci listesi
OgrList = []

def OgrEkle(name, surname,number):  #ogrenci listesine yeni bir ögrenci ekler
  
    global OgrList  # Global degisken

    NewOgr = {"name": name, "surname": surname, "number": number} # yeni ogrenci sozlugu
    
    OgrList.append( NewOgr)  # ogrenci listesine ogrenci ekleme

    print(f"{name} {surname} ({number}) listeye eklendi.")  # ekleme bilgisi

def OgrGoster():   # ogrencileri listeler
    if not OgrList:    #liste bossa
        print("Listede ogrenci yok.")
    else:
        print("Listedeki ogrenciler:")
        for Ogr in OgrList:  # ogrencilerin bilgierini listele
            print(f" {Ogr["name"]} {Ogr["surname"]} ({Ogr["number"]})")


OgrEkle("Ayse", "Yilmaz", 123)  # ogrenci ekleme
OgrEkle("Ali", "Demir", 456)
OgrEkle("Berra", "Korkut", 789)

OgrGoster()  # ogrencileri gosterme


print(f"Global öğrenci listesi: {OgrList}") # global degiskeni yazdirma






# 4. Siniflar ve Nesneler

# Bir Hesap Makinesi sinifi olusturun. Bu sinif toplama, cıkarma, carpma ve bolme islemlerini gerceklestirsin.

class Calculater:
    def Add(self,Say1,Say2):    # toplama
        return Say1 + Say2

    def Sub(self,Say1,Say2):    # cikarma
        return Say1 - Say2

    def Multi(self, Say1, Say2):  # carpma
        return Say1 * Say2

    def Div(self,Say1,Say2):   # bolme
        if Say2 == 0:
            return "Sifira bolme hatasi"
        return Say1 / Say2

Calculater1 = Calculater()

Say1 = float(input("ilk sayiyi girin: "))  # sayi girdisi
Say2 = float(input("ikinci sayiyi girin: "))

print(Calculater1.Add(Say1,Say2))
print(Calculater1.Sub(Say1,Say2))
print(Calculater1.Multi(Say1,Say2))
print(Calculater1.Div(Say1,Say2))



# Bir ogrenci sinifini olusturun.Ogrencinin adi, notlari ve sinifini tutan ozellikler ekleyin. Ortalama not hesaplayan bir metot yazin.

class Student:  # ogrenci sinifi:name,class,midterm,final bilgisi
    def __init__(self,Name ,Class):   # isim ve class bilgisi
        self.StudentName = Name  
        self.StudentNotes = {}    # Notlari sozluk olarak tutuyoruz
        self.StudentClass = Class

    def AddNote(self, Midterm = 0, Final = 0):
        self.StudentNotes["Midterm"] = str(Midterm)
        self.StudentNotes["Final"] = str(Final)

    def Average(self):
        if not self.StudentNotes:
            return 0
        
        Midterm = int(self.StudentNotes["Midterm"])
        Final = int(self.StudentNotes["Final"])
        return (Midterm * 0.4) + (Final * 0.6)  # Vize %40, Final %60
    
    def Info(self):
        print(f"ogrencinin Adi: {self.StudentName}")
        print(f"ogrencinin Sinifi: {self.StudentClass}")
        print(f"ogrencinin Notlari: {self.StudentNotes}")
        print(f"ogrencinin Not Ortalamasi: {self.Average()}")
        

S1 = Student("Ayşe", "9B")
S1.AddNote(80, 95)   # not girisi
S1.Info()


S2 = Student("Veli", "10C")
S2.AddNote(75, 85)
S2.Info()

# 5. Kalitim

# Bir Hayvan sinifi yazin ve bu siniftan Kedi ve Köpek alt siniflarini turetin.
# Her alt sinif icin farkli ses cikaran bir metot ekleyin.

# hayvan classindan miras alan kopek ve kedi sinifi


# hayvan sinifi(base class)

class Animal():

# class constructor
    def __init__(self):
        print("Hayvan sinifi")

# class attributes
    PetName = " "
    


# kopek sinifi (derived class)
class Dog(Animal):

# class constructor
    def __init__(self):
        print("Kopek sinifi")
        Animal.__init__(self)
# class attributes
    PetGender = " "
    
# class methods
    def Info(self):        # hayvan bilgisi
        print("İsim:", self.PetName)
        print("Tur:", self.PetGender)
        
    def Bark(self):            # kopege ozel islev
        print("Havladim.")


# kedi sinifi (derived class)
class Cat(Animal):

# class constructor
    def __init__(self):
        print("Kedi sinifi")
        Animal.__init__(self)
# class attributes
    PetGender = " "
    
# class methods
    def Info(self):        # hayvan bilgisi
        print("İsim:", self.PetName)
        print("Tur:", self.PetGender)
        
    def Meow(self):            # kediye ozel islev
        print("Miyavladim.")

D1 = Dog()  # kopek nesnesi olusturma
# D1 = Animal()  hayvan nesnesi olusturma
D1.PetName = "Tintin"
D1.PetGender = "Scotish"
D1.Info()
D1.Bark()

C1 = Cat()  # kedi nesnesi olusturma
C1.PetName = "Pamuk"
C1.PetGender = "Tekir"
C1.Info()
C1.Meow()




# Bir Araba sinifindan tureyen bir Elektrikli Araba sinifi olusturun. Elektrikli araba sinifina pil seviyesi ve sarj metotlari ekleyin.


class Cars():   # araba sinifi

    def __init__(self,brand,model,price):  # marka,model,fiyat bilgisi
        self.CarsBrand = brand
        self.CarsModel = model
        self.CarsPrice = price
    
    def SpeedUp(self):                         # hizlandir
        print("hizlandim...")
    
    def Slowed(self):                         # yavaslat
        print("yavasladim...")
        
    def Stopped(self):                         # durdur
        print("Durdum")

    def Info(self):
        print(f"Marka: {self.CarsBrand}, Model: {self.CarsModel},Price:{self.CarsPrice}")  # marka,model,fiyat yazdir

class ElectricCars(Cars):        # elektrikli arabalar sinifi
    def __init__(self,brand,model,price,battery = 0,capasity = 0):  #model,marka,fiyat,sarj ve batarya bilgisi
        super().__init__(brand, model, price)   # ust sinifin yapicisi
        self.ElectricCarsBattery = battery  
        self.ElectricCarsCapacity = capasity
        
    def Charge(self,amount):    # sarj etme 
        self.ElectricCarsBattery += amount
        if self.ElectricCarsBattery > self.ElectricCarsCapacity: # kapasiteyi asmamali
            self.ElectricCarsBattery = self.ElectricCarsCapacity
        print("sarj oldum...")
        
        
    def Info(self): # model,marka,fiyat,sarj ve batarya bilgisi yazdirma
        super().Info()
        print(f"Batarya: {self.ElectricCarsBattery},Capacity:{self.ElectricCarsCapacity}")
                  
Car1 = Cars("mercedes","g63","1 million dollars")
Car1.SpeedUp()
Car1.Info()

E1 = ElectricCars("tesla", "2023", "50 thousand dollars", 75, 100)
E1.Info()
E1.Charge(30)  # 30 birim sarj oldu
E1.Info()

E2 = ElectricCars("TOGG", "2024", "70 thousand dollars", 50, 60)
E2.Charge(20) # 20 birim sarj oldu kapasiteyi asmadi
E2.Info()





# 6. Ozel Metotlar

# Iki vektoru toplayan ozel bir __add__ metodu tanimlayin.

class Vector:
    def __init__(self, *args):
        self.Values = list(args)

    def __add__(self, VektorIki):
        
        Result = []
        for i in range(len(self.Values)):
            Result.append(self.Values[i] + VektorIki.Values[i])
        return Vector(*Result)

    def __str__(self):  # __str__ metodu
        return str(self.Values)



v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

v3 = v1 + v2  # __add__ metodu 
print(str(v3))


# Bir sınıfta nesnenin açıklamasını veren bir __str__ metodu yazın.

class Student:   # ogrenci sinifi
    def __init__(self,name, surname, number):
        self.Name = name
        self.Surname = surname
        self.Number = number

    def __str__(self):  # str metodu
        return f"Name: {self.Name}, Surname: {self.Surname}, Number: {self.Number}"

S1 = Student("Ali", "Yılmaz", 12345)
print(str(S1))










