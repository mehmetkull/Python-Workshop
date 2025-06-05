yas = 15

if yas >= 18:
    print("Reşitsiniz!")
else:
    print("Reşit Değilsiniz!")

not_ = 75

if not_ >= 90:
    print("Notunuz: AA")
elif not_ >= 80:
    print("Notunuz: BA")
elif not_ >= 70:
    print("Notunuz: BB")
else:
    print("Kaldiniz.")

kullanici_adi = "admin"
sifre = "1234"

if kullanici_adi == "admin":
    if sifre == "1234":
        print("Giris Basarili!")
    else:
        print("Sifre yanlis!")
else:
    print("Kullanici adi yanlis!")

yas = 25
ehliyet_var_mi = True

if yas >= 18 and ehliyet_var_mi:
    print("Araba Kullanabilirsin")
else:
    print("Araba Kullanamazsin!")