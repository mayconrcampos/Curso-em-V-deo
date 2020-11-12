lista = []

for i in range(0, 11):
    n = int(input(f'Digite um valor para a posição {i}: '))
    lista += n,

print('=-' * 30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor é {max(lista)} e está na posição',end=' ')

for i, v in enumerate(lista):
    if lista[i] == max(lista):
        print(f'..{i}',end='')

print(f'\nO menor valor é {min(lista)} e está na posição',end=' ')

for i, v in enumerate(lista):
    if lista[i] == min(lista):
        print(f'..{i}',end='')
