### Dosya Yonetimi ###

# Dosya Acma - Olusturma

"""

Dosya acmak ve olusturmak icin open() fonksiyonu
kullanilir.

Kullanimi: open(dosya adi,dosya erisme modu)

Dosya Erisme Modu:
    "w" : write - yazma modu - dosyayi konumda olusturur.
    "a" : append - dosya konumda yoksa olusturur.
    "x" : create - dosya zaten varsa hata verir.
    "r" : read - dosya konumda yoksa hata verir.
"""


# "w" : write - yazma modu - dosyayi konumda olusturur.

file = open("textfile.txt","w")
file.close()  # dosyayi kapama

# dosyaya eklerken eski bilgi silinir
file = open("C:/Users/berra/OneDrive/Masaüstü/AI Camp Cerebrum/3_hafta/dosya_yonetimi/usertextfile.txt","w")
file.write("w ile olusturulan dosya")
file.close()

# dosyaya ekleme yaparken uzerine yazilir.
file = open("C:/Users/berra/OneDrive/Masaüstü/AI Camp Cerebrum/3_hafta/dosya_yonetimi/usertextfile.txt","a")
file.write("\n a ile olusturuldu.")
file.close()

# dosya zaten varsa hata verir.
# file = open("C:/Users/berra/OneDrive/Masaüstü/AI Camp Cerebrum/3_hafta/dosya_yonetimi/usertextfile.txt","x")

# Dosya Okuma

file = open("C:/Users/berra/OneDrive/Masaüstü/AI Camp Cerebrum/3_hafta/dosya_yonetimi/usertextfile.txt","r")

for i in file:
    print(i,end="")

# ya da 


content = file.read(5)  # 5 karakter oku
print(content)
content = file.read()  # dosya okuma
print(content)

file.close()

# readline()  satir satir okur.

file = open("C:/Users/berra/OneDrive/Masaüstü/AI Camp Cerebrum/3_hafta/dosya_yonetimi/usertextfile.txt","r")

print(file.readline() )
print(file.readline() )

file.close()

# with ile close otomatik cagrilir.
with open("C:/Users/berra/OneDrive/Masaüstü/AI Camp Cerebrum/3_hafta/dosya_yonetimi/usertextfile.txt","r") as file:
    content = file.read()  # dosya okuma
    print(content)
    
    print(file.tell())  # cursor un (imlecin) konumu
    
    file.seek(10)  # imlec 10 dan baslar
    content = file.read()  # dosya okuma
    print(content)


# Dosya Guncelleme

with open("C:/Users/berra/OneDrive/Masaüstü/AI Camp Cerebrum/3_hafta/dosya_yonetimi/usertextfile.txt","r+") as file:

    file.write("\n deneme yazildi.")  # guncelleme

with open("C:/Users/berra/OneDrive/Masaüstü/AI Camp Cerebrum/3_hafta/dosya_yonetimi/usertextfile.txt","r+") as file:
    print(file.read())

with open("C:/Users/berra/OneDrive/Masaüstü/AI Camp Cerebrum/3_hafta/dosya_yonetimi/usertextfile.txt","r+") as file:
    print(file.read())
    print(file.tell())
    file.seek(43)  # imleci 43 e tasidik.
    file.write("imlec tasindi.")


with open("C:/Users/berra/OneDrive/Masaüstü/AI Camp Cerebrum/3_hafta/dosya_yonetimi/usertextfile.txt","r+") as file:
    print(file.read())

# "a" ile acip da en sona ekleyebiliriz.

# sayfa basina

with open("C:/Users/berra/OneDrive/Masaüstü/AI Camp Cerebrum/3_hafta/dosya_yonetimi/usertextfile.txt","r+") as file:
    content = file.read()
    content = "basa guncelleme \n" + content
    file.seek(0)
    file.write(content)
    
with open("C:/Users/berra/OneDrive/Masaüstü/AI Camp Cerebrum/3_hafta/dosya_yonetimi/usertextfile.txt","r+") as file:
    print(file.read())















