classe = str(input("Escolha a classe (guerreiro, mago ou arqueiro): "))
pontos_força = int(input("Digite os pontos de força (de 1 a 20): "))
pontos_magia = int(input("Digite os pontos de magia (de 1 a 20): "))
if (classe == "mago") :
    if (pontos_força <= 10) and (pontos_magia >= 15) :
        print("Pontos de atributo consistentes com a classe escolhida: True")
    else: 
        print("Pontos de atributo não consistentes com a classe escolhida: False")
elif (classe == "guerreiro") :
    if (pontos_força >= 15) and (pontos_magia <= 10) :
        print("Pontos de atributo consistentes com a classe escolhida: True")
    else: 
        print("Pontos de atributo não consistentes com a classe escolhida: False") 
elif (classe == "arqueiro") :
    if (pontos_força > 5) and (pontos_força <= 15) and (pontos_magia >5) and (pontos_magia <= 15) :
        print("Pontos de atributo consistentes com a classe escolhida: True")
    else: 
        print("Pontos de atributo não consistentes com a classe escolhida: False")