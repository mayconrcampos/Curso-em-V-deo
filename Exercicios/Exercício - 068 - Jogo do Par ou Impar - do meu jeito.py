from random import randint
jogada = 0
vitoria = 0
derrota = 0
while True:
    print('-=' * 15)
    n = int(input('Digite um número de 1 a 10: 0 pra sair:  '))
    par_ou_impar = str(input('Par ou Impar? [P/I], ou digite nada pra parar: ')).upper()
    print('-=' * 15)
    pc_num = randint(1, 10)
    soma = n + pc_num
    jogada += 1
    if n != 0:
        if n > 0 and n <= 10:
            if par_ou_impar != '':
                if par_ou_impar == 'P':
                    if soma % 2 == 0:
                        print('-=' * 15)
                        print(f'Você Jogou {n} e o computador jogou {pc_num}.')
                        print(f'Total deu {soma}, deu PAR!')
                        print('Você Venceu!')
                        print('-=' * 15)
                        vitoria += 1
                    else:
                        print('-=' * 15)
                        print(f'Você Jogou {n} e o computador jogou {pc_num}.')
                        print(f'Total deu {soma}, deu IMPAR!')
                        print('Você Perdeu!')
                        print('-=' * 15)
                        derrota += 1
                elif par_ou_impar == 'I':
                    if soma % 2 != 0:
                        print('-=' * 15)
                        print(f'Você jogou {n} e o computador jogou {pc_num}.')
                        print(f'Total deu {soma}, deu impar.')
                        print('Você Venceu!')
                        print('-=' * 15)
                        vitoria += 1
                    else:
                        print('-=' * 15)
                        print(f'Você Jogou {n} e o computador jogou {pc_num}.')
                        print(f'Total deu {soma}, deu PAR!')
                        print('Você Perdeu!')
                        print('-=' * 15)
                        derrota += 1
            else:
                print('Você terminou o jogo!')
                break
        else:
            print('Você Optou por Terminar o Jogo!')
            break
    else:
        print('Você Optou por Terminar o Jogo!')
        break

print(f'GAME OVER! Você jogou {jogada - 1} vezes, venceu {vitoria} e perdeu {derrota}.')
