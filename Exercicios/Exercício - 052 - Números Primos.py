n = int(input('Digite um número inteiro: '))
tot = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\33[34m', end='')
        tot += 1
    else:
        print('\33[31m', end='')
    print('{} '.format(i), end=' ')
print('\n\33[mO número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('É um número PRIMO!')
else:
    print('Não é PRIMO!')