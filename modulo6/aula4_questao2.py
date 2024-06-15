frase = str(input("digite uma frese: "))
frase = frase.replace(" ", "")
print(frase)
vogais = [i for i in frase if i in "AEIOUaeiou"]
print(vogais)
consoantes = [i for i in frase if not i in vogais]
print(consoantes)