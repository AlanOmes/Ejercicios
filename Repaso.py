# Escriba un programa que pida un número de días, horas, minutos y segundos y calcule cuántos segundos
# son en total.

'''

d = int (input ('Dígame un número de días: '))
h = int (input ('Dígame un número de horas: '))
m = int (input ('Dígame un número de minutos: '))
s = int (input ('Dígame un número de segundos: '))

ds = d * 86400
hs = h * 3600
ms = m * 60 
s_total = ds + hs + ms + s

print (f'{d} días, {h} horas, {m} minutos y {s} segundos son {s_total} segundos.')

'''

# El calendario musulmán empezó en el año 622 del calendario gregoriano y el año musulmán es algo más
# corto que el año solar. Por ello, una relación aproximada entre un año del calendario musulmán y un
# año del calendario gregoriano es: 33g = 32m + 20526. Escriba un programa que convierta años entre 
# ambos calendarios.

'''

año = int (input ('Dígame un año: '))

'''

# Escriba un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras
# tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si
# no, que no riman.

'''

palabra = input ('Dígame una palabra: ')
palabra_2 = input ('Dígame otra palabra: ')

if palabra [-1] == palabra_2 [-1] and palabra [-2] == palabra_2 [-2] and palabra [-3] == palabra_2 [-3]:
    print (f'Las palabras {palabra} y {palabra_2} riman.')
elif palabra [-1] == palabra_2 [-1] and palabra [-2] == palabra_2 [-2]:
    print (f'Las palabras {palabra} y {palabra_2} riman un poco.')
else:
    print (f'Las palabras {palabra} y {palabra_2} no riman.')

'''

# Escriba un programa que pida tres números y que diga de cada uno si es el más grande, el más pequeño
# o el de en medio.

'''

num = int (input ('Escriba un número: '))
num_2 = int (input ('Escriba otro número: '))
num_3 = int (input ('Escriba otro número: '))

if num > num_2 and num > num_3:
    print (f'{num} es el más grande')
    if num_2 > num_3:
        print (f'{num_2} es el del medio.')
        prnt (f'{num_3} es el más pequeño.')
    else:
        print (f'{num_3} es el del medio.')
        print (f'{num_2} es el más pequeño.')
if num_2 > num and num_2 > num_3:
    print (f'{num_2} es el más grande.')
    if num > num_3: 
        print (f'{num} es el de medio.')
        print (f'{num_3} es el más pequeño.')
    else:
        print (f'{num_3} es el del medio.')
        print (f'{num} es el más pequeño.')
if num_3 > num and num_3 > num_2:
    print (f'{num_3} es el más grande.')
    if num_2 > num:
        print (f'{num_2} es el del medio.')
        print (f'{num} es el más pequeño.')
    else:
        print (f'{num} es el del medio.')
        print (f'{num_2} es el más pequeño.')

'''

# Escriba un programa que pida el valor mínimo, el valor máximo (mayor que el inicial) y el número de
# valores intermedios y escriba la lista de valores enteros correspondiente:


# Escriba un programa que pregunte cuántos números va a introducir, pida esos números y escriba si ha
# escrito algún número par.

'''

cant_num = int (input ('Dígame cuántos números va a escribir: '))
par = False

for i in range (1, cant_num+1):
    num = int (input (f'Dígame el número {i}: '))
    if num % 2 == 0:
        par = True
print ()
if par == True:
    print ('Ha escrito algún número par.')
else:
    print ('No ha escrito ningún número par.')

'''

# Escriba un programa que pida una palabra o número y diga si es o no palíndroma o capicúa

'''

palabra = input ('Dígame algo: ')

if palabra [:] == palabra [::-1]:
    print (f'{palabra} es capicúa o palíndroma.')
else:
    print (f'{palabra} no es capicúa o palíndroma.')

'''

# Escriba un programa que pida una palabra y cree una lista con las letras de esa cadena

'''

frase = input ('Dígame algo: ')
lista = []

for i in range (len(frase)):
    lista.append(frase[i])
print ('La lista creada es', lista)

'''

# Escriba un programa que pida una frase y una vocal y cambie todas las vocales de la frase por la 
# vocal (una forma de hacerlo es convertir la frase en una lista y hacer el cambio en la lista.

vocales = ['a', 'e', 'i', 'o', 'u']

frase = input ('Dígame algo: ')
vocal = input ('Dígame una vocal: ')