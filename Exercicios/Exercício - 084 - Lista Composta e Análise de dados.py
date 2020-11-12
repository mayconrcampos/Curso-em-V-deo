
pessoas = []
pesos = []
leves = []
nomespesados = []
nomesleves = []
pesados = []
continuar = ' '

while True:
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    continuar = str(input('Quer continuar? S/N: '))
    pessoas.append(nome)
    pesos.append(peso)

    if continuar in 'nN':
        break

for nome, peso in zip(pessoas, pesos):
    if peso == max(pesos):
        pesados.append(peso)
        nomespesados.append(nome)
    elif peso == min(pesos):
        leves.append(peso)
        nomesleves.append(nome)

print('-= =- ' * 10)
print(f'Você cadastrou {int(len(pessoas))} pessoas.')
print('-= =- ' * 10)
print(f'As pessoas cadastradas são {pessoas}.')
print(f'O mais pesado tem {pesados[0]}kg, que é peso de {nomespesados}.')
print(f'O mais leve tem {leves[0]}kg, que é o peso de {nomesleves}.')


