from random import randint
from time import sleep
from operator import itemgetter

print('Valores sorteados...')

sorteados = dict()
ranking = dict()

for c in range(1, 5):
    sorteados[f'jogador {c}'] = randint(1, 6)

for jog, num in sorteados.items():
    print(f'O {jog} tirou {num} no dado.')
    sleep(1)

# Este método abaixo é utilizado para ordenar um dict do menor ao maior valor...
# e com o reverse=True, invertendo do maior pro menor.

ranking = sorted(sorteados.items(), key=itemgetter(1), reverse=True)

print('-='* 25)
print('-= RANKING DOS JOGADORES =-')
conta = 0
for v, item in ranking:
    conta += 1
    print(f'{conta}º Lugar:', end=' ')
    print(f'{v} {item}')


