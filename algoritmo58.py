import math

xnum1 = float(input("\n Entrar com 1° valor: "))
xnum2 = float(input("\n Entrar com 2° valor: "))
xnum3 = float(input("\n Entrar com 3° valor: "))
x = xnum1 + xnum2 / (xnum3 + xnum1) + 2 *(xnum1 - xnum2) +math.log(64.)/math.log(2.)
print("\n X = ",x)
print("\n") 