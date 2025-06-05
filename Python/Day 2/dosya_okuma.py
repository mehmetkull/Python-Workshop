#open("demo.txt","x") Dosya oluşturma
"""
with open("demo.txt","w") as dosya:
    dosya.write("Merhaba!\n")
    dosya.write("Nasilsin ?\n")

    "w" içerisinde bir yazı olsa dahi silip üzerine yazar.

with open("demo.txt","a") as dosya:
    dosya.write("Selam!\n")
    dosya.write("Iyiyim\n")
with open("demo.txt","r") as dosya:
    veri = dosya.read()
    print(veri)
with open("demo.txt","r") as dosya:
    veri = dosya.readline()
    print(veri)
with open("demo.txt","r") as dosya:
    veri = dosya.readlines()
    for satir in veri:
        print(satir.strip())

not_ = input("Notunuzu Girin: ")

with open("notlar.txt","a") as dosya:
    dosya.write(not_ + "\n")

print("Not Kaydedildi!")
"""
try:
    with open("olmayan_dosya.txt","r") as dosya:
        print(dosya.read())
except FileNotFoundError:
    print("Dosya bulunamadı!")
    