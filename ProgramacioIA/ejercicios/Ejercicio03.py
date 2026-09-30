
#! Ejercicio 1: Control de notas
"""
- Mostrar todas las notas.
- Calcular cuántas notas están aprobadas y cuántas suspendidas.
- Calcular la nota media.
- Mostrar la nota más alta y la nota más baja.
- Indicar si la media final está aprobada o suspendida.
"""
notas = [10,8,4,4,2,1,0,7,6,5]
suspendidos = 0
aprobados = 0

nota_alta = 0
nota_baja = 11 # ponermos un 10 porque si ponemos un número inferor a 0 no será útil y no podemos poner 0 porque no sería real 

for nota in notas:
    if nota < 5:
        suspendidos += 1
    else:
        aprobados += 1

    if nota > nota_alta:
        nota_alta = nota

    if nota < nota_baja:
        nota_baja = nota

nota_media = sum(notas)/len(notas)

if nota_media >= 5:
        mensaje = "Arpboada"
else:
        mensaje = "Suspendida"

print("-----------------Ejercicio 1---------------------")
print(f"Notas: {notas}")
print(f"Aprobados: {aprobados}")
print(f"Suspendidos: {suspendidos}")
print(f"Nota mas alta: {nota_alta}")
print(f"Nota mas baja: {nota_baja}")
print(f"Media: {nota_media} y están: {mensaje}")


#! Ejericio 2: Carrito de la compra
"""
- Mostrar cada producto con su precio.
- Calcular el precio total de la compra.
- Aplicar un descuento del 10% si el total supera 20 euros.
- Mostrar el total final que debe pagarse.
Condición: Debe utilizar zip, un acumulador, if y operadores aritméticos.
"""
productos = ['pan', 'leche', 'arroz', 'huevos']
precios = [1.20,0.95,2.10,2.80] 

precio_total = sum(precios)

if precio_total > 20:
     precio_total = precio_total * 0.90
else:
    precio_total = precio_total

print("-----------------Ejercicio 2---------------------")
for producto,precio in zip(productos,precios):
     print(f"Producto: {producto} cuesta: {precio}€")


#! Ejercicio 3: Registro de alumno
"""
- Mostrar todos los datos del alumno.
- Indicar si el alumno aprueba. Aprueba si su nota_media es mayor o igual que 5.
- Indicar si debe recibir un aviso. Recibe aviso si tiene más de 10 faltas.
- Mostrar un mensaje final combinando el resultado académico y el aviso por faltas.
"""

alumno = {
     'nombre' : 'Elias',
     'edad' : 21,
     'curso' : 'BigData&IA',
     'nota_media' : 7.5,
     'faltas' : 16
}

if alumno['nota_media'] >= 5:
     aprueba = True
else:
     apreuba = False

if alumno['faltas'] > 10:
     aviso = "Cuidado con las faltas"
else:   
     aviso = "Vas bien"


print("-----------------Ejercicio 3---------------------")
print(f"nombre: {alumno['nombre']} tiene {alumno['edad']} y está en el curso {alumno['curso']} y tiene una nota media de {alumno['nota_media']} y está aprovado? {aprueba} con {alumno['faltas']} faltas {aviso}")



#! Ejercicio 4: Numero pares, impares y múltiplos
pares = 0
impares = 0
num = 0
for i in range(1,50):
     
    if i % 2 == 0:
         pares += 1
    else:
         impares += 1

    if i % 5 == 0:
         num += 1

print("-----------------Ejercicio 4---------------------")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Multiples de 5: {num}")


#! Ejercicio 5 : Validación de contraseña
"""
- Comprobar si la contraseña tiene al menos 8 caracteres.
- Comprobar si contiene el símbolo @.
- Comprobar que no sea igual a 12345678.
- Si cumple todas las condiciones, mostrar Contraseña válida.
- En caso contrario, mostrar Contraseña no válida.
Condición: Debe utilizar strings, len, operadores lógicos
"""

print("-----------------Ejercicio 5---------------------")
contraseña = input("Dame tu contraseña: ")

if len(contraseña) < 8:
     tamaño_corr = False
else:
     tamaño_corr = True

for n in contraseña:
    if n == "@":
          tiene_arr = True 
    else:
         tiene_arr = False

if contraseña == "123456789":
     igual = True
else:
     igual = False


if tamaño_corr and tiene_arr and not igual:
     mensaje = "Contraseña válida"
else:
     mensaje = "Contraseña no válida"
     
     
print(mensaje)


#! Ejercicio 6: Inventario de productos
"""
- Mostrar todos los productos y sus unidades.
- Mostrar qué productos están agotados.
- Calcular cuántas unidades hay en total.
- Mostrar cuántos productos tienen menos de 10 unidades.
Condición: Debe utilizar diccionarios, items(), acumuladores, contadores
"""
print("-----------------Ejercicio 6---------------------")
inventario = {
     'raton' : 12,
     'teclado' : 5,
     'monitor' : 0,
     'cable' : 25
}
agotados = 0
unidades_totales = 0
menos_10 = 0

for elemento,numero in inventario.items():
    if numero <= 0:
          agotados += 1
    elif numero <= 10:
            menos_10 += 1

    unidades_totales += numero

print(f"Agotados: {agotados}")
print(f"Menos de 10: {menos_10}")
print(f"Unidades totales: {unidades_totales}")

#! Ejercicio 7: Busqueda en una lista
"""
- Recorrer la lista buscando ese nombre.
- Si encuentra el nombre, mostrar en qué posición está.
- Cuando lo encuentre, detener la búsqueda.
- Si no lo encuentra, mostrar Alumno no encontrado.
Condición: Debe utilizar listas, for, enumerate, if, break y una
"""
print("-----------------Ejercicio 7---------------------")
nombre_alumnos = ['jose', 'carlos','marta','carla','josefina', 'carlota', 'marc']
a_buscar = 'marc'

for pos, nombre in enumerate(nombre_alumnos):
    if nombre == a_buscar:
          print(f"Posición: {pos}") 
          break
    else:
        print("Alumno no encontrado")


#! Ejercicio 8: Limpieza de datos
"""
- Recorrer la lista completa.
- Ignorar los números negativos usando continue.
- Sumar solo los números positivos.
- Contar cuántos ceros hay.
- Mostrar la suma final y la cantidad de ceros
"""
print("-----------------Ejercicio 8---------------------")

lista_num = [1,5,2,4,-7,0,9,-7,-8,-4,1,-2,-7,6,-2,-4,-3,7,5,6,4,2,1,5,3,6,9,8,-1,-5,-10]
positivos = []
ceros = 0
for num in lista_num:
     if num <0:
          continue
     else:
        positivos.append(num)

     if num == 0:
        ceros += 1

num_pos = sum(positivos)
print(f"Suma final: {num_pos} y hay {ceros} Ceros")


#!Ejercicio 9: Clasificación de usuarios

print("-----------------Ejercicio 9---------------------")
alumnos = [
    {
        'nombre' : 'carlos',
        'edad' : 18,
        'activo' : True,
        'puntos' : 100
    },

    {
        'nombre' : 'marco',
        'edad' : 16,
        'activo' : True,
        'puntos' : 52
    },

    {
        'nombre' : 'carla',
        'edad' : 19,
        'activo' : False,
        'puntos' : 65
    }
]

for alum in alumnos:
     if alum['activo'] and alum['puntos'] >= 100:
          alum['Premium'] = True
     else:
          alum['Premium'] = False

     if alum['activo'] and alum['puntos'] < 100:
          alum['Estandar'] = True
     else:
          alum['Estandar'] = False

     if not alum['activo']:
          alum['Inactivo'] = True
     else:
          alum['Inactivo'] = False

     if not alum['edad'] <= 18:
          alum['Menor'] = True
     else:
          alum['Menor'] = False

     print(f"ALumno: {alum['nombre']} puntos: {alum['puntos']}")


#!Ejercicio 10: Sistema de intentos
"""
- Recorrer todos los intentos.
- Mostrar cada intento realizado.
- Si un intento está vacío, debe entrar en una condición donde se use pass como marcador.
- Si un intento coincide con el código correcto, mostrar Acceso concedido y terminar el bucle.
- Si después de todos los intentos no se encuentra el código correcto, mostrar Acceso denegado.
"""
print("-----------------Ejercicio 10---------------------")
codigo_correcto = 1234
intentos = [5241,9874,6521,3254,1256,1234]
intento = 0
for inte in intentos:
    intento += 1
    if inte is None:
     pass

    if inte == codigo_correcto:
     print("Acceso concedido")
     break
    else:
     print("Acceso denegado")

    
print(f"Num de intentos: {intento}")


        

#! Ejercicio 11 Diferencias/ simulitudes: i= i+1, i++, ++i, i+=1
print("-----------------Ejercicio 11---------------------")
a = 0
b = 0

for i in range(10):
    a += 1
    b =+ 1 # <-- no funciona
    print(f"A: {a}")
    print(f"B: {b}")
    # en python el i++ e ++i no funcionan

#! Ejercicio 12 "zip" y "enumerate" en iterables
print("-----------------Ejercicio 12---------------------")
habitaciones = ['dormitorio', 'cocina', 'garaje'] 
personas = [2,4,1]

for habitacion,persona in zip(habitaciones,personas):
    print(f"Habitacion: {habitacion} puede tener {persona} personas")

