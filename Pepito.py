# LAas aventuras de Pepito el pastelero

# En la pastelería donde trabaja Pepito se acumularon muchos pedidos y necesita agruparlos de tal manera que 
# sea lo más fácil posible cumplir con todos los cilentes. Se le ocurrió agrupar los pedidos por tipo. Pepito
# sabe que en su pastelería pueden pedir 5 tipos distintos de comida dulce. Pasteles decorados, donas doradas,
# cupcakes de animalitos, tartas de limón y creme brulee.
# La única información del pedido que tiene el pastelero, es el nombre del cliente y el tipo de postre que 
# necesita. Se imagina que son como máximo 100 pedidos. Lo que si sabe, porque Pepito es muy decidido, es que
# el programa tiene que terminar cuando ingresa la palabra FINN. Si, con dos N.
# Pepito necesita que le hagas un programa donde ingrese los pedidos de los clientes y al finalizar le devuelva
# la cantidad de postres que tiene que preparar de cada tipo. Además, es importante que se le informe al 
# pastelero, el postre que más pidieron para poder empezar a hacerlo primero, y el postre que menos pidieron 
# para prepararlo a lo último.

print()
print ('TIPOS DE PEDIDOS')
print ()

print ('Para seleccionar el tipo de pedido que va a realizar, ingrese el número correspondiente: ')
print()

print ('1: Pasteles decorados \r\n2: Donas doradas \r\n3: Cupcakes de animalitos \r\n4: Tartas de limón \r\n5: Creme brulee \r\n(Escriba FINN para finalizar)')

pasteles = []
donas = []
cupcakes = []
tartas = []
creme = []

pedir = True

while pedir: # PIDE EL TIPO DE PEDIDO, EL NOMBRE DEL CLIENTE Y LO AGREGA A LA LISTA CORRESPONDIENTE
    pedido = input ('\r\nIngrese el tipo de pedido: ')
    if pedido == '1':
        nombre = input ('Ingrese el nombre del cliente: ')
        pasteles.append(nombre)
    elif pedido == '2':
        nombre = input ('Ingrese el nombre del cliente: ')
        donas.append(nombre)
    elif pedido == '3':
        nombre = input ('Ingrese el nombre del cliente: ')
        cupcakes.append(nombre)
    elif pedido == '4':
        nombre = input ('Ingrese el nombre del cliente: ')
        tartas.append(nombre)
    elif pedido == '5':
        nombre = input ('Ingrese el nombre del cliente: ')
        creme.append(nombre)
    elif pedido == 'FINN' or pedido == 'Finn' or pedido == 'finn':
        pedir = False
        print ('\r\n¡Hasta luego!')
    else:
        print ('¡Número de pedido incorrecto! Por favor, inténtelo nuevamente.')

for i in range (1, len(pasteles)+1): # CALCULA LA CANTIDAD DE PEDIDOS DE PASTELES DECORADOS
    cant_p = -999999
    if i > cant_p:
        cant_p = i

for i in range (1, len(donas)+1): # CALCULA LA CANTIDAD DE PEDIDOS DE DONAS DORADAS
    cant_d = -99999
    if i > cant_d:
        cant_d = i

for i in range (1, len(cupcakes)+1): # CALCULA LA CANTIDAD DE PEDIDOS DE CUPCAKES DE ANIMALITOS
    cant_c = -99999
    if i > cant_c:
        cant_c = i

for i in range (1, len(tartas)+1): # CALCULA LA CANTIDAD DE PEDIDOS DE TARTAS DE LIMÓN
    cant_t = -99999
    if i > cant_t:
        cant_t = i

for i in range (1, len(creme)+1): # CALCULA LA CANTIDAD DE PEDIDOS DE CREME BRULEE
    cant_cr = -99999
    if i > cant_cr:
        cant_cr = i

maxx = -9999999
minn = 99999999

if cant_p > maxx:  # CALCULA EL TIPO DE PEDIDO MÁS SOLICITADO
    maxx = cant_p
if cant_c > maxx:
    maxx = cant_c
if cant_cr > maxx:
    maxx = cant_cr
if cant_d > maxx:
    maxx = cant_d
if cant_t > maxx:
    maxx = cant_t   

if cant_p < minn: # CALCULA EL TIPO DE PEDIDO MENOS SOLICITADO
    minn = cant_p
if cant_c < minn:
    minn = cant_c
if cant_cr < minn:
    minn = cant_cr
if cant_d < minn:
    minn = cant_d
if cant_t < minn:
    minn = cant_t

print ()
print ('LISTA DE PEDIDOS') # CANTIDAD DE PEDIDOS DE ACUERDO A SU TIPO
print ()
print (f'- Pasteles decorados: {cant_p}')
print (f'- Donas doradas: {cant_d}')
print (f'- Cupcakes de animalitos: {cant_c}')
print (f'- Tartas de limón: {cant_t}')
print (f'- Creme brulee: {cant_cr}')
print()

if maxx == cant_p: # CALCULA LO PRIMERO QUE SE DEBE PREPARAR DE ACUERDO AL PEDIDO MÁS SOLICITADO
    print ('¡Lo primero que debe preparar Pepito son los pasteles decorados!')
elif maxx == cant_c:
    print ('¡Lo primero que debe preparar Pepito son los cupcakes de animalitos!')
elif maxx == cant_d:
    print ('¡Lo primero que debe preparar Pepito son las donas doradas!')
elif maxx == cant_cr:
    print ('¡Lo primero que debe preparar Pepito son los creme brulee!')
elif maxx == cant_t:
    print ('¡Lo primero que debe preparar Pepito son las tartas de limón!')

print()

if minn == cant_p: # CALCULA LO ÚLTIMO QUE SE DEBE PREPARAR DE ACUERDO AL PEDIDO MENOS SOLICITADO
    print ('¡Lo último que debe preparar Pepito son los pasteles decorados!')
elif minn == cant_c:
    print ('¡Lo último que debe preparar Pepito son los cupcakes de animalitos!')
elif minn == cant_d:
    print ('¡Lo último que debe preparar Pepito son las donas doradas!')
elif minn == cant_cr:
    print ('¡Lo último que debe preparar Pepito son los creme brulee!')
elif minn == cant_t:
    print ('¡Lo último que debe preparar Pepito son las tartas de limón!')