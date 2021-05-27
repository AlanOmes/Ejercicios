# Escriba un programa que genere una multiplicación de dos números del 2 al 10 al azar, pregunte por 
# el resultado y diga si se ha dado la respuesta correcta.

import random

'''

num = random.randrange (2, 11)
num_2 = random.randrange (2, 11)
resultado = num * num_2

pregunta = int (input (f'¿Cuánto es {num} x {num_2}?: '))

if pregunta == resultado:
    print ('¡Respuesta correcta!')
else:
    print ('¡Respuesta incorrecta!')

'''

# Amplíe el programa anterior haciendo que el programa pida primero al usuario cuántas 
# multiplicaciones se van a plantear.

'''

cant_preg = int (input ('Número de preguntas: '))

if cant_preg <= 0:
    print ('El número de preguntas debe ser al menos 1.')
else:
    for i in range (cant_preg):
        num = random.randrange (2, 11)
        num_2 = random.randrange (2, 11)
        preg = int (input (f'\r\n¿Cuánto es {num} x {num_2}?: '))
        if preg == num * num_2:
            print ('¡Respuesta correcta!')
        else:
            print ('¡Respuesta incorrecta!')

'''

# Amplíe el programa anterior haciendo que el programa lleve la cuenta de las respuestas correctas e 
# incorrectas e indique la nota correspondiente. Si la nota es igual o mayor que 9, el programa
# felicitará al usuario por el resultado.

'''

cant_preg = int (input ('Número de preguntas: '))

if cant_preg <= 0:
    print ('El número de preguntas debe ser al menos 1.')
else:
    correcta = 0
    for i in range (cant_preg):
        num = random.randrange (2, 11)
        num_2 = random.randrange (2, 11)
        preg = int (input (f'\r\n¿Cuánto es {num} x {num_2}?: '))
        if preg == num * num_2:
            correcta = correcta + 1
            print ('¡Respuesta correcta!')
        else:
            print ('¡Respuesta incorrecta!')
    nota = (10 / cant_preg) * correcta
    nota = round (nota, 2)
    print (f'\r\nHa contestado correctamente {correcta} preguntas.')
    print (f'Le corresponde una nota de {nota}')
    if nota >= 8:
        print ('¡Exámen aprobado!')
    else:
        print ('¡Exámen desaprobado!')

'''

# Escriba un programa que genere una multiplicación de dos números del 11 al 99 al azar, pregunte por
# el resultado y diga si se ha dado la respuesta correcta, si está a menos del 10% del valor correcta
# o a menos del 30%.

num = random.randrange (11, 100)
num_2 = random.randrange (11, 100)
r = num * num_2

rta = int (input (f'¿Cuánto es {num} x {num_2}?: '))
diez = (10 * r) / 100
treinta = (30 * r) / 100

if rta == r:
    print ('¡Respuesta correcta!')
elif rta <= diez:
    print (f'¡Ha fallado por menos del 10%! La respuesta correcta era {r}.')
elif rta <= treinta:
    print (f'¡Ha fallado por menos del 30%! La respuesta correcta era {r}.')
