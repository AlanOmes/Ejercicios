# Escriba un programa que simule un juego en el que dos jugadores (Álvaro y Bárbara) tiran un dado. El que 
# saque el valor más alto, gana. Si la puntuación coincide, empatan.

'''

import random

a = random.randrange (1, 7)
b = random.randrange (1, 7)

print (f'Alberto ha sacado un {a}')
print (f'Bárbara ha sacado un {b}')

if a > b:
    print ('Ha ganado Alberto.')
elif a == b:
    print ('Han empatado.')
else:
    print ('Ha ganado Bárbara.')

'''

# Escriba un programa que simule un juego en el que dos jugadores (Carmen y David) tiran dos dados. El que 
# saque mayor puntuación total, gana. Si la puntuación total coincide, gana quien haya sacado el dado con el 
# valor más alto. Si el valor más alto también coincide, empatan.

'''

import random

c = random.randrange (1,7)
c_2 = random.randrange (1, 7)
d = random.randrange (1, 7)
d_2 = random.randrange (1,7)

total_carmen = c + c_2
total_david = d + d_2

print (f'Carmen ha sacado un {c} y un {c_2}.')
print (f'David ha sacado un {d} y un {d_2}.')

if total_carmen > total_david:
    print ('Ha ganado Carmen.')
elif total_david > total_carmen:
    print ('Ha ganado David.')
else:
    if c > d and c > d_2:
        print ('Ha ganado Carmen.')
    elif c_2 > d and c_2 > d_2:
        print ('Ha ganado Carmen.')
    elif d > c and d > c_2:
        print ('Ha ganado David.')
    elif d_2 > c and d_2 > c_2:
        print ('Ha ganado David.')
    else:
        print ('Han empatado.')

'''

# Escriba un programa que simule un juego en el que dos jugadores (Gloria y Héctor) sacan tres cartas al azar
# del 1 al 10. Gana el jugador que obtenga la mayor puntuación total, siempre que no se pase de quince, en
# cuyo caso el jugador pierde.

'''

import random 

g = random.randrange (1, 11)
g_2 = random.randrange (1, 11)
g_3 = random.randrange (1, 11)
h = random.randrange (1, 11)
h_2 = random.randrange (1, 11)
h_3 = random.randrange (1, 11)

total_g = g + g_2 + g_3
total_h = h + h_2 + h_3

print (f'Gloria ha sacado un {g}, un {g_2} y un {g_3}.')
print (f'Héctor ha sacado un {h}, un {h_2} y un {h_3}')

if total_g > 15 and total_h > 15:
    print ('No ha ganado nadie.')
elif total_g > 15:
    print ('Ha ganado Héctor.')
elif total_h > 15:
    print ('Ha ganado Gloria.')
else:
    if total_g > total_h:
        print ('Ha ganado Gloria.')
    elif total_h > total_g:
        print ('Ha ganado Héctor.')
    else:
        print ('Han empatado.')

'''

# Escriba un programa que simule el juego Piedra, papel, tijera para dos jugadores (Inés y Juan).

'''

import random 

i = random.randrange (1, 4)
j = random.randrange (1, 4)

print ('Inés ha sacado ', end= '')
if i == 1:
    print ('piedra.')
elif i == 2:
    print ('papel.')
else:
    print ('tijera.')
print ('Juan ha sacado ', end= '')
if j == 1:
    print ('piedra.')
elif j == 2:
    print ('papel.')
else:
    print ('tijera.')

if j == i:
    print ('Han empatado.')
elif i == 1 and j == 3:
    print ('Ha ganado Inés.')
elif i == 2 and j == 1:
    print ('Ha ganado Inés.')
elif i == 3 and j == 2:
    print ('Ha ganado Inés.')
else:
    print ('Ha ganado Juan.')

'''

# Resuelva este ejercicio utilizando la función random.choice(), de manera que se seleccione un valor entre 
# "piedra", "papel" y "tijera".

'''

import random

juego = ['piedra', 'papel', 'tijera']

i = random.choice(juego)
j = random.choice(juego)

print (f'Inés ha sacado {i}.')
print (f'Juan ha sacado {j}.')

if j == i:
    print ('Han empatado.')
elif i == 'piedra' and j == 'tijera':
    print ('Ha ganado Inés.')
elif i == 'papel' and j == 'piedra':
    print ('Ha ganado Inés.')
elif i == 'tijera' and j == 'papel':
    print ('Ha ganado Inés.')
else:
    print ('Ha ganado Juan.')

'''