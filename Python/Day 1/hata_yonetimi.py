try:
    sayi = int(input("Bir Sayı Girin:"))
    print(10/sayi)
except ValueError:
    print("Lütfen sadece sayı girin")
except ZeroDivisionError:
    print("Sıfıra bölme hatası")
except Exception as e:
    print("Beklenmeyen bir hata oluştu!",e)
else:
    print("Başarıyla bölündü!")
finally:
    print("İşlem tamamlandı")