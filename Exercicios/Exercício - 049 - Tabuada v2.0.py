from time import sleep
n = int(input('Digite um número para ver sua tabuada: '))
cont = 1
while cont <= 10:
    tabuada = cont * n
    sleep(0.5)
    print('{} x {} = {}'.format(n, cont, tabuada))
    cont += 1
print('Esta aí sua Tabuada de {} usando a função while!'.format(n))

#-------------------------------------------

n = int(input('Numero: '))
for i in range(1, 11):
    tabuada = n * i
    sleep(0.5)
    print('{} x {} = {}'.format(n, i, tabuada))
print('Está aí sua tabuada de {} usando a função For i in Range!'.format(n))