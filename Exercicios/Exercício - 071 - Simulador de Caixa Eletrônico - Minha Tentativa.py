print('==' * 20)
print('             BANCO DOLLYNES           ')
print('==' * 20)
valor = float(input('Qual valor você quer sacar? '))

total = valor
cedula = 100
total_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1

    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula}')

        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1

        total_cedula = 0

        if total == 0:
            break

print('FIM DA TRANSAÇÃO: SEJE BEM VINDOOL AO BANCO DOLLYNES')
print('Pegueie çeu dinheirool e infieie no cool')