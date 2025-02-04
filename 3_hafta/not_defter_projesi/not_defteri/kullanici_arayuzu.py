
def not_girisi():  # girilecek not ve basligi alinir.
    
    baslik = input("Not Basligi: ")
    icerik = input("Not Girin: ")
    return baslik, icerik

def not_goster(notlar):  # notlar gosterilir
    
    if not notlar:
        print("not yok.")
        

    for i, notx in enumerate(notlar):  # enumerate edilerek indeks ve icerik bilgisi
        print(f"\n Not { i + 1}: ")
        print(f"Baslik: {notx['baslik']} ")
        print(f"Icerik: {notx['icerik']} ")
        print(f"Tarih: {notx['tarih']} ")
        

def not_silme_secimi(notlar): # not silmek icin
    not_goster(notlar)
    
    try:
        indeks = int(input("silmek istediginiz notun numarasi: cikis icin 0 "))
        if indeks == 0:   # o donerse islem iptal
            return 0
        elif 1 <= indeks <= len(notlar):  # not silinir
            return indeks
        else:   # gecersiz islem
            print("Geçersiz seçim. Not numarası listede yok.")
    except ValueError:
        print("Geçersiz giriş. Lütfen bir sayı girin.")