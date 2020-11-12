linha = '-' * 40
titulo = 'LISTAGEM DE PREÇOS'
pontos = '.' * 30

print(linha.ljust(40))
print(titulo.center(40))
print(linha.ljust(40))

listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

continua = ' '
while continua not in 'nnNN':
    continua = str(input('''Deseja acrescentar mais itens na lista?'
                          S/N:  '''))
    if continua == 's':
        nome = str(input('Nome do Material: '))
        preco = float(input('Preço: '))
        listagem += nome,
        listagem += preco,


for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    elif pos % 2 != 0:
        print(f'R$ {listagem[pos]:>7.2f}')

print(linha)