velocidade = float(input('Digite a velocidade em Km/h: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO! Você atingiu velocidade superior a 80km/h')
    print('Você deverá pagar uma multa de R$ {}'.format(multa))
print('Parabéns, você atrapalha todo mundo!')
print('Seu carro será recolhido ao ferro velho')
#Quando comando tá no inicio da linha ele sempre será executado.
#Quando tiver indentado, ele depende do resultado de if para que else seja executado

#REPETINDO CÓDIGO SEM OLHAR PRA CIMA

velocidade1 = float(input('Digite a sua velocidade em km/h: '))
if velocidade1 > 80:
    multa1 = (velocidade1 - 80) * 7
    print('MULTADO! Você excedeu o limite de velocidade que é 80km/h')
    print('Você terá que pagar uma multa no valor de R$ {}'.format(multa1))
else:
    print("Parabéns, você merece andar de carroça")
    print('Seu carro será recolhido ao ferro velho')

#Ou pode ser usado else

