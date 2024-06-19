frase = str(input("Digite uma frase: "))
indf = ""
ind=-1
contador = 0
for i in frase:
    ind+=1
    if i in "aeiouAEIOU":
        contador+=1
        indf += str(ind)
lst = list(indf)
txt = ",".join(lst)
print(contador)
print(lst)