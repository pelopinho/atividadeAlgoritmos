deposito = float(input("\n Entre com o depósito: "))
taxa = float(input("\n Entre com a taxa de juros: "))
valor = (deposito * taxa) / 100
total = deposito + valor
print("\n Rendimentos: ",valor, "\n Total: ",total)
print("\n")