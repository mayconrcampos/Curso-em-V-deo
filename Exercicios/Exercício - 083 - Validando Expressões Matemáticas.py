# A princípio achei que seria impossível resolver esse exercício, e nem tentei,
# Fui direto para as respostas, mas porém, fiquei decepcionado, pois achei que seria
# muito difícil, pois matemática sempre me apavora. Até que descobri que utilizaram
# uma simples ferramenta de comparação ao transformar o input em string.
# Em seguida coloca-se uma condicional if comparando o número de abre parênteses com,
# fecha parênteses.... Se for igual o número, é válida. Se não, é Inválida.
# Decepcionado, mas aprendi mais uma coisa no dia de hoje.


n = str(input('Digite sua expressão: '))
if n.count('(') == n.count(')'):
    print('Esta expressão é válida!')
else:
    print('Expressão Inválida!')