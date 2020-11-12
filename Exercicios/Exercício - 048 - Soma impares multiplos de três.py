soma = 0
cont = 1
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma dos {} divisiveis por 3 é igual a {}'.format(cont, soma))