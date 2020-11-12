peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)
print('O seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS, Você está no peso ideal!')
elif imc >= 25 and imc < 30:
    print('Você está com SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('Você está com OBESIDADE!')
elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA!')