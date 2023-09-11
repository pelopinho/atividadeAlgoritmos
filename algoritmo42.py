import math

angulo = float(input("\n Digite um ângulo em graus: "))
rang = (angulo*math.pi)/180
print("\n Seno: ", math.sin(rang))
print("\n Cosseno: ", math.cos(rang))
print("\n Tangente: ", math.tan(rang))
print("\n Cossecante: ", 1/math.sin(rang))
print("\n Secante: ", 1/math.cos(rang))
print("\n Cotangente: ", 1/math.tan(rang))
print("\n")