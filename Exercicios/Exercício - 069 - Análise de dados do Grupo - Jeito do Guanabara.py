cont = cont_18 = cont_mulher = cont_homens = 0

while True:
    print('-=' * 20)
    print(' VALIDAÇÃO DE DADOS - IDADE E SEXO ')
    idade = int(input('IDADE: '))
    if idade >= 18:
        cont_18 += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO: M/F: ')).upper()
    print('--' * 20)

    if sexo == 'M':
        cont_homens += 1

    elif sexo == 'F' and idade < 20:
        cont_mulher += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continua, S/N? ')).upper()
    print('-=' * 20)

    cont += 1

    if resp == 'N':
        break

print(f'{cont} pessoas foram cadastradas IDADE e SEXO. E destas...')
print(f'{cont_18} pessoas tem acima de 18 anos.')
print(f'{cont_homens} homens foram cadastrados.')
print(f'{cont_mulher} mulheres tem menos de 20 anos.')