### Nesne Tabanli Programlama ###

# Nesne Tabanli Programlama Nedir ?

""" 
Nesne tabanli programlama,
gercek dunyadaki nesneleri temsil eden siniflar ve
bu siniflardan olusturulan nesneler kullanarak 
programlama yapma seklidir.
"""


# class:
    
"""
Siniflar, nesnelerin temel ozelliklerini ve
davranislarini tanimlayan yapilardir.
Siniflar,degiskenler, metotlar ve alt siniflar gibi
uyeler icerebilir.
"""   
    
    
# instance(object)

""" 
Siniflardan olusturulan nesneler,
sinifin ozelliklerine ve davranislarina sahiptir.
"""

# Nesne Tabanli Programlamanin Faydalari

"""
Nesne tabanli programlama, asagidaki faydalari saglar:
 
- Kodun okunabilirligini ve anlasilabilirligini artirir.
- Kodun yeniden kullanilabilirligini artirir.
- Kodun bakimini kolaylastirir.
- Kodun daha esnek ve olceklenebilir olmasini saglar.
"""



# Class Olusturma 

class Bos:          # bos sinifini tanimlama
    # pass             # bos class tanimlama
    
    # constructor  def__init__(self,):  # yapici metod
    """ attributes ya da 
     methods yer alabilir."""


# class
class Person:        # kisi sinifi tanimlandi
    
# class attributes
    Name = " "      # name,surname ve age degiskenleri
    Surname = " "
    Age = 0
 
# class methods
    def Info(self):       # nesnenin bilgilerini yazdiran info() metodu
        print("İsim:", self.Name)     # name bilgisini ekrana yazdirir.
        print("Soyisim:", self.Surname)     # surname bilgisini ekrana yazdirir.
        print("Yas:", self.Age)     # age bilgisini ekrana yazdirir.


# Nesne Olusturma

P1 = Person()
P2 = Person()
P3 = Person()

P1.Name = "Berra"        # P1 icin bilgiler girildi.
P1.Surname = "Alinca"    # Nesne uzerinden class ozelliklerine erisim
P1.Age = 22

P2.Name = "Ali"
P2.Surname = "Yilmaz"
P2.Age = 12

P3.Name = "Veli"
P3.Surname = "Demir"
P3.Age = 23

P1.Info()        # p1 bilgilerini ekrana yazdirma
P2.Info()        # nesne uzerinden methodlara erisim
P3.Info()

# Update

P1.Name = "Berra Nur"   # nesne uzerinden degisken guncellendi
P1.Info()




# Circle Class

class Circle:           # class tanimi

# class attributes
    pi = 3.14      
 
# class constructor
    def __init__(self,radius = 1):    # yaricap bilgisi verilmezse varsayilan 1
        self.radius = radius

# class methods
    def CirclePer(self):      # cevre hesaplama
        return 2 * self.pi * self.radius

    def CircleArea(self):
        return self.pi * (self.radius ** 2)     # alan hesaplama


C1 = Circle(10)
C2 = Circle()        # yaricap 1

print(f"C1 cevresi: {C1.CirclePer()}")    # cevre hesaplama
print(f"C1 alani: {C1.CircleArea()}")     # cevre hesaplama

print(f"C2 cevresi: {C2.CirclePer()}")    # cevre hesaplama
print(f"C2 alani: {C2.CircleArea()}")     # cevre hesaplama
 



# Inheritance(Miras Alma)

""" Bir sinifin ozelliklerini ve davranislarini
baska bir sinifa miras alma islemidir."""

# hayvan classindan miras alan kopek sinifi


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


D1 = Dog()  # kopek nesnesi olusturma
# D1 = Animal()  hayvan nesnesi olusturma

D1.PetName = "Tintin"
D1.PetGender = "Scotish"

D1.Info()
D1.Bark()




# Special Methods

MyStr = "my string"

print(len(MyStr))    # str icin calisirken


# boyle bir class taanimladigimizda 
"""
class MyClass():
    pass

M1 = MyClass() 
"""
# print(len(M1)) bu ifade calismaz.
# Bu ifadenin bizim class'imiz icin tanimli olmasi gerekir.

class MyClass():
    
    
    def __init__(self,Mylen):
        self.MyLen = Mylen
        
    def __len__(self):       # len methodunu MyClass icin tanimladik
        return self.MyLen
    
M1 = MyClass(100) 
print(len(M1))


# Quiz Uygulamasi

# Sorular sinifi: Her bir soru ve cevaplarini tutar
class Questions:
    def __init__(self,content,choices,answer):
        self.content = content   # soru icerigi
        self.choices = choices   # cevap secenekleri
        self.answer = answer     # dogru cevap
        
    def CheckAns(self,answer):   # cevabi kontrol eden metod
        return str(self.answer) == answer
            
 
# Quiz sinifi: Sorulari yonetir skoru tutar
class Quiz:

    def __init__(self,questions):
        self.questions = questions  # Sorularin listesi
        self.score = 0   ## Kullanicinin skoru
        self.questionIndex = 0  # Hangi sorunun gosterilecegini tutan indeks
        
    def GetQuestion(self):    # Gecerli soruyu getir
        return self.questions[self.questionIndex]

    def DisplayQuestion(self): # Soruyu ekrana yazdir
        
        question = self.GetQuestion()  # Gecerli soruyu al
        print(f"Soru {self.questionIndex + 1 } :{question.content} ")
    
        for choice in question.choices:   # Secenekleri ekrana yazdir
            print("-" + choice)
        
        answer = input("cevap:")  # Kullanicinin cevabini al
        
        if question.CheckAns(answer): # Cevabi kontrol et ve skoru guncelle
            self.score += 1 
            print("cevap dogru")
        else:
            print("cevap hatali")
        self.questionIndex += 1
            
    def DisplayResult(self):  # Quiz sonucunu ekrana yazdir
        print(f"Quiz bitti. Toplam skorunuz: {self.score} / { len(self.questions) }")

# soru ornekleri 
Q1 = Questions("2 + 2 ? ", ["1","2","3","4"], 4)
Q2 = Questions("en populer yazilim dili",["python","C","Java"],"python")
# soru listesi
questions = [Q1,Q2]
# sorulai iceren quiz
quiz1 = Quiz(questions)
# tum sorulari goster
while quiz1.questionIndex < len(quiz1.questions):
    quiz1.DisplayQuestion()
# quiz sonucunu goster
quiz1.DisplayResult()









