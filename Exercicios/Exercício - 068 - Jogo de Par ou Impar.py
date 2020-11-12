#A diferença deste jogo pro meu é que este termina quando perde. No meu eu coloquei a opção
#do jogador jogar quantas vezes quiser e encerrar quando quiser.

from random import randint
vitoria = 0
while True:
    n = int(input('Digite um número: '))
    pc = randint(1, 10)
    soma = n + pc
    par_impar = ' '
    while par_impar not in 'PI': #while pra validar resposta. Se digitar outra coisa ele não para de perguntar.
        par_impar = str(input('Par ou Impar? [P/I]: ')).upper()[0].strip()

    print(f'Você jogou {n} e o computador {pc}. Total de {soma}.')
    if par_impar == 'P':

        if soma % 2 == 0:
            print('Você Venceu!')
            vitoria += 1
        else:
            print('Você Perdeu!')
            break
    elif par_impar == 'I':
        if soma % 2 != 0:
            print('Você Venceu!')
            vitoria += 1
        else:
            print('Você Perdeu!')
            break

    print('Vamos jogar Novamente!')
print(f'Você venceu {vitoria} vezes! ')

