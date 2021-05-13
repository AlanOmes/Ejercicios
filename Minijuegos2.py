# Escriba un programa que pida un número de dados y muestre los valores de ese número de dados, al azar.

'''

cant_dados = int (input('Número de dados: \r\n'))

import random

if cant_dados == 0:
    print ('¡Imposible!')
else:
    print ('Dados: ',end= '')
    for dados in range (cant_dados):
      dados = random.randrange (1, 7)
      print (dados, end=' ')

'''

# Escriba un programa que pida un número de jugadores y tire un dado para cada jugador.

cant_jugadores = int (input('\r\nNúmero de jugadores: '))

import random

if cant_jugadores <= 1:
    print ('¡Imposible!')
else:
    for i in range (1, cant_jugadores+1):        
        print (f'Jugador {i}: ', end= '')
        dado = random.randrange(1, 7)
        print (dado)
    
        

  
            
         
            

   
