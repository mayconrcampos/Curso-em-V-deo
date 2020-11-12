from datetime import date
anoatual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pessoa)))
    idade = anoatual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Tivemos {} pessoas maiores de idade'.format(totalmaior))
print('Tivemos {} pessoas que são de menor idade'.format(totalmenor))