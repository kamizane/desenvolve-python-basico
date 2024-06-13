import math
import random
soma=0
n = int(input())
for i in range (0,n):
    a = random.randrange(0,101)
    print(a)
    soma += a 
raiz = math.sqrt(soma)
print(raiz)