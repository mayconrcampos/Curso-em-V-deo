"""
Sistema de Caderno de Fiado - Mercearia do seu Zé
"""
import os
from time import sleep
from random import randint

nomes = []
valores = []

opcao = 0

def cadastro():
    print(" --- Cadastrando Cliente e Nota para Pendurar ---")
    nome = input("Digite o primeiro nome: ").capitalize()
    valor = input("Digite o valor da Nota: ")
    os.system("clear")

    if not nome.isdigit() or valor.isdigit():
        valor = float(valor) 
        nomes.append(nome)
        valores.append(valor)
        print(f"Cliente {nome}: Valor: {valor:.2f}")
        sleep(1)
    else:
        print("Nome ou valor inválido!")

    print("\n\n\n\n\n")

def visualizaTodos():
    print(" --- Visualiza Todas as Notas Pendentes --- ")
    conta = 0
    total = 0
    for i in range(len(nomes)):
        if nomes[i]:
            print(f"Nome: {nomes[i]} : Valor(R$): {valores[i]}")
            conta += 1
            total += valores[i]

    if conta == 0:
        print("Nenhum Registro Encontrado!")

    print(".\n.\n.")

    print(f"Total de Notas Pendentes:------------------: {conta} .")
    print(f"Total Pendente de Todos os Clientes:---- R$: {float(total):.2f} .")
    print("\n\n\n\n\n")

def visualizaTotalCliente():
    print(" --- Visualiza Total de Apenas um Cliente --- ")
    nome = input("Digite o nome do Cliente: ").capitalize()

    if nome:
        conta = 0
        total = 0
        for i in range(len(nomes)):
            if nome == nomes[i]:
                print(f"Nome: {nomes[i]} : Valor(R$): {valores[i]}")
                conta += 1
                total += valores[i]
        
        if conta == 0:
            print(".\n.\n.")
            print(f"Nenhum Registro em nome de {nome}.")
        else:
            print(".\n.\n.")
            print(f"Total a Pagar: R${float(total)}")

    else:
        print("Nome Inválido!")

def darBaixa():
    print(" --- Dar Baixa em Dívidas de Clientes --- ")
    nome = input("Digite o nome do Cliente: ").capitalize()

    print("Listando Notas para Dar Baixa ...")
    conta = 0
    total = 0
    for i in range(len(nomes)):
        if nome == nomes[i]:
            print(f"Nome: {nomes[i]} : Valor: R${float(valores[i]):.2f}")
            conta += 1
            total += valores[i]

            nomes[i] = ""
            valores[i] = 0
            
    
    if conta > 0:
        print(".\n.\n.")
        print(f"Total de Débitos Quitados de {nome}: R${float(total):.2f}")
        print(".\n.\n.")
    else:
        print(".\n.\n.")
        print(f"Não Existem Valores em Aberto para o Cliente: {nome}")
        print(".\n.\n.")

while True:
    print("=-=-=-=-=-= Mercearia do seu Zé -=-=-=-=-")
    print("-=-=- Sistema de Vendas a Fiado V1.0 -=-=")
    print("------------------------------------")
    print("1. Cadastro de Cliente e Nota")
    print("2. Visualizar Total em Aberto de Todos os Clientes.")
    print("3. Visualizar Total de um cliente - Pelo Nome.")
    print("4. Dar Baixa - Total de Notas de um Cliente.")
    print("0 . Sair")
    print("------------------------------------")
    opcao = input("Opçao: 1-2-3-4 ou 0 pra Sair: ")
    if opcao.isdigit():
        opcao = int(opcao)
        os.system("clear")

        if opcao == 1:
            cadastro()
        elif opcao == 2:
            visualizaTodos()
        elif opcao == 3:
            visualizaTotalCliente()
        elif opcao == 4:
            darBaixa()
        elif opcao == 0:
            break
        else:
            os.system("clear")
            print(".\n.\n.")
            print("Opção Inválida! Opções: 1-2-3-4 ou 0 pra Sair.")
            print(".\n.\n.")
    else:
        os.system("clear")
        print(".\n.\n.")
        print("Opção Inválida!")
        print(".\n.\n.")
