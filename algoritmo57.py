pr1 = float(input("\n Digite a PR1: "))
pr2 = float(input("\n Digite a PR2: "))
mf = (pr1 + pr2)/2
print("\n Média truncada = ",int((mf - 0.5)+0.001))
print("\n Média arredondada = ",int((mf + 0.001)))
print("\n")