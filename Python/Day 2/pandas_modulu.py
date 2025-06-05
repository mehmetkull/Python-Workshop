import pandas as pd

data = pd.DataFrame({
    "Yaş": [25,45,30,35,40],
    "Cinsiyet": ["Kadın","Erkek","Erkek","Kadın",None],
    "Maaş": [3000,7000,None,5000,6000],
    "Deneyim": [2,20,5,10,15],
    "Departman": ["IT","Yönetim","Muhasebe","IT","Yönetim"],
    "Terfi": [0,1,0,1,1]
})

print("Veri Setinin ilk 5 Satırı:")
print(data.head())

print("Eksik Değerlerin Sayisi:")
print(data.isnull().sum())

print("Veri Seti Bilgisi:")
print(data.info())

print("İstatistiksel Özet:")
print(data.describe())