
with open('arquivo.txt', 'r') as entrada:

    palavras = [palavra.strip() for linha in entrada for palavra in linha.split() if palavra.isalpha()]


with open('palavras.txt', 'w') as saida:

    for palavra in palavras:
        saida.write(palavra + '\n')


with open('palavras.txt', 'r') as saida:
    conteudo = saida.read()
    print(conteudo)
