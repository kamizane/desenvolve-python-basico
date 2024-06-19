num = str(input("Digite seu núemro:"))
if len(num) == 8:
    num = "9" + num
if num[5] != "-":
    num1 = num[0:5]
    num2 = num[5:9]
    numf = num1 + "-" + num2
print(numf)