import random
lista1 = list()
lista2 = list()
intersecao = list()
for i in range (0,20):
    lista1.append(random.randint(0,50)) 
    lista2.append(random.randint(0,50))
intersecao = set(lista1).intersection(set(lista2))
print("lista 1: ",lista1)
print("lista 2: ",lista2)
print("lista intersecção ordenada", sorted(intersecao))
intersecao = list(sorted(intersecao))
tamanho = len(intersecao)
for a in range (tamanho):
    print(intersecao[a],":",lista1.count(lista1[a]), lista2.count(lista2[a]))