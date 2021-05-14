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

'''

cant_jugadores = int (input('\r\nNúmero de jugadores: '))

import random

if cant_jugadores <= 1:
    print ('¡Imposible!')
else:
    for i in range (1, cant_jugadores+1):        
        print (f'Jugador {i}: ', end= '')
        dado = random.randrange(1, 7)
        print (dado)

'''

# Escriba un programa que pida un número de jugadores, que pida un valor a conseguir, que tire un dado para
# cada jugador y diga si han conseguido obtener el valor.

'''

cant_jugadores = int (input('\r\nNúmero de jugadores: '))

import random

if cant_jugadores <= 0:
    print ('¡Imposible!')
else:
    valor = int (input('Valor a conseguir: '))
    if valor > 6 or valor <= 0:
        print (f'¡Es imposible conseguir un {valor}!')
    else:
        for i in range (1, cant_jugadores+1):
            print (f'Jugador {i}: ', end= '')
            dado = random.randrange (1, 7)
            if dado == valor:
                print (dado, 'CONSEGUIDO')
            else:
                print (dado)
        
''' 

# Escriba un programa que pida un número de dados, que pida un valor a conseguir y que tire después el número
# de dados indicado. El jugador gana si saca el valor ganado



cant_dados = int (input('Número de dados: '))

import random

if cant_dados <= 0:
    print ('¡Imposible!')
else:
    valor = int (input('Valor a conseguir: '))
    if valor > 6 or valor <= 0:
        print (f'¡Es imposible conseguir un {valor}!')
    else:
        print ('Dados: ', end= '')
        for i in range (cant_dados):
            dados = random.randrange (1, 7)
            print (dados, end= ' ')
        
        
                
            