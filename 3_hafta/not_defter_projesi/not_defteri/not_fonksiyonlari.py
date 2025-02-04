
import json
import datetime

def not_oku(dosya_adi):  # dosyayi okuma

    try:
        with open(dosya_adi, "r") as notlar:  # okunabilir sekilde ac
            return json.load(notlar) # dosyayi oku
            print("dosya okundu.")
    except Exception :   # dosya bulunamadi.
        return []
    

def not_ekle(notlar, baslik, icerik):  # dosyaya not ekler.
    
    tarih = datetime.datetime.now().isoformat()   # olusturulma tarihi
    notlar.append({"baslik": baslik, "icerik": icerik, "tarih": tarih}) # notlara ekle
    

def not_sil(notlar,indeks):  # not silme
    if indeks > 0 and indeks <= len(notlar):  # verilen indeks dogrulama
        del notlar[indeks-1]  # bu indeksteki notu sil
        return True
    return False

def not_sirala(notlar):  # notlari tarihe gore sirala
    return sorted(notlar,key=lambda notx:notx["tarih"],reverse=True)
    
        
# her islemden sonra kaydedilir.
def not_kaydet(notlar,dosya_adi="C:/Users/berra/OneDrive/Masaüstü/AI Camp Cerebrum/3_hafta/not_defter_projesi/not_defteri/notlar.json"):
    try:
        with open(dosya_adi,"w") as notlar1:
            json.dump(notlar, notlar1, indent=4, ensure_ascii=False) # kaydetme ve ozellestirme
            print("notlar kaydedildi.")
    except Exception as e:
        print(e)


