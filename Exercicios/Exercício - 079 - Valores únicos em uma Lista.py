# Programa que pede pra digitar um número, e filtra os valores que serão
# adicionados na lista. Se o numero existir, ele mostra mensagem de valor duplicado,
# Depois pergunta pro usuario se ele quer continuar... Se sim, ele continua pedindo
# pra digitar números... se o usuario digitar n ou N (não).. o programa encerra...
# Após encerrado ele mostra a lista com os numeros digitados, sem os repetidos
# e em ordem crescente.

continua = ' '
lista = []
while continua not in 'nN':
    n = int(input('Digite um valor: '))

    if n not in lista:
        print('Número adicionado com sucesso!')

    for i, v in enumerate(lista):
        if n == v:
            print(f'O número {v} já existe na lista!')
            lista.pop(i)

    continua = str(input('Quer continuar? '))
    lista += n,

print(f'Você digitou {sorted(lista)}')
print(type(lista))
