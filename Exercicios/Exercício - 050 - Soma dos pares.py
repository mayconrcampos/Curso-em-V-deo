soma = 0
conta = 0
for i in range(1, 7):
    numero = int(input('Digite o {}º número: '.format(i)))
    if numero % 2 == 0:
        soma += numero
        conta += 1
print('Você digitou {} números pares e a soma deles é {}.'.format(conta, soma))



