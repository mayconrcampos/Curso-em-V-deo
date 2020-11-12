from random import randint
minha_tupla = ()
conta = 1
continua = ' '
while continua not in 'nN':
    print(f'Foi sorteado o {conta}º número...')
    continua = str(input("Deseja acrescentar mais um? S/N: "))
    minha_tupla += randint(1, 5),
    conta += 1

print(f'Foram Sorteados {len(minha_tupla)} números.')
print('-=-=' * 10)
print(f'Os números são: {minha_tupla}')
print('-=-=' * 10)
print(f'O maior número é {max(minha_tupla)}')
print('-=-=' * 10)
print(f'O menor número é {min(minha_tupla)}')
print('-=-=' * 10)
print(f'A soma dos valores é {sum(minha_tupla)}')
print('-=-=' * 10)
print(f'A média dos valores é {sum(minha_tupla) / len(minha_tupla):.2f}')
print('-=-=' * 10)
print(f'O tipo é {type(minha_tupla)}')
print('-=-=' * 10)
print('Fim da Análise de Tupla!')