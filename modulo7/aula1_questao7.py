import random

def encrypt(x):
    contador=0
    for i in x:
        i = i.replace(i,chr(ord(i)+chave))
        x = x.replace(x[contador],i)
        contador+=1
    return x

nomes = "Luana, Ju, Davi, Vivi, Pri, Luiz"
nomes = nomes.lower()
chave = random.randint(1,10)

nomes_cripto = encrypt(nomes)
print(nomes_cripto)
print(chave)