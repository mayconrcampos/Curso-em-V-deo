# maneira tradicional#
co = float(input("Comprimento do cateto oposto: "))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1 / 2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

# MANEIRA IMPORTANDO função MATH#
import math
hi2 = math.hypot(co, ca)
print("A hipotenusa vai medir {:.2f}".format(hi2))

# MANEIRA CHAMANDO SOMENTE A FUNÇÃO HYPOT - Hipotenusa#
from math import hypot

co1 = float(input("Comprimento do cateto oposto: "))
ca1 = float(input('Comprimento do cateto adjacente: '))
hi3 = hypot(co1, ca1)
print("A hipotenusa vai medir {:.2f}".format(hi3))
