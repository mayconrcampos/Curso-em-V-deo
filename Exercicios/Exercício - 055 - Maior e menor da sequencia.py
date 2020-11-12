maior = 0
menor = 0
for p in range(1 , 5):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso é {}kg'.format(maior))
print('O menor peso é {}kg'.format(menor))
