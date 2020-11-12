# Essa foi a minha resolução do exercicio,
# Porém o Guanabara fez algo diferente no bloco while...


continuar = ' '
n = 1
lista = []
while n > 0 and continuar not in 'nN':
    n = int(input('Digite um número: '))
    continuar = str(input('Continuar? S/N: '))
    lista += n,

print(f'Você digitou {len(lista)} valores.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print(f'O valor 5 está na lista. ')
else:
    print(f'O valor 5 não está na lista.')