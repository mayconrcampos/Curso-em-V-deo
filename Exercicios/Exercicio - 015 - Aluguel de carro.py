dias = float(input("Quantos dias alugado? "))
km = float(input("Quantos km foi rodado? "))
pago = (dias * 60) + (km * 0.15)
print("O valor a ser pago por {} dias e {} km rodados será de R${:.2f}".format(dias, km, pago))