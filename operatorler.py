### Operatorler ###

# Atama = ,+= ,-= ,/= ,*= ,%=

x,y,z = 5,15,25
print(x)

x = 555
print(x)

x += 5      # x = x + 5
print(x)

x -= 5 
print(x)

x /= 5 
print(x)

x *= 5 
print(x)

x %= 5 
print(x)

# Uygulama

a,b,c = 2,5,107
Numbers = 1,5,7,10,6

# Kullanicidan aldiginiz 2 sayinin carpimi ile a,b,c toplaminin farki nedir

Sayi1 = int(input("ilk sayi:"))
Sayi2 = int(input("ikinci sayi"))
Fark = ( Sayi1 * Sayi2 ) - ( a + b + c )
print(Fark)

# b' nin a' ya kalansiz bolumunu hesaplayiniz.

Bolum = b / a
print(int(Bolum))

# a,b,c toplaminin mod 3'u nedir

Mod = ( a + b + c ) % 3
print(Mod)

# b'nin a.nci kuvvetini hesaplayiniz.

Kuvvet =  b ** a
print(Kuvvet)



# Karsilastirma

UserName = "Berra"
Password = "12345"


Control = ( "Berra" == UserName)
print(Control)


# Uygulama

# Girilen 2 sayidan hangisi daha buyuktur

Girdi1 = int(input("1.sayi:" ))
Girdi2 = int(input("2.sayi: "))

if(Girdi1 > Girdi2):
    print("1.sayi buyuktur.")
else:
    print("2.sayi buyuktur.")
       

# Kullanicidan 2 vize (%60) ve final(%40) notunu alip ortalama hesaplayiniz.

Vize1 = int(input("ilk vize: "))
Vize2 = int(input("ikinci vize: "))
Final = int(input("final: "))

Ortalama = (Vize1 + Vize2 ) / 2 * 0.6 + (Final * 0.4)
print(Ortalama)




# Mantıksal and,or,not

Not = 85
AA = (Not > 90) and (Not < 100)
print(True == AA)


















