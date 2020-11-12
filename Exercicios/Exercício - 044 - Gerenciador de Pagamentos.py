#--------------------------------------------------------------------------------------------------
#               PROGRAMA ONDE VOCÊ DIGITA O VALOR DA COMPRA E O COMPUTADOR LHE DÁ OPÇÕES
#               DE PAGAMENTO COM DESCONTOS Á VISTA, PARCELADO EM ATÉ 12X NO CARTÃO.
#                         Escrito por Maycon R Campos - 18/05/2019 - v1.0
#--------------------------------------------------------------------------------------------------

print("============LOJAS CAMPOS===========")
preco = float(input('Preço das compras R$: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no débito
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a OPÇÃO?'))
if opcao == 1:
    desconto = preco - (preco * 10 / 100)
    print('A vista tem 10% de desconto, você vai pagar R${:.2f}'.format(desconto))
elif opcao == 2:
    desconto = preco - (preco * 5 / 100)
    print('A vista no Débito tem 5% de desconto, você vai pagar R${:.2f}'.format(desconto))
elif opcao == 3:
    parcela_duas = preco / 2
    print('Você escolheu em 2x, você vai pagar duas parcelas de R${:.2f}'.format(parcela_duas))
elif opcao == 4:
    print('''Você escolheu a opção 4
    Escolha a opção de parcelamento.
    [ 3 ] 3x
    [ 4 ] 4x
    [ 5 ] 5x
    [ 6 ] 6x
    [ 7 ] 7x
    [ 8 ] 8x
    [ 9 ] 9x
    [ 10 ] 10x
    [ 11 ] 11x
    [ 12 ] 12x''')
    opcao = int(input('Qual é a OPÇÃO?'))
    parcelamento = preco / opcao
    if opcao >= 2 and opcao <= 6:
        juro_tres_a_seis = preco + (preco * 5 / 100)
        parcela = juro_tres_a_seis / opcao
        print('Acréscimo de 5%. Você irá pagar {} parcelas de R${:.2f}. Total de {:.2f}'.format(opcao, parcela, juro_tres_a_seis))
    elif opcao >= 7 or opcao <= 12:
        juro_sete_a_doze = preco + (preco * 10 / 100)
        parcela1 = juro_sete_a_doze / opcao
        print('Acréscimo de 10%. Você irá pagar {} parcelas de R${:.2f}'.format(opcao, parcela1, juro_sete_a_doze))
    else:
        print('Opção Inválida! Digite Novamente!')

else:
    print('Opção inválida! Digite novamente.')