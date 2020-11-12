# Agora temos listas dentro de dicionários.

# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado['uf'] = str(input('UF: '))
#     estado['sigla'] = str(input('Sigla: '))
#     brasil.append(estado)                    <- Aqui está o erro
# print(brasil)

# [{'uf': 'Amazonas', 'sigla': 'AM'}, {'uf': 'Amazonas', 'sigla': 'AM'},
# {'uf': 'Amazonas', 'sigla': 'AM'}]
# Deu este erro simplesmente por utilizar append sem o método de fatiamento.
# Para dicionários existe um método interno para fazer isto com o
# método copy().

# -------------- ABAIXO A FORMA CORRETA COM O MÉTODO COPY --------------

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('UF: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print(brasil)
# [{'uf': 'Santa Catarina', 'sigla': 'SC'},
# {'uf': 'Paraná', 'sigla': 'PR'},
# {'uf': 'Goias', 'sigla': 'GO'}]

for e in brasil: # <- Lista brasil
    print(e)
    # {'uf': 'amazonas', 'sigla': 'AM'} <- printa os dicionarios um por vez
    # {'uf': 'goias', 'sigla': 'GO'}
    # {'uf': 'Minas', 'sigla': 'MG'}
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
        # O campo uf tem valor Parana.
        # O campo sigla tem valor PR.
        #
        # O campo uf tem valor Amazonas.
        # O campo sigla tem valor AM.
        #
        # O campo uf tem valor Goias.
        # O campo sigla tem valor GO.

for e in brasil:
    for k in e.keys():
        print(f'Chave {k}')
        # Chave uf
        # Chave sigla
        # Chave uf
        # Chave sigla
        # Chave uf
        # Chave sigla

for e in brasil:
    for v in e.values():
        print(f'valor {v}')
        # valor Paraná
        # valor PR
        # valor São Paulo
        # valor SP
        # valor Amazonas
        # valor AM

