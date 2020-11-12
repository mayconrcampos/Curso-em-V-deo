from datetime import date
nasci = int(input('Ano de Nascimento do Atleta: '))
ano = date.today().year
atual = ano - nasci
print('O Atleta tem {} anos'.format(atual))
if atual < 9:
    print('Atleta MIRIM!')
elif atual >= 9 and atual < 14:
    print('Atleta INFANTIL!')
elif atual >= 14 and atual < 19:
    print('Atleta JUNIOR!')
elif atual >= 19 and atual < 25:
    print('Atleta SENIOR!')
else:
    print('Atleta MASTER!')


