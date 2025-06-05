meyveler = ["elma","armut","muz"]

print(meyveler[2])

meyveler.append("çilek")

meyveler.insert(1,"kiraz")

meyveler.remove("armut")

print(meyveler)
meyveler.sort()
print(len(meyveler))

koordinat = (10,20)

print(koordinat[0])

#koordinat[0] = 50 HATA VERİR!

sayilar = {1,2,3,3,4,4,5}
demo = {"Ali","Veli","Ayşe","Armut"}

print(demo)

#print(sayilar[0]) HATA VERİR!

sayilar.add(6)
sayilar.remove(2)
print(sayilar)

a = {1,2,3}
b = {3,4,5}
print(a - b)

ogrenci = {
    "ad":"Ahmet",
    "yas": 38,
    "sahir": "Mersin"
}

print(ogrenci["ad"])

ogrenci["yas"] = 22

ogrenci["okul"] = "YTÜ"

print(ogrenci.keys())
print(ogrenci.values())