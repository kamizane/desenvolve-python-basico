nome_do_produto_1 = str(input("Digite o nome do produto 1: "))
preço_unitario_produto_1 = float(input("Digite o preço unitário do produto 1: "))
quantidade_produto_1 = int(input("Digite a quantidade do produto 1: "))

nome_do_produto_2 = str(input("Digite o nome do produto 2: "))
preço_unitario_produto_2 = float(input("Digite o preço unitário do produto 2: "))
quantidade_produto_2 = int(input("Digite a quantidade do produto 2: "))



nome_do_produto_3 = str(input("Digite o nome do produto 3: "))
preço_unitario_produto_3 = float(input("Digite o preço unitário do produto 3: "))
quantidade_produto_3 = int(input("Digite a quantidade do produto 3: "))

total = (preço_unitario_produto_1 * quantidade_produto_1) + (preço_unitario_produto_2 * quantidade_produto_2) + (preço_unitario_produto_3 * quantidade_produto_3)

print("Total: R$%.2f" % (total))