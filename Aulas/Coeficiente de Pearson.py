from math import sqrt

"""Calculando Coeficiente de Pearson"""

nascidos_vivos_x = int(input("Nascidos Vivos:(x): "))
taxa_mortalidade_y = int(input("Taxa de Mortalidade:(x): "))
numero_municipios_N = int(input("Número de Cidades:(N): "))
soma_X_vezes_y = int(input("Soma de X * Y: "))
soma_x_ao_quadrado = int(input("Soma de X²: "))
soma_y_ao_quadrado = int(input("Soma de Y²: "))



numerador = soma_X_vezes_y - ((nascidos_vivos_x * taxa_mortalidade_y)/numero_municipios_N)
denominador_01 = soma_x_ao_quadrado - (nascidos_vivos_x**2 / numero_municipios_N)
denominador_02 = soma_y_ao_quadrado - (taxa_mortalidade_y**2 / numero_municipios_N)
print(numerador / (sqrt(denominador_01 * denominador_02)))
