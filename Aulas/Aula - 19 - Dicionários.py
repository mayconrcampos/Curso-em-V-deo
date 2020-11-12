# Aula Teórica

# Estrutura Composta

dados = list()
dados.append('Pedro')

# Cria o elemento 0 e coloca 'Pedro' neste indice.

dados.append(25)

# Cria o elemento 1 e coloca 25 neste indice.

# Dicionários são estruturas de dados semelhantes a listas e tuplas,
# Porém podemos personalizar os indices colocando nomes neles,
# ao invés do índice numérico das listas e tuplas.

# Tuplas são identificadas pelos () parênteses e cada item com uma virgula
# Listas são identificadas pelo [] colchetes...

# Dicionários são identificados por barras {}.

dados = {'NOME': 'Pedro', 'IDADE': 25}

# adiciona uma chave e um valor

dados['sexo'] = 'M'
print(dados)
# {'NOME': 'Pedro', 'IDADE': 25, 'sexo': 'M'}

# deleta elementos pela chave

del dados['IDADE']
print(dados)
# {'NOME': 'Pedro', 'sexo': 'M'}

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}

print(filme.values())
# dict_values(['Star Wars', 1977, 'George Lucas'])

print(filme.keys())
# dict_keys(['titulo', 'ano', 'diretor'])

print(filme.items())
# dict_items([('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])

for key, value in filme.items():
    print(f'O {key} é {value}.')

    # O titulo é Star Wars.
    # O ano é 1977.
    # O diretor é George Lucas.

# Podemos criar dicionarios com listas dentro e vice versa.

locadora = [{'titulo': 'Star Wars',
             'ano': 1977,
             'diretor': 'George Lucas'}, {'titulo': 'Avengers',
                                          'ano': 2012,
                                          'diretor': 'Joss Whedon'}, {'titulo': 'Matrix',
                                                                      'ano': 1999,
                                                                      'diretor': 'Wachovski'}]
for i, item in enumerate(locadora):
    print(i, item)

    # 0 {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
    # 1 {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'}
    # 2 {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachovski'}

print(locadora[1]['titulo']) # Avengers
print(locadora[2]['ano'])    # 1999
print(locadora[0]['diretor'])# George Lucas




