import random
print('''Sou seu computador...
Acabei de pensar em um número entre 0 a 20...
Será que você consegue adivinhar? ''')
palpite = int(input('Qual é seu palpite? '))
sorteio = random.randint(1,20)
tentativas = 1
while palpite < sorteio:
    print('Você errou pra menos!')
    palpite = int(input('Digite outro número: '))
    tentativas += 1
while palpite > sorteio:
    print('Você errou pra mais!')
    palpite = int(input('Digite outro número: '))
    tentativas += 1
if palpite == sorteio:
    print('Você acertou em {} tentativas!'.format(tentativas))


