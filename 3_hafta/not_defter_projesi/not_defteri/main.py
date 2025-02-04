
from not_fonksiyonlari import not_oku,not_ekle,not_sil,not_sirala,not_kaydet  # import etme
from kullanici_arayuzu import not_girisi,not_goster,not_silme_secimi

def ana_menu():
    
    dosya_adi = "C:/Users/berra/OneDrive/Masaüstü/AI Camp Cerebrum/3_hafta/not_defter_projesi/not_defteri/notlar.json"
    notlar = not_oku(dosya_adi) # okunan dosyayi atama
    
    if not notlar:  # eger dosya bossa
        notlar = []
        
    while True:      # cikana kadar islem yapilir
        print("Not Defteri")
        print("1. Not Ekle")
        print("2. Notlari Goruntule")
        print("3. Notlari Tarihe Gore Sirala")
        print("4. Not Sil")
        print("5. Cikis")
        
        islem = input("Islem seciniz: ")  # islem turu secme
        
        if islem == "1":  # kullanicidan not girisi alir ve notu ekler.
            baslik,icerik = not_girisi()
            not_ekle(notlar, baslik, icerik)
            
        elif islem == "2":  # notlari goruntuler
            not_goster(notlar)
        elif islem == "3":  # notlari siralar.
            notlar = not_sirala(notlar)  # sirali liste gosterilir
            not_goster(notlar)
        elif islem == "4":   # not silme islemi
            indeks = not_silme_secimi(notlar)  # indeks al
            if indeks == 0:  # indeks o donerse
                print("silme yapilmadi.")
            elif 1 <= indeks <= len(notlar):  # indeks 1 ve not uzunlugu arasindaysa silme yapilir
                if not_sil(notlar, indeks):   # islem basarili
                    print("not silindi.") 
                else:   # diger durumlarda
                    print("not silme basarisiz.") 
            else:  # indeks secilemezse
                print("indeks secimi yapilamadi")
            
        elif islem == "5":  # islem sonlandirma
            print("cikis yapildi.")
            break
        else:
            print("gecersiz islem...")
            
        not_kaydet(notlar,dosya_adi)  # notlari kaydet
        
        
if __name__ == "__main__":
    ana_menu()

