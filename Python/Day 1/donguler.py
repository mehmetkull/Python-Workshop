meyveler = ["elma","armut","muz"]

for meyve in meyveler:
    print(meyve)

for i in range(5):
    print(i)

for i in range(1,10,2):
    print(i)

sayi = 1

while sayi <= 5:
    print(sayi)
    sayi += 1

while True:
    komut = input("Çıkmak için q tuşuna basın:")
    
    if komut == "q":
        print("Programdan çıkıldı")
        break
    else:
        print("Devam ediliyor...")

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)

for i in range(3):
    pass