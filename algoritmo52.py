import math

lado = float(input("\n Digite o lado do quadrado: "))
perimetro = 4 * lado
area = lado ** 2
diagonal = lado * math.sqrt(2)
print("\n Perímetro: ",perimetro)
print("\n Área: ",area)
print("\n Diagonal: ",diagonal)
print("\n")
