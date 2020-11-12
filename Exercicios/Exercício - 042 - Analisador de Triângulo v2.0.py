l1 = int(input('Digite lado 1: '))
l2 = int(input('Digite lado 2: '))
l3 = int(input('Digite lado 3: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("Pode formar um triângulo.")
    if l1 == l2 and l1 == l3 and l2 == l3:
        print('Triângulo EQUILÁTERO.')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print("Triângulo ESCALENO.")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Triângulo ISÓSCELES.')
    elif l1**2 == l2**2 + l3**2 or l2**2 == l1**2 + l3**2 or l3**2 == l1**2 + l2**2:
        print('Triângulo RETÂNGULO.')
else:
    print('Não forma um triângulo.')
