lista = []
continua = ' '
while continua not in 'nN':
    nome = str(input('NOME: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    continua = str(input('Continua? S/N: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])

print('-=' * 20)
print(f'{"No.":<5}{"NOME":<10}{"MÉDIA":>8}')
for cada, aluno in enumerate(lista):
    print(f'{cada:<5}{aluno[0]:<10}{aluno[2]:^10.1f}')

while True:
    conta = int(input('Mostrar notas de qual aluno? '))
    if conta != 999:
        print(f'As notas de {lista[conta][0]} são: {lista[conta][1]}')
    else:
        print('Fim do programa!')
        break
