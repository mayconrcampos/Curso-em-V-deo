while True:
    n = int(input('Digite um número para ver sua tabuada: '))

    if n < 0:
        print('Fim do Programa!')
        break

    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')

#Quando for pra fazer tabuada simples, pode se fazer com while,
#Porém se quiser que o programa refaça a pergunta pra digitar o input infinitas vezes.
#Somente abra o loop infinito, submeta uma opção para que possa dar falso, neste caso if n < 0: Se for falso ele
#printa o fim do programa, mas encerra somente com a função break.
#e invoque a função for i in range pra fazer a tabuada que é muito simples.
