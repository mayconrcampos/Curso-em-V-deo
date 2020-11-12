frase = str(input('Digite uma frase: ')).upper()
palavras = frase.split()
print(palavras)
junto = ''.join(palavras)
print(junto)
if junto == junto[::-1]:
    print(junto[::-1])
    print('Palindromo!')
else:
    print('Não é Palindromo!')