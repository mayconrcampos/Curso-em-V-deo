minha_tupla = ()
continua = ' '
while continua not in 'nN':
    adiciona = str(input('Digite uma palavra para ser analisada pelo Python: ')).upper()
    continua = str(input('''Quer adicionar mais uma?
     S/N: '''))
    minha_tupla += adiciona,

for item in minha_tupla: #Para cada item na tupla
    print(f"\nNa palavra {item} temos", end=' ') #print Na Palavra {p} temos
    for letra in item: #para cada letra no item
        if letra in 'AEIOU': #Se tiver a letra 'AEIOU' .. Encontrando as VOGAIS.
            print(letra, end=' ') #printa somente elas.
