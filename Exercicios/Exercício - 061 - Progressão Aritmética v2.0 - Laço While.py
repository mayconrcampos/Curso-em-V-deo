n = int(input('Primeiro: '))
razao = int(input('Razão: '))
elementos = int(input('Nº de elementos: '))
ultimo = n + (elementos - 1) * razao
while n <= ultimo:
    n += razao
    print(n, end=' -> ')
print('FIM')

