"""while dögüsü sonsuza kadar devam edebilir 
fakat for dögüsü belirli bir sayıda döner"""

meyveler = ["elma", "armut", "muz", "çilek"]
for meyve in meyveler:
    print(meyve)

    for i in range(5):
        print(i)
        
        # 1 den başlayarak 10 a kadar olan sayıları
        #  ikişer ikişer yazdır
for i in range (1, 10, 2):
    print(i)

    while True:
        komut = input("Çıkmak için 'q' ya basın: ")
        if komut == "q":
            print("Çıkılıyor...")
            break
        else:
            print("Devam ediliyor...")

            for i in range(1, 10):
                if i == 5:
                    break
                print(i)

                for i in range(1, 10):
                    if i == 2:
                        continue
                    print(i)



                    for i in range(3):
                        pass

                    
