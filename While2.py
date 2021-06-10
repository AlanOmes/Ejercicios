# Escriba un programa que muestre números al azar del 1 al 6 mientras lo pida el usuario.

import random

'''

lanzar = True

while lanzar:
    tiro = input ('\r\nPulse intro para lanzar el dado. Pulse otra tecla e intro para terminar.\r\n') 
    num = random.randrange (1, 7) 
    if tiro == '':
        print (f'Tirada: {num}')
    else:
        lanzar = False
        print ('Programa terminado.')
    
'''

# Amplíe el programa anterior, haciendo que el programa muestre la suma de los números anteriores.

lanzar = True

while lanzar:
    tiro = input ('\r\nPulse intro para lanzar el dado. Pulse otra tecla e intro para terminar.\r\n')
    num = random.randrange (1, 7)
    t = num
    suma = t + num                          
    if tiro == '':
        print (f'Tirada: {t} - Suma: {suma}')
    else:
        lanzar = False
        print ('Programa terminado.')