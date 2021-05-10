# Escriba un programa que pida primero un número par y luego un número impar (positivos o negativos). En caso
# de que uno o los dos valores no sea correcto, se mostrará un único aviso.

'''

pregunta_1 = 'Escriba un número par: \r\n'
pregunta_2 = 'Escriba un número impar: \r\n'

par = int (input(pregunta_1))
impar = int (input (pregunta_2))

if par % 2 == 0 and impar % 2 != 0:
    print ('¡Gracias por su colaboración!')
else:
    print ('Uno o más de los valores que ha escrito no son correctos. \r\nEjecute de nuevo el programa para volver a intentarlo.')

'''

# Escriba un programa que pida primero un número par (positivo o negativo) y si el valor no es correcto,
# muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o negativo) y si el valor no es
# correcto, mostrará un aviso.

'''

pregunta_1 = 'Escriba un número par: \r\n'
pregunta_2 = 'Escriba un número impar: \r\n'
preguntar = True

par = int (input (pregunta_1))

if par % 2 == 0:
    impar = int (input (pregunta_2))
    if impar % 2 != 0:
        print ('¡Gracias por su colaboración!')
    else:
        print ('No ha escrito un número impar. \r\nEjecute de nuevo el programa para volver a intentarlo.')
else:
    print ('No ha escrito un número par. \r\nEjecute de nuevo el programa para volver a intentarlo.')

'''

# Escriba un programa que pida primero un número par y a continuación un numero impar (positivos o negativos).
# En caso de que uno o los dos valores no sean correctos, se mostrarán uno o dos avisos.

'''

pregunta_1 = 'Escriba un número par: \r\n'
pregunta_2 = 'Escriba un número impar: \r\n'

par = int (input(pregunta_1))
impar = int (input(pregunta_2))

if par % 2 == 0 and impar % 2 != 0:
    print ('¡Gracias por su colaboración!')
elif par % 2 == 0:
    print ('No ha escrito un número impar. \r\nEjecute de nuevo el programa para volver a intentarlo.')
elif impar % 2 != 0:
    print ('No ha escrito un número par. \r\nEjecute de nuevo el programa para volver a intentarlo.')
else:
    print ('No ha escrito un número par. \r\nNo ha escrito un número impar. \r\nEjecute de nuevo el programa para volver a intentarlo')

'''

# Escriba un programa que pida primero un número par y a continuación un numero impar (positivos o negativos).
# En cada petición, si el valor no es correcto se mostrará un aviso.

'''

pregunta_1 = 'Escriba un número par: \r\n'
pregunta_2 = 'Escriba un número impar: \r\n'

par = int (input(pregunta_1))

if par % 2 == 0:
    impar = int (input (pregunta_2))
    if impar % 2 != 0:
        print ('¡Gracias por su colaboración!')
    else:
        print ('No ha escrito un número impar. \r\nEjecute de nuevo el programa para volver a intentarlo.')
else:
    print ('No ha escrito un número par.')
    impar = int (input (pregunta_2))
    if impar % 2 != 0:
        print ('Ejecute de nuevo el programa para volver a intentarlo.')
    else:
        print ('No ha escrito un número impar. \r\nEjecute de nuevo el programa para volver a intentarlo.')

'''

# Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es
# exacta o no.

'''

numero_1 = 'Escriba el dividendo: \r\n'
numero_2 = 'Escriba el divisor: \r\n'

dividendo = int (input (numero_1))
divisor = int (input (numero_2))

cociente = dividendo // divisor
resto = dividendo % divisor

if resto == 0:
    print (f'La división es exacta. Cociente: {cociente}') 
else:
    print (f'La división no es exacta. Cociente: {cociente}. Resto: {resto}')

'''

# Mejore el programa anterior haciendo que tenga en cuenta que no se puede dividir por cero

'''

numero_1 = 'Escriba el dividendo: \r\n'
numero_2 = 'Escriba el divisor: \r\n'

dividendo = int (input (numero_1))
divisor = int (input (numero_2))

if divisor == 0:
    print ('No se puede dividir por cero.')
else:
    cociente = dividendo // divisor
    resto = dividendo % divisor
    if resto == 0:
        print (f'La división es exacta. Cociente: {cociente}') 
    else:
        print (f'La división no es exacta. Cociente: {cociente}. Resto: {resto}')

'''

# Escriba un programa que pida dos números y que conteste cuál es el menor y cuál el mayor o que escriba que 
# son iguales.

'''

numero_1 = 'Escriba un número: \r\n'
numero_2 = 'Escriba otro número: \r\n'

num_1 = float (input (numero_1))
num_2 = float (input (numero_2))

if num_1 > num_2:
    print (f'Mayor: {num_1}; Menor: {num_2}')
elif num_2 > num_1:
    print (f'Mayor: {num_2}; Menor: {num_1}')
else:
    print ('Los dos números son iguales.')

'''

# Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde
# ese año o cuántos años faltan para llegar a ese año.

'''

año_actual = '¿En qué año estamos?: \r\n'
cualquier_año = 'Escriba un año cualquiera: \r\n'

actual = int (input (año_actual))
año = int (input (cualquier_año))
futuro = año - actual
pasado = actual - año

if año > actual:
    print (f'Para llegar al año {año} faltan {futuro} años.')
elif actual > año:
    print (f'Desde el año {año} han pasado {pasado} años.')
else:
    print ('¡Son el mismo año!')

'''

# Mejore el programa anterior haciendo que cuando la diferencia sea exactamente un año, escriba la frase en
# singular.

'''

año_actual = '¿En qué año estamos?: \r\n'
cualquier_año = 'Escriba un año cualquiera: \r\n'

actual = int (input (año_actual))
año = int (input (cualquier_año))
futuro = año - actual
pasado = actual - año

if año > actual:
    if futuro == 1:
        print (f'Para llegar al año {año} falta 1 año.')
    else:
        print (f'Para llegar al año {año}, faltan {futuro} años.')
elif actual > año:
    if pasado == 1:
        print (f'Desde el año {año} ha pasado 1 año.')
    else:
        print (f'Desde el año {año} han pasado {pasado} años.')
else:
    print ('¡Son el mismo año!')

'''

# Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.

'''

numero_1 = 'Escriba un número: \r\n'
numero_2 = 'Escriba otro número: \r\n'

num_1 = int (input(numero_1))
num_2 = int (input (numero_2))

if num_1 > num_2:
    if num_1 % num_2 == 0:
        print (f'{num_1} es múltiplo de {num_2}')
    else:
        print (f'{num_1} no es múltiplo de {num_2}')
else:
    if num_2 % num_1 == 0:
        print (f'{num_2} es múltiplo de {num_1}')
    else:
        print (f'{num_2} no es múltiplo de {num_1}')

'''

# Mejore el programa anterior haciendo que el programa avise cuando se escriben valores negativos o nulos.

'''

numero_1 = 'Escriba un número: \r\n'
numero_2 = 'Escriba otro número: \r\n'

num_1 = int (input(numero_1))
num_2 = int (input (numero_2))

if num_1 <= 0 or num_2 <= 0:
    if num_1 == 0 or num_2 == 0:
        print ('Lo siento, este programa no admite valores nulos.')
    elif num_1 < 0 or num_2 < 0:
        print ('Lo siento, este programa no admite valores negativos.')
else:
    if num_1 > num_2:
        if num_1 % num_2 == 0:
            print (f'{num_1} es múltiplo de {num_2}')
        else:
            print (f'{num_1} no es múltiplo de {num_2}')
    else:
        if num_2 % num_1 == 0:
            print (f'{num_2} es múltiplo de {num_1}')
        else:
            print (f'{num_2} no es múltiplo de {num_1}')

'''

# Escriba un programa que pida tres números y que escriba si son los tres iguales, si hay dos iguales o si son
# los tres distintos.

'''

pregunta = 'Escriba un número: \r\n'
pregunta_2 = 'Escriba otro número: \r\n'
pregunta_3 = 'Escriba otro número más: \r\n'

num_1 = float (input(pregunta))
num_2 = float (input(pregunta_2))
num_3 = float (input(pregunta_3))

if num_1 == num_2 and num_1 == num_3:
    print ('Ha escrito tres veces el mismo número.')
elif num_1 == num_2 and num_1 != num_3:
    print ('Ha escrito uno de los números dos veces.')
elif num_1 == num_3 and num_1 != num_2:
    print ('Ha escrito uno de los números dos veces.')
elif num_2 == num_3 and num_2 != num_1:
    print ('Ha escrito uno de los números dos veces.')
else:
    print ('Los tres números que ha escrito son distintos.')

'''

# Escriba un programa que pida un año y que escriba si es bisiesto o no.
# Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los 
# múltiplos de 400 sí.

'''      

pregunta = 'Escriba un año y le diré si es bisiesto: \r\n'

año = int (input (pregunta))

if año % 4 == 0 and año % 100 != 0:
    print (f'El año {año} es bisiesto porque es múltiplo de 4 sin ser múltiplo de 100')
elif año % 400 == 0:
    print (f'El año {año} es un año bisiesto porque es múltiplo de 400.')
else:
    print (f'El año {año} no es un año bisiesto.')

'''

# Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la 
# solución.
# Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos 
# los números sean solución. Se recuerda que la fórmula de las soluciones es x = -b / a

'''

print ('ECUACIÓN A X + B = 0')
numero_1 = 'Escriba el valor del coeficiente A: \r\n'
numero_2 = 'Escriba el valor del coeficiente B: \r\n'

a = float (input(numero_1))
b = float (input (numero_2))

if a == 0 and b == 0:
    print ('Todos los números son solución.')
elif a == 0 
    print ('La ecuación no tiene solución.')
else:
    x = -b / a
    ecuacion = a * x + b 
    if ecuacion == 0:
        print (f'La ecuación tiene una solución: {x}')

'''

# Escriba un programa que pida los coeficientes de una ecuación de segundo grado (a x² + b x + c = 0) y
# escriba la solución.
# Se recuerda que una ecuación de segundo grado puede no tener solución, tener una solución única, tener dos 
# soluciones o que todos los números sean solución. Se recuerda que la fórmula de las soluciones cuando hay 
# dos soluciones es x = (-b ± √(b2-4ac) ) / (2a)

'''

numero_1 = 'Escriba el valor del coeficiente A: \r\n'
numero_2 = 'Escriba el valor del coeficiente B: \r\n'
numero_3 = 'Escriba el valor del coeficiente C: \r\n'

a = int (input (numero_1))
b = int (input (numero_2))
c = int (input (numero_3))

'''

# Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo.
# Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que 
# pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un
# círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.
# Se recuerda que el área de un triángulo es base por altura dividido por 2 y que el área de un círculo es Pi 
# (aproximadamente 3,141592) por el radio al cuadrado.

'''

print ('Elija una figura geométrica: \r\na) Triángulo \r\nb) Círculo')
pregunta = '¿Qué figura quiere calcular? (Escriba T o C)\r\n'

figura = input (pregunta)

if figura == 'T' or figura == 't':
    base = float (input ('Escriba la base: \r\n'))
    altura = float (input ('Escriba la altura: \r\n'))
    area = (base * altura) / 2 
    print (f'Un triángulo de base {base} y altura {altura} tiene un área de {area}')
elif figura == 'C' or figura == 'c':
    radio = int (input ('Escriba el radio: \r\n'))
    pi = 3,141592
    area = pi * radio ** 2
    print (f'Un círculo de radio de {radio} tiene un área de {area}')

'''

# Escriba un programa que pida una distancia en centímetros y que escriba esa distancia en kilómetros, metros
# y centímetros (escribiendo todas las unidades).

'''

pregunta = 'Escriba una distancia en centímetros: \r\n'

cm = int (input (pregunta))

if cm == 0:
    print ('Escriba una distancia mayor que cero.')
else:
    km = cm // 100000
    r = cm % 100000
    m = r // 100
    cms = r % 100
    print (f'{cm} centímetros son {km} km {m} m {cms} cm.')
    
'''   

# Mejore el programa anterior haciendo que no se escriban las unidades innecesarias (cuando el valor es cero).

'''

pregunta = 'Escriba una distancia en centímetros: \r\n'

cm = int (input (pregunta))

if cm == 0:
    print ('Escriba una distancia mayor que cero.')
else:
    km = cm // 100000
    r = cm % 100000
    m = r // 100
    cms = r % 100
    if m == 0 and cms == 0:
        print (f'{cm} centímetros son {km} km.')
    elif km == 0 and cms == 0:
        print (f'{cm} centímetros son {m} m.')
    elif km == 0 and m == 0:
        print (f'{cm} centímetros son {cms} cm.')
    elif km == 0:
        print (f'{cm} centímetros son {m} metros y {cms} cm.')       
    elif m == 0:
        print (f'{cm} centímetros son {km} km y {cms} cm.')
    elif cms == 0:
        print (f'{cm} centímetros son {km} km y {m} m.')
    else:
        print (f'{cm} centímetros son {km} km, {m} m y {cms} cm.')

'''

