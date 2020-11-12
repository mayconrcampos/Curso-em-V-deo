#Cria uma lista de convidados e você pode acrescentar quantos quiser nela.

convidados = []
contador = 0
while True:
    x = input("Digite o nome do convidado: ")
    convidados.append(x)
    y = input('Mostra resultado? (sim/não)').lower()
    contador += + 1
    if y == 'sim':
        print('A sua lista tem {} convidados e eles são: {}'.format(contador, convidados))
        break