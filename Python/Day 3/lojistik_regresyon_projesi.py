import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

print("Lojistik Regresyon İçin Veri Seti Oluşturuluyor...")

data_classification = {
    "Age": [22,25,47,52,46,56,55,60,62,61],
    "Income": [25000,32000,47000,52000,46000,58000,60000,62000,64000,63000],
    "Purchased": [0,0,1,1,1,1,1,1,1,1]
}

df_classification = pd.DataFrame(data_classification)
print("Lojistik Regresyon Veri Seti")
print(df_classification.head())

print("Lojistik Regresyon İçin Veri Eğitim ve test Setine Ayrılıyor...")

x_cls = df_classification[["Age","Income"]]
y_cls = df_classification["Purchased"]

x_train, x_test, y_train, y_test = train_test_split(x_cls,y_cls,test_size=0.2, random_state=42)

print(f"Eğitim Seti Boyutu: {x_train.shape}")
print(f"Test Seti Boyutu: {x_test.shape}")

model_logistic = LogisticRegression()

model_logistic.fit(x_train,y_train)
print("Logistic Regresyon Modeli Eğitildi!")
print("Katsayılar:")
print(model_logistic.coef_)
print(f"Intercept: {model_logistic.intercept_}")

print("Lojistik Regresyon Modeli Test Verisi ile tahmin Yapıyor...")

y_pred_logistic = model_logistic.predict(x_test)

print("Gerçek vs Tahmin Edilen Değerler:")
for gerçek, tahmin in zip(y_test,y_pred_logistic):
    print(f"Gerçek: {gerçek} -> Tahmin: {tahmin}")

print("Lojistik Regresyon Modeli Performansı Ölçülüyor...")

accuracy_logistic = accuracy_score(y_test, y_pred_logistic)

print(f"Doğruluk Skoru: {accuracy_logistic:.4f}")

print("KNN Modeli Eğitiliyor...")

model_knn = KNeighborsClassifier(n_neighbors=7)

model_knn.fit(x_train,y_train)

print("KNN Modeli Test Verisi ile Tahmin Yapıyor...")

y_pred_knn = model_knn.predict(x_test)

for gerçek, tahmin in zip(y_test, y_pred_knn):
    print(f"Gerçek: {gerçek} -> Tahmin: {tahmin}")

print("KNN Modeli Performansı Ölçülüyor...")

accuracy_knn = accuracy_score(y_test, y_pred_knn)

print(f"Doğruluk Skoru: {accuracy_knn:.4f}")
