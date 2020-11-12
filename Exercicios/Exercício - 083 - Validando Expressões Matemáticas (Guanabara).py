# Resolução do exercício pelo Prof Guanabara.
# A Lógica que ele usou é sensacional.

expr = str(input('Digite sua expressão: '))
pilha = []

# Toda string é uma lista, podemos verificar cada item de uma string individualmente.
# Assim como as listas.

for simb in expr:             # Para cada simb da string expr
    if simb == "(":           # Se simb for igual a abre parenteses
        pilha.append("(")     # Adiciona um abre parenteses a lista Pilha
    elif simb == ")":         # Se simb for igual a fecha parenteses, temos duas opções;
        if len(pilha) > 0:    # Se a quantidade de itens da pilha for maior que 0
            pilha.pop()       # Deleta-se o ultimo item dela.
        else:                 # Senão
            pilha.append(')') # Adiciona um fecha parenteses na lista Pilha
            break             # Interrompemos o laço for.


if len(pilha) == 0: # Se o número de itens for 0...
    print('Sua expressão está Válida.')
else:
    print('Sua expressão está Inválida. ')

