import math

base = float(input("\n Digite a base: "))
altura = float(input("\n Digite a altura: "))
perimetro = 2*(base + altura)
area = base * altura
diagonal = math.sqrt(base**2 + altura ** 2)
print("\n Perímetro = ",perimetro)
print("\n Área = ",area)
print("\n Diagonal = ",diagonal)
print("\n")
