import pandas as pd

from sklearn.preprocessing import LabelEncoder, StandardScaler

from sklearn.model_selection import train_test_split

def handle_missing_values(data):
    data["Maaş"] = data["Maaş"].fillna(data["Maaş"].mean())
    data["Cinsiyet"] = data["Cinsiyet"].fillna("Bilinmiyor")

    print("\n Eksik Değerlerin Sayısı(Doldurulduktan sonra)")
    print(data.isnull().sum())

    return data

def encode_categorial_data(data):

    le = LabelEncoder()
    data["Cinsiyet"] = le.fit_transform(data["Cinsiyet"])

    data = pd.get_dummies(data, columns=["Departman"], drop_first=True)
    print("\n Kategorik Dönüştürme")
    print(data.head())
    return data

def scale_data(data):
    scaler =StandardScaler()

    data[["Yaş","Maaş","Deneyim"]] = scaler.fit_transform(data[["Yaş","Maaş","Deneyim"]])
    print("\n Öçeklendirme Sonrası")
    print(data.head())
    return data

def split_data(data):

    x = data.drop(["Terfi"],axis=1)
    y = data["Terfi"]

    x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    return x_train,x_test,y_train,y_test

