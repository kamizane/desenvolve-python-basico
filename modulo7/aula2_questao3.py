while True:
    frase = str(input("Digite uma frase (digite 'fim' para encerrar):"))
    frase2 = frase
    frase2 = frase2.lower()
    frase2 = frase2.strip()
    frase2 = frase2.replace(" ","")
    teste = frase2[::-1]
    if frase =="fim":
       exit()
    elif frase2 == teste:
        print("'%s' é um palíndromo" % (frase))
    else:
      print("'%s' não é um palíndromo" % (frase))  
