media = contador = maior = menor = 0 #Declaração das variaveis de controle em uma linha somente.
continua = 's'
while continua in 's': #Aqui esta sendo provocado um True para o programa entrar no Loop.
    n = int(input('Digite um número: ')) #input numero
    continua = str(input('Continua? ')) #input S ou N. Se sim, vai somar as variaveis de controle
    contador += 1  #soma 1              #Senão vai encerrar o programa.
    media += n     #soma + n

    if contador == 1: #Define um parâmetro para encontrar o menor e o maior número
        maior = n     #Cria variavel maior
        menor = n     #Cria a menor
    elif n > maior:   #n precisa ser maior que a variavel maior para que o Python encontre o valor maior
        maior = n
    elif n < menor:   #n precisa ser menor que a variavel menor para que o python encontre o valor menor
        menor = n

print('Você digitou {} números e a média foi {:.2f}'.format(contador, media/contador))
print('O maior número é {} e o menor é {}'.format(maior, menor))






