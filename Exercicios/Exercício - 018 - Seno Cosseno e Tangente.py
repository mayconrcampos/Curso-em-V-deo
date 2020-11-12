import math
angulo = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("O ângulo de {} tem o seno de {:.2f}".format(angulo, seno))
print("O Cosseno é {:.2f}".format(coseno))
print("A Tangente é {:.2f}".format(tangente))

#Chamando somente as funções Seno, Cosseno, Tangente e Radians #

from math import sin, cos, tan, radians
#angulo1 = ("Digite o ângulo que você deseja: ")#
seno1 = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente1 = tan(radians(angulo))
print("Este ângulo possui o SENO de {}".format(angulo, seno1))
print("Cosseno de {:.2f}".format(cosseno))
print("E a Tangente de {:.2f}".format(tangente1))