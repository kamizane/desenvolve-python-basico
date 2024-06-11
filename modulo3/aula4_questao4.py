distancia = float(input("Digite a distância (km): "))
peso = float(input("Digite o peso(kg): "))
if (distancia <= 100) :
    valor = peso * 1
elif ((distancia >= 101) and (distancia <= 300)) :
    valor = peso * 1.5
elif (distancia > 300) :
    valor = peso * 2
if (peso > 10):
    valor += 10
print(valor)