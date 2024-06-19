data = str(input("digite a data de seu nascimento: "))
data = data.replace("/","")
fatia = data[2:4]
fatia = int(fatia)
meses = ["janeiro", "fevereiro ", "março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
print("Você nasceu em  %s de %s de %s." % (data[0:2], meses[fatia-1],data[4:8]))