num = int(input("\n Digite um número de 3 dígitos: "))
c = num//100
d = num % 100 // 10
u = num % 10
num1 = u*100 + d*10 + c
print("\n Número: ",num)
print("\n Invertido: ",num1)
print("\n")
