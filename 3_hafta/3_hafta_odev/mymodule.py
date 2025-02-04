# modul olusturma
import math

print("modul eklendi.")

# aritmetik ortalama hesaplayan fonk

def aricmeticort(*args):
    if not args:
        return 0
    return  sum(args) /  len(args)


# geometrik ortalama hesaplayan fonk

def geometricort(*args):
    
    if not args:
        return 0  # Eğer hiç girdi verilmezse, ortalama 0 olarak kabul edilir.

    carpim = 1
    adet = len(args)

    for sayi in args:
        if sayi <= 0:
            raise ValueError("Geometrik ortalama negatif veya sifir icin hesaplanamaz.")
        carpim *= sayi

   
    return  math.pow(carpim, 1 / adet)