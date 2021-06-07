# Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número
# y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la 
# lista.

'''

cant = int (input ('Dígame cuántas palabras tiene la lista: '))
lista = []

for i in range (1, cant+1):
    palabras = input (f'Dígame la palabra {i}: ')
    lista.append(palabras)

print (f'La lista creada es {lista}')

'''

# Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga 
# cuántas veces aparece esa palabra en la lista.

'''

cant = int (input ('Dígame cuántas palabras tiene la lista: '))
lista = []
p = 0

for i in range (1, cant+1):
    palabras = input (f'Dígame la palabra {i}: ')
    lista.append(palabras)
print ()
print (f'La lista creada es {lista}')
print ()
buscar = input ('Dígame la palabra a buscar: ')

for i in lista:
    if buscar == i:
        p = p + 1
if p == 1:
    print (f'La palabra {buscar} aparece una vez en la lista.')
elif p > 1:
    print (f'La palabra {buscar} aparece {p} veces en la lista.')
else:
    print ('La palabra no está en la lista.')

'''

# Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y 
# sustituya la primera por la segunda en la lista.

'''

cant = int (input ('Dígame cuántas palabras tiene la lista: '))
lista = []

for i in range (1, cant+1):
    palabras = input (f'Dígame la palabra {i}: ')
    lista.append(palabras)

print()
print (f'La lista creada es: {lista}')
print ()

sust = input ('Sustituir la palabra: ')
sust_2 = input ('por la palabra: ')

for i in range (len(lista)):
    if sust == lista[i]:
        lista[i] = sust_2

print ()
print (f'La lista es ahora: {lista}')

'''

# Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine
# esa palabra de la lista.

'''
# FORMA EFICIENTE

cant = int (input ('Dígame cuántas palabras tiene la lista: '))
lista = []
borrar = False
v = 0

for i in range (1, cant+1):
    palabras = input (f'Dígame la palabra {i}: ')
    lista.append(palabras)

print()
print (f'La lista creada es: {lista}')
print()

p = input ('Palabra a eliminar: ')

for i in range (len(lista)):
    if p == lista[i]:
        borrar = True
        v = i
if borrar == True:
    del lista[v]

    

print ()1
print (f'La lista es ahora: {lista}')

'''
'''

# FORMA INEFICIENTE

cant = int (input ('Dígame cuántas palabras tiene la lista: '))
lista = []
borrar = False

for i in range (1, cant+1):
    palabras = input (f'Dígame la palabra {i}: ')
    lista.append(palabras)

print()
print (f'La lista creada es: {lista}')
print()

e = input ('Palabra a eliminar: ')


p = 0
while borrar:
    if lista[p] == e:
        borrar = True
    else:
        p = p + 1
del lista[p]
print (lista)

'''

# Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera
# lista los nombres de la segunda lista.



cant = int (input ('Dígame cuántas palabras tiene la lista: '))
lista = []

for i in range (1, cant+1):
    pal = input (f'Dígame la palabra {i}: ')
    lista.append(pal)
    
print()
print (f'La lista creada es: {lista}')
print()

cant_2 = int (input ('Dígame cuántas palabras tiene la lista de palabras a eliminar: '))
lista_2 = [] 

for i in range (1, cant_2+1):
    pal_2 = input (f'Dígame la palabra {i}: ')
    lista_2.append(pal_2)

print ()
print (f'La lista de palabras a eliminar es: {lista_2}')
print ()

for i in range (1, len(lista_2) +1):
    maxx = -9999999
    if i > maxx:
        maxx == i

p = 0
borrar = False

while borrar:
    c = 0
    for i in range (len(lista_2)):
        if lista_2[i] == lista[p]:
            del lista[p]
            c = c + 1
            p = p + 1
        else:
            p = p + 1
    if c == maxx:
        borrar == True   

print 
    

# Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista 
# igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista 
# distinta).

'''

cant = int (input ('Dígame cuántas palabras tiene la lista: '))
lista = []

for i in range (1, cant+1):
    pal = input (f'Palabra número {i}: ')
    lista.append(pal)

print ()
print (f'La lista creada es: {lista}')
print ()

lista_2 = []

for i in range (-cant+1, 0+1):
    l = lista[i]
    lista_2.append(l)
    print (l)

'''