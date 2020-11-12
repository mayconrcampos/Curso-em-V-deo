from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(2)
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador])) #Itens atrela os itens da tupla com o randint.. São 3 itens da tupla e 3 numeros a serem sorteados pelo randint
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Você Venceu!')
    elif jogador == 2:
        print('Você Perdeu!')
    elif jogador < 0 or jogador > 3:
        print('Jogada Inválida!')
elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('Você Perdeu!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Você Venceu!')
    elif jogador < 0 or jogador > 3:
        print('Jogada Inválida!')
elif computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('Você Venceu!')
    elif jogador == 1:
        print('Você Perdeu!')
    elif jogador == 2:
        print('EMPATE!')
    elif jogador < 0 or jogador > 3:
        print('Jogada Inválida!')
