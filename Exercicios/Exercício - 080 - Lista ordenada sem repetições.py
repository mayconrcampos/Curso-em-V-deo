lista = []

for i in range(0, 5):
    n = int(input('Digite um valor: '))

    if i == 0:
        lista.append(n)
        print('Número adicionado na última posição')

    elif n > max(lista):
        lista.append(n)
        print('Número adicionado na última posição')

    elif n < min(lista):
        lista.insert(0, n)
        print('Número adicionado na posição 0')

    elif n > lista[1] and n < lista[2]:
        lista.insert(2, n)
        print('Número adicionado na posição 1')

    elif n > lista[0] and n < max(lista):
        lista.insert(1, n)
        print('Número adicionado na posição 1')


print('-=' * 30)
print(f'Você digitou {lista}')