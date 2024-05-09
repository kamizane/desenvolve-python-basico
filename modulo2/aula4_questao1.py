#entrada de dados do usuário
comprimento = float(input())
#entrada de dados do usuário
largura = float(input())
#entrada de dados do usuário
preço = float(input())
#a partir dos dados fornecidos, calcula-se a area
area = comprimento*largura
#a partir dos dados fornecidos e o calculo da area, calcula-se o preço total
preço_total = area * preço
#por fim, imprimi-se os resultados
print("O terreno possui %dm2 e custa R$%.2f" % (area, preço_total))
