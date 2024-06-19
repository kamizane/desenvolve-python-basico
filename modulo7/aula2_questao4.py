def validador_senha(senha):
    if len(senha) > 7 and not(senha.isalpha()) and not(senha.isalnum()) and not(senha.islower()) :
        print( "True")
    else:
        print("False")

senha = str(input("Digite sua senha: "))
validador_senha(senha)