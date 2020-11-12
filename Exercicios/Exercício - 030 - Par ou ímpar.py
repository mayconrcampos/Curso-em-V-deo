numero = int(input('Digite um número qualquer: '))
if int(numero) % 2 == 0:
    print('Este número é PAR')
else:
    print('Este número é IMPAR')


#outra maneira de fazer é assim
n1 = int(input('Digite outro número: '))
resultado = n1 % 2
if resultado == 0:
    print('Este número é PAR')
else:
    print('Este número é IMPAR')