count = 0
soma = 0
n = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        continue
    soma += n
    count += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(count, soma))