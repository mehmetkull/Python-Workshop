def selamla():
    print("Merhaba Dünya!")

selamla()

def selamla(isim):
    print(f"Merhaba {isim}!")

selamla("Ahmet")

def topla(x,y):
    return x + y

sonuc = topla(5,6)
print(sonuc)

def topla(*sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return toplam

print(topla(1,2,3,4,5,54))

def bilgiler(**kisi):
    for anahtar, deger in kisi.items():
        print(f"{anahtar}: {deger}")

bilgiler(ad="Ahmet",yas=38,sehir="Mersin")

kare = lambda x:x*x

print(kare(5))

def kullanici_topla():
    a = int(input("Birinci sayiyi girin: "))
    b = int(input("İkinci sayiyi girin: "))
    print("Toplam", a + b)

kullanici_topla()

