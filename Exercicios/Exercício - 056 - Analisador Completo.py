media = 0
velho = 0
conta_mulher = 0
for p in range(1, 5):
    print('''----- {}ª PESSOA -----'''.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).lower()
    media += idade
    if sexo == 'm':
        if idade == 1:
            velho = idade
        elif idade > velho:
            velho = idade
            nome2 = nome
    if sexo == 'f':
        if idade < 20:
            conta_mulher += 1
print('A média de idade do grupo é de {:.1f} anos'.format(media / 4))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho, nome2.capitalize()))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(conta_mulher))
