minhatupla = ()
n = 0
cont = 1
while cont <= 10:
    n = int(input('Digite um número: '))
    cont += 1
    minhatupla += n,

print(f'Você digitou os valores {minhatupla} ')

print(f'O valor 9 apareceu {minhatupla.count(9)} vezes.') #No caso de count, se eu não digitar nenhum
#valor 9, ele não vai dar erro, apenas diz que digitou 0 vezes.

if 3 in minhatupla:
    print(f'O valor 3 apareceu na {minhatupla.index(3) + 1}º posição.')
else:
    print('O valor 3 não foi digitado!')

print(f'Os valores pares digitados foram.', end=' ')
for c in minhatupla:
    if c % 2 == 0:
        print(c, end=', ')
