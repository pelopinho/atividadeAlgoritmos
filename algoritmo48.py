sm = float(input("\n Entre com o salário mínimo: "))
qtdade = float(input("\n Entre com a quantidade em quilowatt: "))
preco = sm/700
vp = preco * qtdade
vd = vp * 0.9
print("\n Preço do quilowatt: ",preco,"\n valor a ser pago: ",vp,"\n valor com desconto: ",vd)