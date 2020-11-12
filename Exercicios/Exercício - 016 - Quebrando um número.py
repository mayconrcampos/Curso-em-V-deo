import math
num = float(input("Digite um valor: "))
valor = math.trunc(num)
print("O valor digitado foi {} e sua porção inteira é {}".format(num, valor))

#OUTRA MANEIRA DE FAZER ESTA MESMA COISA
print("O valor digitado foi {} e sua porção inteira é {}".format(num, math.trunc(num)))
#OUTRA MANEIRA DE FAZER ESTA MESMA COISA
from math import trunc #importou somente a função truncate#
#OUTRA MANEIRA DE FAZER ESTA MESMA COISA
print("O valor digitado foi {} e sua porção inteira é {}".format(num, int(num)))

