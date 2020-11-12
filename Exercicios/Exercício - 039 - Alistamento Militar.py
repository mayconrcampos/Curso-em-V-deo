from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
sexo = str(input('Digite o sexo: F ou M: ')).lower()
idade = atual - nasc
falta_alistar = 18 - idade
passou_pra_alistar = idade - 18
print('Quem nasceu em {}, tem {} anos neste ano de {}.'.format(nasc, idade, atual))
if sexo == 'm':
        if idade == 18:
            print('PARABENS, este é o ano de seu alistamento!')
        elif idade < 18:
            print('Ainda faltam {} ano(s) pra você se alistar.'.format(falta_alistar))
            sera_ano = atual + falta_alistar
            print('Seu alistamento será no ano de {}'.format(sera_ano))
        elif idade > 18:
            foi_ano = atual - passou_pra_alistar
            print('Era pra você ter se alistado há {} anos atrás.'.format(passou_pra_alistar))
            print('Isto foi pelos idos de {}.'.format(foi_ano))
else:
    print('Você não precisa se alistar')

