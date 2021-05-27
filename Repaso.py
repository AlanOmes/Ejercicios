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

año = int (input ('Dígame un año: '))
m = 1
g = año * 622

