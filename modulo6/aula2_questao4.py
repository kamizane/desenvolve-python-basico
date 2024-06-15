from itertools import zip_longest

qnt_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = list()
print("Digite os %d elementos da lista 1:" % (qnt_lista1))
for i in range(qnt_lista1):
    elemento1 = int(input())
    lista1.append(elemento1)

qnt_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = list()
print("Digite os %d elementos da lista 2:" % (qnt_lista2))
for a in range (qnt_lista2):
    elemento2 = int(input())
    lista2.append(elemento2)
print(lista1,lista2)
intercalada= list()
for a,b in zip_longest(lista1,lista2, fillvalue=None):
    if a is not None:
        intercalada.append(a)
    if b is not None:
        intercalada.append(b)
print(intercalada)