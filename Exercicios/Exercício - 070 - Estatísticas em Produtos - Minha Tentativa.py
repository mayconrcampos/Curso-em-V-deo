total = mais_caro = barato = cont_barato = 0
produto_barato = '' # <--- Variável de controle pra associar Menor Valor com a string produto.
print('-' * 30)
print('        LOJÃO DO POVO          ')
print('-' * 30)
while True:
    produto = str(input('Nome do Produto: ')).capitalize()
    valor = float(input('Preço: R$ '))

    cont_barato += 1
    total += valor

    if valor >= 1000:
        mais_caro += 1

    if cont_barato == 1 or valor < barato:
        barato = valor
        produto_barato = produto

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Continua? ')).upper()

    if continua == 'N':
        break

print('---------- FIM DO PROGRAMA ----------')
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {mais_caro} produto(s) custando mais que R$1000,00')
print(f'O produto mais barato é o(a) {produto_barato} e custou R${barato:.2f}')

# Neste exercício eu montei o programa como está escrito acima, dando todos os resultados corretamente,
# porém, exceto associar o menor valor a variável string produto.
# O qual foi resolvido da seguinte maneira:
# Criou-se duas variaveis além do barato. Criou Cont_barato = 0
# E também o produto_barato = '' , este que vai associar o menor valor a String do produto.

# Colocamos o cont_barato abaixo das inputs afim de iniciar a contagem cont_barato += 1
# E criamos a condicional if cont_barato == 1: <- Ela que vai definir o parâmetro comparativo de mais barato para a variavel valor
# definimos a variavel barato = produto
# definimos a variavel produto_barato = produto <- Aqui se define o parâmetro comparativo de mais barato para a String produto
# Criamos mais uma condicional elif valor < barato:
# definimos a variavel barato = valor <- Aqui define qual valor será o mais barato
# definimos a variavel produto_barato = produto <- Aqui define qual dos produtos será o mais barato.
