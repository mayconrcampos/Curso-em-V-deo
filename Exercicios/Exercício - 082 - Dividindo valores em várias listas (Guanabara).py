num = list()
pares = list()
impares = list()

while True:
    num.append(int(input('Digite um Número: ')))
    resp = str(input('Quer continuar? S/N: '))
    if resp in 'nN':
        break

for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print('-=' * 30)
print(f'A lista completa é {num}.')
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')