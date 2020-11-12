primeiro = int(input('Primeiro Valor: '))
segundo = int(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
    print('''Escolha uma opção...
    [ 1 ] somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair''')
    opcao = int(input('Digite sua Opção: '))
    if opcao == 1:
        soma = primeiro + segundo
        print('{} + {} = {}'.format(primeiro, segundo, soma))

    elif opcao == 2:
        multiplica = primeiro * segundo
        print('{} X {} = {}'.format(primeiro, segundo, multiplica))

    elif opcao == 3:
        if primeiro > segundo:
            maior = primeiro
            print('Entre {} e {}, o número maior é {}'.format(primeiro, segundo, maior))

        elif segundo > primeiro:
            maior = segundo
            print('Entre {} e {}, o número maior é {}'.format(primeiro, segundo, maior))

        elif primeiro == segundo:
            print('Os Números São Iguais')

    elif opcao == 4:
        primeiro = int(input('Digite Outro Primeiro Número: '))
        segundo = int(input('Digite Outro Segundo Número: '))
    elif opcao == 5:
        print('Você Saiu do Programa.')
    else:
        print('Comando Inválido')




