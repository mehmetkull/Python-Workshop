
try:
    sayi = int(input("Bir sayı girin: "))
    print(10/sayi)

except ValueError:
    print("Lütfen geçerli bir sayı girin!") 
except ZeroDivisionError:
    print("Sayı sıfır olamaz!")
except Exception as e:
    print(f"Beklenmeyen bir hata oluştu: {e}")

else:
    print("İşlem başarılı!")
    # finally her koşulda çalışır
finally:
    print("Program sonlandı.")

    