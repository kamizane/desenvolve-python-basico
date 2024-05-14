idade_usuario = int(input("Digite sua idade: "))
numero_jogos = input("Você ja jogou ao menos 3 jogos?")
numero_vitorias = int(input("Quantos jogos vocÊ já venceu?"))
if (idade_usuario >= 16) and (idade_usuario < 18) and (numero_jogos == "True") and (numero_vitorias >= 1):
    print("Apto para ingressar no clube de jogos de tabuleiro: True")
else:
    print("Não apto para ingressar no clube de jogos de tabuleiro: False")