import random
numero = int(input('Adivinhe um numero entre 0 a 5: '))
escolhido = random.randint(0, 5)
if numero == escolhido:
    print('Parabéns! Você acertou na mosca!!!')
else:
    print('Errou!!')
