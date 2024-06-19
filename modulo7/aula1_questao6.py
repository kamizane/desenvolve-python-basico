frase = "Meu amor mora em Roma e me deu um ramo de flores"
obj = "amor"
lst = frase.split(" ")
print(lst)
for i in lst:
    if ("a" and "m" and "o" and ("r" or "R")) in i :
        print(i)