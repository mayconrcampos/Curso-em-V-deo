import random
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input("Terceiro Aluno: "))
aluno4 = str(input('Quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

#Chamando somente a função choice

from random import choice
escolhido1 = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido1))