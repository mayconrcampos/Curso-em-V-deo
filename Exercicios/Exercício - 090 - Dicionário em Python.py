aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] < 5:
    aluno['situaçao'] = 'Reprovado'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['situaçao'] = 'Recuperação'
elif aluno['media'] >= 7:
    aluno['situaçao'] = 'Aprovado'


print('-=' * 20)
#print(f'Nome do aluno: {aluno["nome"]}.') # Maneira arcaica de fazer o mesmo de baixo
#print(f'A média é {aluno["media"]}.')     # com o maravilhoso laço for.
#print(f'Situação: {aluno["situaçao"]}')

for k, v in aluno.items():
    print(f'{k} é igual a {v}')