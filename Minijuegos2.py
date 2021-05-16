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

'''

cant_dados = int (input('Número de dados: '))

import random
valor_encontrado = False

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
            if valor == dados:
                valor_encontrado = True
        if valor_encontrado == True:
            print ('El jugador ha perdido.')
        else:
            print ('El jugador ha perdido.')
            
'''      

# Escriba un programa que pida un número de dados, que tire el número de dados indicado y diga cuál es el valor
# más alto obtenido.

'''

import random

cant_dados = int (input('Número de dados: '))
maxx = -999 

if cant_dados <= 0:
    print ('¡Imposible!')
else:
    print ('Dados: ', end= '')
    for i in range (cant_dados):
        dados = random.randrange (1, 7)
        print (dados, end= ' ')
        if dados > maxx:
             maxx = dados
    print (f'El dado más alto es {maxx}')

'''

# Escriba un programa que pida un número de dados y tire esa cantidad para dos jugadores. El jugador que saque
# el valor más alto, gana.

'''

import random

cant_dados = int (input('Número de dados: '))
maxx= -999
maxx_2 = -999

if cant_dados <= 0:
    print ('¡Imposible!')
else:
    print ('Jugador 1: ', end= '')
    for i in range (cant_dados):
        dados = random.randrange (1, 7)
        print (dados, end= ' ')
        if dados > maxx:
            maxx = dados
    print ('\r\nJugador 2: ', end= '')
    for i in range (cant_dados):
        dados = random.randrange (1, 7)
        print (dados, end= ' ')
        if dados > maxx_2:
            maxx_2 = dados
    print ()
    if maxx > maxx_2:
        print ('Ha ganado el jugador 1.')
    elif maxx < maxx_2:
        print ('Ha ganado el jugador 2.')
    else:
        print ('Han empatado.')

'''

# Escriba un programa que pida un número de dados y tire esa cantidad de dados. El primer jugador obtiene un
# punto por cada dado par. El segundo jugador obtiene un punto por cada dado impar. El jugador que saque más 
# puntos, gana.

'''

import random

cant_dados = int (input('Número de dados: '))

pares = 0
impares = 0

if cant_dados <= 1:
    print ('¡Imposible!')
else:
    print ('Dados: ', end= '')
    for i in range (cant_dados):
        dados = random.randrange (1, 7)
        print (dados, end= ' ')
        if dados % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1
    if pares > impares:
        print ('Ha ganado el jugador de los pares.')
    elif pares < impares:
        print ('Ha ganado el jugador de los impares.')
    else:
        print ('Han empatado.')

'''

# Escriba un programa que pida un número de jugadores y tire un dado para cada jugador. El último jugador que
# saque el valor más bajo, gana.

'''

import random

num_jugadores = int(input('Número de jugadores: '))
minn = 7

if num_jugadores <= 1:
    print ('¡Imposible!')
else:
    for i in range (1, num_jugadores+1):
        print (f'Jugador {i}:', end= ' ')
        dado = random.randrange (1, 7)
        print (dado)
        if dado <= minn:
            minn = dado
            j = i 
    print (f'Ha ganado el jugador {j}.')
    
'''

# Escriba un programa que pida un número de dados y tire esa cantidad de dados para dos jugadores. El jugador 
# que saque más puntos sumando su valor más alto y su valor más bajo, gana.

'''

import random

cant_dados = int(input('Número de dados:'))

maxx = 0
minn = 7
maxx_2 = 0
minn_2 = 7

if cant_dados <= 1:
    print ('¡Imposible!')
else:
    print ('Jugador 1: ', end= '')
    for i in range (1, cant_dados+1):
        dados = random.randrange (1, 7)
        print (dados, end= ' ')
        if dados > maxx:
            maxx = dados
        if dados < minn:
            minn = dados 
    total = maxx + minn
    print ()
    print ('Jugador 2: ', end= '')
    for i in range (1, cant_dados+1):
        dados = random.randrange (1, 7)
        print (dados, end= ' ')
        if dados > maxx_2:
            maxx_2 = dados
        if dados < minn_2:
            minn_2 = dados
    total_2 = maxx_2 + minn_2
    print ()
    if total > total_2:
        print ('Ha ganado el jugador 1.')
    elif total < total_2:
        print ('Ha ganado el jugador 2.')
    else:
        print ('Han empatado.')

''' 
# Escriba un programa que pida un número de dados y tire esa cantidad de dados. Si no salen dos dados iguales 
# seguidos, el jugador gana. Si salen, pierde.

'''

import random
perder = False
actual = -1

cant_dados = int (input('Número de dados: '))

if cant_dados <= 1:
    print ('¡Imposible!')
else:
    print ('Dados: ', end= '')
    for i in range (cant_dados):
        dados = random.randrange (1, 7)
        print (dados, end= ' ')
        anterior = actual
        actual = dados
        if anterior == actual:
            perder = True
    print ()
    if perder == True:
        print ('El jugador ha perdido')
    else:
        print ('El jugador ha ganado.')

'''


        
        


        


            