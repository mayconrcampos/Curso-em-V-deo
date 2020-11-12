nome = str(input('Digite seu nome completo: ')).strip()
a = nome.lower().count('a')
b = nome.lower().find('a')+1
u = nome.lower().rfind('a')+1
print('A Letra A aparece {} vezes na frase'.format(a))
print('A primeira Letra A apareceu na posição {}'.format(b))
print('A última Letra A apareceu na posição {}'.format(u))

# Outra forma de fazer

nome1 = str(input('Digite seu nome completo: ')).upper().strip()
print('A Letra A aparece {} vezes na frase'.format(nome1.count('A')))
print('A primeira Letra A apareceu na posição {}'.format(nome1.find('A')+1))
print('A ultima Letra A apareceu na posição {}'.format(nome1.rfind('A')+1))