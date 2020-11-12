# Escrevi o programa abaixo lendo o enunciado, porém, vendo a resolução do mesmo,
# Descobri que há um sistema de validação mais eficiente que..
# Enquanto a pessoa não digita a informação correta, a pergunta se repete ad infinitum.
# É a estrutura while sendo utilizada localmente para validar apenas uma pergunta,
# sem a necessidade de criar uma estrutura de decisão com ifs e elifs.

# Ficando assim:

# sexo = ' '                    #Cria=se a variável com uma string vazia.
# while sexo not in 'MF':       #Enquanto a variável não conter a letra M e F maiúscula...
# sexo = str(input('SEXO: M/F: ') #Esta pergunta será repetida até que M ou F seja digitado.


# É sensacional! Pule para a o exercício 69 feito pelo Guanabara pra ver essa nova estrutura funcionando.
# Este exercício aqui tá correto e funcionando, porém é um modo ineficiente pra validação de dados.

cont18 = cont_homens = cont_mulheres = cont = 0

while True:
    print('-=' * 20)
    print('-------CADASTRO DE IDADE E SEXO-------')
    print('-=' * 20)
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO - [M/F]: ')).upper()
    print('-=' * 20)
    cont += 1
    if idade >= 18:
        cont18 += 1

        if idade < 0:
            break

    if sexo == 'M':
        cont_homens += 1

    elif sexo == 'F' and idade < 20:
        cont_mulheres += 1

    continua = str(input('Quer continuar? [S/N]')).upper()
    if continua == 'N':
        break

print('-=' * 20)
print(f'Foram cadastrados {cont} pessoas. Destas....')
print(f'Temos {cont18} pessoas acima de 18 anos.')
print(f'Foram cadastrados {cont_homens} homens.')
print(f'{cont_mulheres} mulheres tem menos de 20 anos.')
print('-=' * 20)