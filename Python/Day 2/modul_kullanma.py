import math as a 
from math import sqrt
import random as r
import requests
import mat_modul

print(a.sqrt(16))
print(a.factorial(5))

print(r.randint(1,10))

icerik = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(icerik.json())

print(mat_modul.topla(3,5))
print(mat_modul.carp(3,5))