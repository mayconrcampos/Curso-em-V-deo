n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite um terceiro número: '))
lista = [n1, n2, n3]
menor = min(lista)
maior = max(lista)
print('Os números são {}. {} e {}'.format(n1, n2, n3))
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))

#Outra maneira de se fazer

nn = int(input('Digite um numero: '))
nnn = int(input('Digite outro: '))
nnnn = int(input('E outro: '))
listinha = [nn, nnn, nnnn]
min = min(listinha)
maxi = max(listinha)
print('O valor mínimo é {} e o máximo é {}'.format(min, maxi))

#Fazendo com as funções condicionais if
num1 = int(input('Digite valor 1: '))
num2 = int(input('Digite valor 2: '))
num3 = int(input('Digite valor 3: '))
#Verificando menor
menor1 = num1
if num2 < num1 and num2 < num3:
    menor1 = num2
if num3 < num1 and num3 < num2:
    menor1 = num3
#Verificando maior
maior1 = num1
if num2 > num1 and num2 > num3:
    maior1 = num2
if num3 > num1 and num3 > num2:
    maior1 = num3
print('O menor valor digitado foi {}'.format(menor1))
print('O maior valor digitado foi {}'.format(maior1))