salario = float(input('Digite seu salário: R$'))
aumento1 = salario + (salario * 10 / 100)
aumento2 = salario + (salario * 15 / 100)
if salario > 1250:
    print('Você ganhou 10% de aumento e vai receber R${:.2f}'.format(aumento1))
else:
    print('Você ganhou 15% de aumento e vai receber RS{:.2f}'.format(aumento2))

#Outra forma de fazer mais simplificada
salario1 = float(input('Digite seu salário: R$'))
if salario1 <= 1250:
    novo = salario1 + (salario1 * 15 / 100)
else:
    novo = salario1 + (salario1 * 10 / 100)
print('Quem ganhava R${:.2f} agora passa a ganhar R${:.2f}'.format(salario1, novo))