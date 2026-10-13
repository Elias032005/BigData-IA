# HE USADO IA PORQUE HAY PUNTOS QUE SI NO FUERA POR ELLA NO LO SACABA, todo el código que me ha generado la IA está marcado con comentarios de mas.

import pandas as pd

# 1 Cargar y exploración de datos
df = pd.read_csv('datos_estadistica_alumnos.csv')

print(df.head())

# Ejercicio 2 Media

# Método 1: bucle
puntos = list(df['puntos_prueba'])
suma = 0
for valor in puntos:
    suma += valor

media_bucle = suma / len(puntos)

# Método 2: Funciones
media_funciones = sum(map(lambda x: x, puntos)) / len(puntos)

#Método 3: Pandas
media_pandas = df['puntos_prueba'].mean()

print(f"Media Bucle: {media_bucle}")
print(f"Media Funciones: {media_funciones}")
print(f"Media Pandas: {media_pandas}")

# Ejercicio 3 : Mediana
# Método 1 : Bucle

puntos = list(df["puntos_prueba"])
puntos_ordenados_bucle = []

for _ in range(len(puntos)):  # Repite el proceso tantas veces como elementos había inicialmente; _ no se utiliza.
    x = puntos[0]  # Guarda el primer valor como mínimo provisional.
    posicion_minimo = 0  # Guarda la posición de ese mínimo provisional.

    for i in range(len(puntos)):  # Recorre los índices de la lista actual: desde 0 hasta len(puntos) - 1.
        if puntos[i] < x:  # Comprueba si el valor de esta posición es menor que el mínimo guardado.
            x = puntos[i]  # Actualiza el mínimo con el valor encontrado.
            posicion_minimo = i  # Guarda el índice donde se encontró ese nuevo mínimo.

    puntos_ordenados_bucle.append(x)  # Añade el mínimo al final de la lista de resultados.

    pendientes = []  # Crea una lista vacía para guardar los elementos que quedan.

    for i in range(len(puntos)):  # Recorre de nuevo todos los índices de la lista actual.
        if i != posicion_minimo:  # Comprueba que el índice no sea el del mínimo elegido.
            pendientes.append(puntos[i])  # Copia el elemento a pendientes si no ocupa esa posición.

    puntos = pendientes  # Sustituye puntos por la lista restante, que tiene un elemento menos.


puntos = list(df["puntos_prueba"])
x = 0
for _ in puntos_ordenados_bucle:
   x += 1
   medio = x // 2

if x % 2 == 0:
    mediana_bucle = (puntos[medio-1] + puntos[medio]) / 2
    # print(puntos[medio-1])
    # print(puntos[medio])
else: 
    mediana_bucle = puntos[medio]


# Método 2: Funciones
puntos = list(df["puntos_prueba"])
puntos_ordenados_funciones = sorted(puntos)

medio_funcion = len(puntos_ordenados_funciones) // 2

if len(puntos_ordenados_funciones) % 2 == 0:
    mediana_funcion = (
        puntos_ordenados_funciones[medio_funcion - 1] + puntos_ordenados_funciones[medio_funcion]) / 2
else:
    mediana_funcion = puntos_ordenados_funciones[medio_funcion]


    
# Método 3: Pandas
puntos_ordenados_pandas = df.sort_values('puntos_prueba', ascending=True)
mediana_pandas = puntos_ordenados_pandas['puntos_prueba'].median()

print(f"Mediana Bucle : {mediana_bucle}")
print(f"Mediana Funcion: {mediana_funcion}")
print(f"Mediana Pandas: {mediana_funcion}")


# Ejercicio 4. Moda
# Método 1 : Bucles
puntos = list(df['puntos_prueba'])
frecuencias = {}

for i in puntos:
    if i in frecuencias:
        frecuencias[i] += 1
    else:
        frecuencias[i] = 1

num_frecuencia_mayor = -1
for punto in frecuencias:
    if  frecuencias[punto] > num_frecuencia_mayor:
        num_frecuencia_mayor = frecuencias[punto]
        moda_bucle = punto


# Método 2: Funciones
moda_funciones = max(set(puntos), key=lambda x : puntos.count(x))
# set(puntos) crea un conjunto con cada valor distinto de puntos.
# max() recorre esos valores y pasa cada uno como x a la función lambda.
# La lambda devuelve puntos.count(x): las apariciones de x en la lista original.
# key indica que max() debe comparar esos conteos.
# max() devuelve el valor x asociado al conteo mayor, no el conteo.
# El valor devuelto se guarda en moda_funciones.
# Método 3: Pandas


# Método 3: Pandas
moda_pandas = df['puntos_prueba'].mode()
print(f"Moda Bucle {moda_bucle}")
print(f"Moda Funciones {moda_funciones}")
print(f"Moda Pandas {moda_pandas}")


# Ejercicio 5: Desviación de cada dato respeto a la media
# Método 1: Bucle
desviacion_bucle = []
for i in puntos: 
     x = i - media_bucle
     desviacion_bucle.append(x)


# Método 2: Funciones
puntos = list(df["puntos_prueba"])
desviacion_funciones = list(map(lambda x : x - media_funciones, puntos))

# Método 3: Pandas
df['desviación'] = df['puntos_prueba'] - media_pandas


print(f"Desviación Bucle: {desviacion_bucle}")                                                                                              
print(f"Desviación Funciones: {desviacion_funciones}")
print(f"Desviación Pandas: {df['desviación']}")    

# Ejercicio 6: Varianza

# Método 1 Bucle
diferencias_cuadrado_bucle = []
for i in desviacion_bucle:
    x = (i) **2
    diferencias_cuadrado_bucle.append(x)

vuelta_bucle = 0
resultado_bucle = 0
for i in diferencias_cuadrado_bucle:
    vuelta_bucle += 1
    resultado_bucle += i

varianza_bucle = resultado_bucle / vuelta_bucle

# Método 2: Fucniones
varianza_funciones = sum(map(lambda x : x**2, desviacion_funciones)) / len(desviacion_funciones)

# Método 3: Pandas

varianza_pandas = df['puntos_prueba'].var(ddof=0)

print(f"Varianza Bucle: {varianza_bucle}")
print(f"Varianza Funciones: {varianza_funciones}")
print(f" Varianza Pandas: {varianza_pandas}")
