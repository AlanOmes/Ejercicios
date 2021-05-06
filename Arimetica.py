# Escriba un programa que pida dos números y que escriba su media aritmética.
# Se recuerda que la media aritmética de dos números es la suma de ambos números dividida por 2.

'''

pregunta_1 = 'Escriba un número: \r\n'
pregunta_2 = 'Escriba otro numero: \r\n'


numero_1 = float (input (pregunta_1))
numero_2 = float (input (pregunta_2))

resultado = (numero_1 + numero_2) / 2

print (f'La media arimética de {numero_1} y {numero_2} es {resultado}')

'''

# Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de una persona y que calcule su
#  índice de masa corporal (imc).
# Se recuerda que el imc se calcula con la fórmula imc = peso / altura^2 

'''

pregunta_1 = '¿Cuánto pesa?: \r\n'
pregunta_2 = '¿Cuánto mide en metros?: \r\n'

peso = float (input(pregunta_1))
altura = float (input (pregunta_2))

resultado = peso / (altura * altura)
resultado = round (resultado, 2)

print (f'Su imc es {resultado}') 
print ('Un ímc muy alto indica obesidad. Los valores normales de imc están entre 20 y 25,\r\npero esos límites dependen de la edad, del sexo, de la constitución física, etc.')

'''

# Escriba un programa que pida una distancia en pies y pulgadas y que escriba esa distancia en centímetros.
# Se recuerda que un pie son doce pulgadas y una pulgada son 2,54 cm.

'''

cantidad_pies = 'Escriba una cantidad de pies: \r\n'
cantidad_pulgadas = 'Escriba una cantidad de pulgadas: \r\n'

pies = int (input (cantidad_pies))
pulgadas = int (input (cantidad_pulgadas))

pulgada = 2.54
pieses = pulgada * 12

result_pulgada = pulgada * pulgadas
result_pies = pieses * pies 
resultado = result_pulgada + result_pies

print (f'{pies} pies y {pulgadas} pulgadas son {resultado} cm.')

'''

# Escriba un programa que pida una temperatura en grados Celsius y que escriba esa temperatura en grados Fahrenheit.
# Se recuerda que la relación entre grados Celsius (C) y grados Fahrenheit (F) es la siguiente: F = 1,8 * C + 32

'''

pregunta = 'Escriba una temperatura en grados Celcius: \r\n'

celcius = float (input (pregunta))
farenheit = 1.8 * celcius + 32

print (f'{celcius}ºC son {farenheit}ºF')

'''

# Escriba un programa que pida una temperatura en grados Fahrenheit y que escriba esa temperatura en grados Celsius.
# Se recuerda que la relación entre grados Celsius (C) y grados Fahrenheit (F) es la siguiente: C = (F - 32) / 1,8

'''

pregunta = 'Escriba una temperatura en grados Farenheit: \r\n'

farenheit = float (input(pregunta))
celcius = (farenheit - 32) / 1.8
celcius = round (celcius, 2)

print (f'{farenheit}ºF son {celcius}ºC')

'''

# Escriba un programa que pida una cantidad de segundos y que escriba cuántos minutos y segundos son.
'''

pregunta = 'Escriba una cantidad de segundos: \r\n'

s = int (input (pregunta))

m = s // 60
ss = s % 60

print (f'{s} segundos son {m} minutos y {ss} segundos.')

'''

# Escriba un programa que pida una cantidad de segundos y que escriba cuántas horas, minutos y segundos son.

'''

pregunta = 'Escriba una cantidad de segundos: \r\n'

s = int (input(pregunta))

h = s // 3600
r = s % 3600
ss = r % 60
m = r // 60

print (f'{s} segundos son {h} horas, {m} minutos y {ss} segundos.')

'''

# Escriba un programa que pida una cantidad y que escriba cuántas gruesas, docenas y unidades son.
# Se recuerda que una gruesa son doce docenas.

'''

pregunta = 'Escriba una cantidad (entera): \r\n'

u = int (input(pregunta))

g = u // 144
pr = u % 144
d = pr // 12
uu = pr % 12

print (f'{u} unidades son {g} gruesas, {d} docenas y {uu} unidades')

'''