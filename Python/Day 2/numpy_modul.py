import numpy as np

print("NumPy Versiyonu:", np.__version__)

liste = [1,2,3,4,5]
numpy_dizi = np.array(liste)
print("Türü:", type(numpy_dizi))

numpy_dizi2 = np.array([10,20,30,40,50])
print("NumPy Dizi:", numpy_dizi2)

dizi_aralik = np.arange(0,10,2)
print("Aralikli NumPy Dizi:", dizi_aralik)

dizi_sifirlar = np.zeros(5)
print("Sifir NumPy Dizi:", dizi_sifirlar)

dizi_birler = np.ones(5)
print("Birler NumPy Dizi:", dizi_birler)

dizi_linspace = np.linspace(0,20,5)
print("Eşit Parça NumPy Dizi:", dizi_linspace)

dizi_random = np.random.rand(5)
print("Rastgele Dizi:",dizi_random)

dizi = np.array([10,20,30,40,50])

print("Dizi:", dizi)
print("Toplam: ", np.sum(dizi))
print("Ortalama: ", np.mean(dizi))
print("Maksimum Değer: ", np.max(dizi))
print("Minimum Değer: ", np.min(dizi))
print("Standart Sapma: ", np.std(dizi))
print("Varyans: ", np.var(dizi))

matris = np.random.randint(1,10, (2,3))
print("Matris:\n",matris)

transpoz = matris.T
print("transpoz:\n",transpoz)

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
carpim = np.dot(A,B)
print("Matris Çarpımı:\n",carpim)

