cpf  =  str(input("Digite seu cpf (XXX.XXX.XXX-XX): "))
cpf = cpf.replace("-","")
cpf = cpf.replace(".","")
digitos9 = cpf[0:9]
digitoV1 = int(cpf[9:10])
digitoV2 = int(cpf[10:11])
n=0
soma=0
soma2=0
n2 = 0
for i in digitos9:
    i  = int(i)
    soma += i*(10-n)
    n+=1
resultado = soma%11
conta = 11-resultado
if resultado<2:
    if digitoV1 != 0:
        print("Inválido")
        exit()
else:
    if digitoV1 != conta:
        print("invalido")
        exit()
digitos10 = cpf[0:10]
for i in digitos10:
    i  = int(i)
    soma2 += i*(11-n2)
    n2 +=1
resultado2 = soma2%11
conta2 =11-resultado2
if resultado<2:
    if digitoV2 != 0:
        print("Inválido")
        exit()
    else:
        print("Válido")
else:
    if digitoV2 != conta2:
        print("Inválido")
        exit()
    else:
        print("Válido")
