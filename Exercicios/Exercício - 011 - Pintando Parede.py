altura = float(input("altura tem sua parede? "))
largura = float(input("largura tem sua parede? "))
total = altura * largura
tinta = total / 2
print("Sua parede tem {}x{} de dimensão, {}m² e vai precisar de {} L de tinta para pinta-la".format(altura, largura, total, tinta))