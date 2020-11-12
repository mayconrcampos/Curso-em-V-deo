lista = []
lista_pares = []
lista_impares = []

while True:
    n = int(input('Digite um número: '))
    continua = str(input('Quer continuar? S/N: '))
    lista += n,
    if continua in 'nN':
        break

    elif n in lista:
        if n % 2 == 0:
            lista_pares.append(n)
        else:
            lista_impares.append(n)

print('-=' * 30)
print(f'A lista completa é {lista}.')
print(f'A lista de pares é {lista_pares}.')
print(f'A lista de impares é {lista_impares}.')