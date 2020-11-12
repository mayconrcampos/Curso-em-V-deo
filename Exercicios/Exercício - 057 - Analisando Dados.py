sexo = str(input('SEXO: [M/F]: ')).upper()
while sexo != 'M' and sexo != 'F':
    print('''Dado Inválido!
    Digite somente M ou F, não existe uma terceira opção.''')
    sexo = str(input('Digite novamente: [M/F]: ')).upper()
if sexo == 'M':
    sexo = 'Masculino'
elif sexo == 'F':
    sexo = 'Feminino'
print('Dado Validado com Sucesso')
print('SEXO: {}'.format(sexo))