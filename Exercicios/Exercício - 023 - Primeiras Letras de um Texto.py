from typing import List

cidade = str(input('Digite o nome de uma cidade: ')).strip()
print(cidade[0:5].upper() == "Santo") #Primeiro ele dá o strip (retirando espaço do inicio
#e do fim, passa pra maiusculo #Printa a primeira palavra do caracter 0 ao 4,
# se caso for igual a palavra Santo. Se for diferente ele devolve como valor False.

cidade1 = str(input("Digite o nome da cidade: ")).strip()
if cidade1 == 'Floripa':
     print('Tu éx manezinho da ilha!! Dazumbanho!!')
elif cidade1 == 'Palhoça':
     print('Olhólhó, um Palhocense!! Coza maix kirida!!!')
elif cidade1 == 'São José':
     print('Saum José?!?!?! Tax tolo tax?')
else:
     print('Intãum éx du fim do mundo!')

#Outro jeito de fazer através do if e else:

cidade2 = str(input('Digite o nome de uma cidade: ')).strip() #REMOVE ESPAÇOS DO INICIO E DO FIM DA VARIÁVEL QUE VAI SER DIGITADA NO INPUT
if cidade2[0:5] == 'Santo':
    print('UUUI Santa!!')
else:
    print('Tu nem é santinho')


