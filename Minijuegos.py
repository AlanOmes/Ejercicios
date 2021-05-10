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

# Escriba un programa que simule un juego en el que dos jugadores (Elena y Fernando) tiran dos dados. El que
# saque el valor más alto, gana. Si el valor más alto coincide, decide el otro dado. Si también coincide,
# empatan.



import random

e = random.randrange (1, 7)
e_2 = random.randrange (1, 7)
f = random.randrange (1, 7)
f_2 = random.randrange (1, 7)

total_elena = e + e_2
total_fernando = f + f_2

print (f'Elena ha sacado un {e} y un {e_2}')
print (f'Fernando ha sacado un {f} y un {f_2}')

if total_elena > total_fernando:
    print ('Ha ganado Elena.')
elif total_fernando > total_elena:
    print ('Ha ganado Fernando.')
