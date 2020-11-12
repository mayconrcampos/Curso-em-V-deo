# Exemplo de Dicionário dentro de uma lista e como fazemos pra acessar
# cada chave e valor.

brasil = []
estado1 = {'uf': 'Santa Catarina', 'sigla': 'SC'}
estado2 = {'uf': 'Rio Grande do Sul', 'sigla': 'RS'}
estado3 = {'uf': 'Paraná', 'sigla': 'PR'}

brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)

print(brasil)
# [{'uf': 'Santa Catarina', 'sigla': 'SC'},
# {'uf': 'Rio Grande do Sul', 'sigla': 'RS'}, {'uf': 'Paraná', 'sigla': 'PR'}]

print(brasil[0])
# {'uf': 'Santa Catarina', 'sigla': 'SC'}

print(brasil[0]['uf'])
# Santa Catarina

print(brasil[0]['sigla'])
# SC

print(f'O melhor estado é {brasil[0]["uf"]} ... ')
print(f'O {brasil[1]["uf"]} e {brasil[2]["uf"]} não prestam.')
# O melhor estado é Santa Catarina ...
# O Rio Grande do Sul e Paraná não prestam.
