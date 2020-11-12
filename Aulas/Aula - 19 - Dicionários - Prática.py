pessoas = {'nome': 'Gustavo',
           'sexo': 'M',
           'idade': 22}

print(pessoas['nome'])
# Gustavo

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# O Gustavo tem 22 anos

print(pessoas.values())
# dict_values(['Gustavo', 'M', 22])

print(pessoas.keys())
# dict_keys(['nome', 'sexo', 'idade'])

print(pessoas.items())
# dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])
# note que ele mostrou uma lista composta de 3 tuplas.

print(pessoas.copy())
print(pessoas)
# {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

for k in pessoas.values():
    print(k)
    # Gustavo
    # M
    # 22

for v in pessoas.keys():
    print(v)
    # nome
    # sexo
    # idade

pessoas['nome'] = 'Maycon'
pessoas['idade'] = 36
for k, v in pessoas.items():
    print(k, v)
    # nome Maycon
    # sexo M
    # idade 36

pessoas['peso'] = 85
for k, v in pessoas.items():
    print(f'O {k} é {v}')
    # O nome é Maycon
    # O sexo é M
    # O idade é 36
    # O peso é 85
