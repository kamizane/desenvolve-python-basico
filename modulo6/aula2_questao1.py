import random
lista = list()
for i in range(0,20):
    lista.append(random.randint(-100,100))
print(sorted(lista))
print("\n")
print(lista)
print("\n")
print("maximo:",max(lista))
print("\n")
print("minimo:",min(lista))