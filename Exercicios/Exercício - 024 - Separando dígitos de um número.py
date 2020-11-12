#Separando um numero de até 4 dígitos em unidade, dezena, centena, milhar.
# num = int(input('Informe um número: '))
# n = str(num)
# print('Analisando o numero {}'.format(num))
# print('Unidade {}'.format(n[3]))
# print('Dezena {}'.format(n[2]))
# print('Centena {}'.format(n[1]))
# print('Milhar {}'.format(n[0]))

#Este algoritmo acima não dá certo pra valores com menos de 4 dígitos, dá erro.
#Por isso para corrigir esse problema, segue abaixo outra maneira de fazer esta tarefa
#logo abaixo

#Mesmo algoritmo, porém escrito de outra forma
num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(u))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))

# ---------------------------- Repetindo código sem copiar
num = int(input('Digite um número '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}', num)
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))