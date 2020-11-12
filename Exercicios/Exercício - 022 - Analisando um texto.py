nome = str(input('Digite seu nome completo: ')).strip() #Não contabiliza espaços antes e depois da palavra
print("Analisando seu nome...")
print('Seu nome em maiúsculas é {}'.format(nome.upper())) #passa tudo pra maiusculo
print('Seu nome em minúsculas é {}'.format(nome.lower())) #passa tudo pra minusculo
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) # Len Conta total de caracteres#
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0]))) #Outra forma mais simples
#Passo a passo#
# 1 - Atribui a divisão dos nomes criando uma lista, sendo a posição 0 o primeiro nome, a posição 1 o segundo nome e assim por diante.
# 2 - printa na tela o primeiro nome
# 3 - Conta a quantidade de letras deste primeiro nome

nome1 = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome ...')
print('Seu nome em maiúsculas é {}'.format(nome1.upper()))
print('Seu nome em minúsculas é {}'.format(nome1.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome1) - nome1.count(' ')))
separado = nome1.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separado[0], len(separado[0])))
print('Seu segundo nome é {} e ele tem {} letras'.format(separado[1], len(separado[1])))
print('Seu terceiro nome é {} e ele tem {} letras'.format(separado[2], len(separado[2])))
