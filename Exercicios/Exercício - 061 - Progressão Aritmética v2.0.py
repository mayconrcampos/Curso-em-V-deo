primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
n = int(input('Nº de Elementos a Exibir: '))
ultimo = primeiro + (n - 1) * razao
ultimo += 1
for i in range(primeiro, ultimo, razao):
    print(i, end=' ')