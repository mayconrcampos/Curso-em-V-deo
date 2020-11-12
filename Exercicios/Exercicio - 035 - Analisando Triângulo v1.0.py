a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))
if a <= 0 and b <= 0 and c <= 0:
    print('Valor inválido em um dos lados')
elif a + b > c and a + c > b and b + c > a:

    if a == b and a == c and b == c: #Se todos lados forem iguais = Equilatero
        print('Triangulo Equilatero')
    elif a != b and a != c and b != c: #Se todos lados forem diferentes uns dos outros = Escaleno
        print('Triângulo Escaleno')
    elif a == b or a == c or b == c: #Se dois lados forem iguais = Isósceles
        print('Triângulo Isósceles')
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2: #Se a² + b² = c² = Triângulo Retângulo
        print('Triângulo Retângulo')
else:
    print('Não forma um Triângulo')
    #Quando a soma dos ² dos catetos for menor que hipotenusa, não forma um triângulo

#OUTRA FORMA DE SE FAZER O MESMO EXERCÍCIO
l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))
if l1 + l2 > l3:
    if l1 == l2 and l1 == l3:
        print('Triângulo Equilátero')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Triângulo Isósceles')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('Triângulo Escaleno')
    elif l1**2 == l2**2 + l3**2 or l2**2 == l1**2 + l3**2 or l3**2 == l1**2 + l2**2:
        print('Triângulo retângulo')
else:
    print('Não forma um triângulo')

#MANEIRA DE FAZER DO PROF GUANABARA - SOMENTE INDICA SE OS SEGMENTOS PODEM OU NÃO
#FORMAR TRIÂNGULO
print('-='*20)
print('Analisador de Triangulo')
print("-="*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
e3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + R3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR TRIANGULOS')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULOS')
