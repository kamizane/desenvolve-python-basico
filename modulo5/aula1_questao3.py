import random
numero_sorteado = random.randrange(1,11)
while True:
    n = int(input("Adivinhe o númeor sorteado de 1 a 10:"))
    if n == numero_sorteado:
        print("Correto! o número é: %d" % (numero_sorteado))
        exit()
    elif n > numero_sorteado:
        print("Muito alto, tente novamente")
    elif n < numero_sorteado:
        print("Muito baixo,tente novamente")