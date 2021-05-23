# Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares
# desde el primero hasta el segundo.

'''

num = int (input('Escriba un número entero: '))
num_2 = int (input (f'Escriba un número entero mayor o igual que {num}: '))

if num_2 < num:
    print (f'¡Le he pedido un número mayor o igual que {num}!')
else:
    for i in range (num, num_2+1):
        print (f'El número {i} es', end= '')
        if i % 2 == 0:
            print (' par.')
        else:
            print (' impar.')

'''

# Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

'''

num = int (input('Escriba un número mayor que cero: '))

if num <= 0:
    print ('¡Le he pedido un número mayor que cero!')
else:
    print (f'Los divisores de {num} son ', end= '')
    for i in range (1, num+1):
        if num % i == 0:
            print (i, end=' ')

'''

# Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre
# un mensaje cada vez que un número no sea mayor que el primero.

'''

valores = int (input('¿Cuántos valores va a introducir?: '))
print ()

if valores <= 0:
    print ('¡Imposible!')
else:
    num = int (input ('Escriba un número: '))
    pregunta = f'Escriba un número más grande que {num}: '

    for i in range (valores-1):
        num_2 = int (input (pregunta))
        if num_2 <= num:
            print (f'¡{num_2} no es mayor que {num}!')
    print ('Gracias por su colaboración.')

'''
       
# Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre
# un mensaje cada vez que un número no sea mayor que el anterior.

'''

num_actual = -1

valores = int (input('Cuántos valores va a introducir?: '))

if valores <= 0:
    print ('¡Imposible!')
else:
    num = int (input('Escriba un número: '))
    pregunta = f'Escriba un número más grande que {num}: ' 
    
    for i in range (valores-1):
        num_actual = num
        num_actual = int (input(pregunta))
        
'''

# Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos
# negativos ha introducido.

'''

valores = int (input ('¿Cuántos valores va a introducir?: '))
cant_negativos = 0
negativos = False

if valores <= 0:
    print ('¡Imposible!')
else:
    for i in range (1, valores+1):
        num = int (input (f'Escriba el número {i}: '))
        if num < 0:
            negativos = True
            cant_negativos = cant_negativos + 1
    if negativos == True:
        if cant_negativos == 1:
            print (f'Ha escrito {cant_negativos} número negativo.')
        else:
            print (f'Ha escrito {cant_negativos} números negativos.')
    else:
        print ('No ha escrito ningún número negativo.')
    
'''

# Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y diga al final 
# cuántos han sido pares y cuántos impares.

'''

valores = int (input ('¿Cuántos valores va a introducir?: '))
impares = 0
pares = 0

if valores <= 0:
    print ('¡Imposible!')
else:
    for i in range (1, valores+1):
        num = int (input (f'Escriba el valor {i}: '))
        if num % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1
    print (f'Ha escrito {pares} números pares y {impares} números impares.')
    print ('Gracias por su colaboración.')

'''

# Escriba un programa que pida un número entero mayor que 1 y que escriba si el número es un número primo o no.

num = int (input ('Escriba un número entero mayor que 1: '))
primo = True

if num <= 1:
    print ('¡Le he pedido un número entero mayor que 1!')
else:
    for i in range (2, 11):
        if num % i == 0:
            primo = False
    if primo == True:
        print (f'{num} es primo.')
    else:
        print (f'{num} no es primo.')

    
            










