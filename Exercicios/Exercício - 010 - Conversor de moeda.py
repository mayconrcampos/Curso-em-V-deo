real = float(input("Quantos reais você tem na carteira? R$ "))
dolar = real / 3.27
print("Com R${:.2f} você comprar US${:.2f} dólares".format(real, dolar))
