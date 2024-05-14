genero = str(input("Digite seu Gênero ('M' ou 'F'): "))
idade = int(input("digite sua idade: "))
anos_trabalhados = int(input("quantos anos você trabalhou: "))
if (genero == "M") :
    if (idade > 65) or (anos_trabalhados >= 30) or ((idade >=60) and (anos_trabalhados >= 25)):
        print(True)
    else:
        print(False)
elif (genero == "F") :
    if (idade > 60) or (anos_trabalhados >= 30) or ((idade >=60) and (anos_trabalhados >= 25)):
        print(True)
    else:
        print(False)