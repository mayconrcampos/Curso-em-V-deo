from time import sleep
for c in range(50, 0, -2):
    sleep(0.2)
    print(c, end=' ')
print('Acabou!')


#Outra maneira de fazer
#for c in range(2, 51, 2):
#    print('.', end=' ')
#    print(c, end=' ')
#print('Números pares!')