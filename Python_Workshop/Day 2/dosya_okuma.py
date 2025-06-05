#open("demo.txt", "x") # Dosya oluşturma


# open("demo.txt", "r") # Dosyayı okuma modunda açma
# open("demo.txt", "w") # Dosyayı yazma modunda açma
# open("demo.txt", "a") # Dosyayı ekleme modunda açma
# open("demo.txt", "r+") # Dosyayı okuma ve yazma modunda açma
# open("demo.txt", "a+") # Dosyayı okuma ve ekleme modunda açma
# open("demo.txt", "x") # Dosyayı oluşturma modunda açma

# dosyayı açtıktan sonra kapatmak gerekir.
# with dosyayı otomatik olarak kapatır.
"""
with open("demo.txt", "w") as dosya: 
    dosya.write("Merhaba Dunya\n")
    dosya.write("Python Programlama Dili\n")
    dosya.write("Dosya Islemleri\n")

    # w kullanıldığında dosya içeriği silinir ve yeni içerik eklenir.
    # a kullanıldığında dosya içeriği silinmez ve yeni içerik eklenir.

with open("demo.txt", "a") as dosya:
    dosya.write("Selam\n")
    dosya.write("Nasilsin\n") """

      # read() dosyanın tamamını okur. 
"""         
with open("demo.txt", "r") as dosya:
        veri = dosya.read()
        print(veri) """

# readline() dosyanın ilk satırını okur.
"""
with open("demo.txt", "r") as dosya:
        veri = dosya.readline()
        print(veri) """

# readlines() dosyanın tüm satırlarını okur ve bir liste döner.
"""
with open("demo.txt", "r") as dosya:
        veri = dosya.readlines()
        for satir in veri:
            print(satir.strip())  """

            # strip() satır sonundaki boşlukları siler.

"""
not_ = input("Notunuzu girin: ")

with open("notlar.txt", "a") as dosya:
    dosya.write(not_ + "\n")

print("Notunuz kaydedildi.") """

# eğer notlar.txt dosyası yoksa, a ile dosya oluşturulur.

try: 
    with open("olmayan_dosya.txt", "r") as dosya:
        notlar = dosya.read()
except FileNotFoundError:
    print("Dosya bulunamadı.")
