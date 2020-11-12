casa = float(input('Valor da casa R$: '))
salario = float(input('Salário do comprador R$: '))
tempo = int(input('Quantos anos de financiamento? '))
jurototal = casa + (casa * 7 / 100)
parcela = jurototal / (tempo * 12)
aprova = salario * 30 / 100
if parcela <= aprova:
    print('Para pagar uma casa de R${:.2f} com 7% de juros, vai lhe custar o preço final de R${:.2f}'.format(casa, jurototal))
    print('Seu salário alcançou 30% da parcela, portanto, o empréstimo pode ser concedido!')
    print('Serão {} anos, e a parcela será será de R${:.2f}'.format(tempo, parcela))
else:
    print('Infelizmente seu CRÉDITO foi negado!')