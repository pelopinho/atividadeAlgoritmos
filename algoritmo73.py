num = float(input("\n Entre com um número com parte fracionária: "))
numi = int(num - 0.5)
numfrac = num - numi
numa = int(num + 0.00001)
print("\n Parte inteira: ",numi)
print("\n Parte fracionária: {:.3f}".format((numfrac + 0.00001)))
print("\n Número arredondado: ",numa)
print("\n")
