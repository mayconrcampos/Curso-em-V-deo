minha_tupla = ()
continua = ' '
while continua not in 'nN':
    adiciona = str(input('Digite uma palavra: ')).upper()
    continua = str(input('Quer acrescentar mais um item? S/N: '))
    minha_tupla += adiciona,

for palavra in minha_tupla:
    print(f'\nA palavra {palavra} temos as consoantes', end=' ')
    for letra in palavra:
        if letra not in 'AEIOU':
            print(f'{letra}', end=' ')