quant = int(input("\n Digite a quantidade de fitas: "))
valAluguel = float(input("\n Digite o valor do aluguel: "))
fatAnual = quant/3 * valAluguel * 12
print("\n Faturamento anual: ", fatAnual)
multas = valAluguel * 0.1 * (quant/3)/10
print("\n Multas mensais: ",multas)
quantFinal = quant - quant * 0.02 + quant/10 * quant * 1.08
print("\n Quantidade de fitas no final do ano: {:.2f} ".format(quantFinal))
print("\n")