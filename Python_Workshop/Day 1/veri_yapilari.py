meyveler = ["elma", "armut", "muz", "çilek"]
print (meyveler[-1])
"""soldan sağa 0 dan başlar
sağdan sola -1 den başlar"""

meyveler.append("kivi") # sona ekler
meyveler.insert(1, "portakal") # 1. indexe ekler

meyveler.remove("armut") # siler

print(meyveler)

meyveler.sort() # sıralar
print(len(meyveler))


koordinat = (10, 20) # tuple
# tuple değiştirilemez
print(koordinat[0])

# koordinat[0] = 15 # hata verir

sayilar = {1, 2, 3, 3, 4, 4, 5}

print(sayilar)

#print(sayilar[0]) # hata verir

sayilar.add(6) # ekler
sayilar.remove(3) # siler
print(sayilar)

a = {1, 2, 3}
b = {3, 4, 5}

print(a - b) # fark

ogrenci = {
    "ad": "Ahmet",
    "yas": 38,
    "sehir": "Mersin"
}

print(ogrenci["ad"])

ogrenci["yas"] = 22

ogrenci["okul"] = "YTÜ"

print(ogrenci.keys()) # anahtarları alır
print(ogrenci.values()) # değerleri alır