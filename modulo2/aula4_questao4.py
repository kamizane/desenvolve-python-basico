valor = int(input())
nota100= 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0
while (valor >= 100):
    valor -= 100
    nota100 +=1
while (valor >= 50):
    valor -= 50
    nota50 += 1
while (valor >= 20):
    valor -= 20
    nota20 += 1
while (valor >= 10):
    valor -= 10
    nota10 += 1
while (valor >= 5):
    valor -= 5
    nota5 += 1
while (valor >= 2):
    valor -= 2
    nota2 += 1
while (valor >= 1):
    valor -= 1
    nota1 += 1
print("%d nota(s) de R$100,00 \n %d nota(s) de R$50,00 \n %d nota(s) de R$20,00 \n %d nota(s) de R$10,00 \n %d nota(s) de R$5,00 \n %d nota(s) de R$2,00 \n %d nota(s) de R$1,00" % (nota100, nota50, nota20, nota10, nota5, nota2, nota1))

