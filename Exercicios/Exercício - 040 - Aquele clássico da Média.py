n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
n3 = float(input('Terceira Nota: '))
n4 = float(input('Quarta Nota: '))
media = (n1 + n2 + n3 + n4) / 4
print('Com as notas {}, {}, {} e {} a média do aluno é {:.1f}'.format(n1, n2, n3, n4, media))
if 7 > media >= 5:
    print('Você não alcançou a média 7 e esta em RECUPERAÇÃO!')
elif media < 5:
    print('Você está REPROVADO!')
else:
    print('PARABÉNS, você alcançou a média 7 e está APROVADO!!!')