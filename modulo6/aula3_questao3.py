import random
lista = list()
for a in range(20):
    lista.append(random.randint(-10,10))
fatia_maior = 0
tam_fatia_maior = 0
fatia_atual = 0
tam_fatia_atual = 0
print(lista)
for i in range(len(lista)):
    if lista[i]<0:
        tam_fatia_atual += 1
        if tam_fatia_atual == 1:
            fatia_atual = i
    else:
        if tam_fatia_atual > tam_fatia_maior:
            tam_fatia_maior = tam_fatia_atual
            fatia_maior = fatia_atual
        tam_fatia_atual = 0
del lista[fatia_maior:fatia_maior+tam_fatia_maior]
print(lista)