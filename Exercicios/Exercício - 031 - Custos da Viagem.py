distancia = float(input('Qual a distância de sua viagem em Km?: '))
abaixo = distancia * 0.50
acima = distancia * 0.45
if distancia <= 200:
    print("Você está prestes a começar uma viagem de {}Km".format(distancia))
    print('O Preço de sua passagem vai lhe custar R${:.2f}'.format(abaixo))
else:
    print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
    print('O preço de sua passagem vai lhe custar R${:.2f}'.format(acima))

#Outra maneira de fazer a mesma coisa, porém a forma de cima é mais intuitiva
d = float(input('Digite a distância de sua viagem em Km: '))
print('Você está prestes a começar uma viagem de {}Km'.format(d))
v = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço de sua passagem vai lhe custar R${:.2f}'.format(v))
