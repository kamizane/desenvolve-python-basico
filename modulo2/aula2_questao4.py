#4) Uma conta poupança foi aberta com um depósito de R$500,00. Esta conta é remunerada em 1% de juros ao mês. O código a seguir apresenta uma forma de implementação para calcular três meses de acúmulo de juros. Reescreva esse código usando apenas duas variáveis. 
#juros = 1.01
#saldo = 500.0
#rendimento1 = saldo * juros
#rendimento2 = rendimento1 * juros
#rendimento3 = rendimento2 * juros
#print("Após 3 meses meu novo saldo é")
#print(rendimento3)

rendimento = 500 * 1.01
rendimento = rendimento * 1.01
rendimento_final = rendimento * 1.01
print("Após 3 meses meu novo saldo é: %.4f" % (rendimento_final))