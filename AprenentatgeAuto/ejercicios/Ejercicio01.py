# ============================================================
# DOCUMENTACIÓN PANDAS
# ============================================================

# pd.DataFrame() → crea una tabla (DataFrame) a partir de datos como listas o diccionarios.

# iterrows() → recorre el DataFrame fila por fila; devuelve el índice y los datos de cada fila como Series.
# indice → identifica la fila; valor → contiene los datos de esa fila.

# valor['columna'] → accede al valor de una columna concreta de la fila actual.

# .loc[fila, columna] → permite acceder o modificar un valor concreto del DataFrame.
# Ejemplo: df.loc[indice, 'apto'] = True → cambia 'apto' de esa fila a True.

# value_counts() → cuenta cuántas veces aparece cada valor dentro de una columna.
# Ejemplo: df['apto'].value_counts() → cuenta cuántos True y False hay.

# pd.DataFrame(columns=df.columns) → crea un DataFrame vacío manteniendo las mismas columnas que otro DataFrame.

# sort_values('columna') → ordena las filas según los valores de una columna, de menor a mayor.
# ascending=False → cambia el orden a mayor → menor.

# describe() → muestra un resumen estadístico de las columnas numéricas: cantidad, media, desviación,
# mínimo, percentiles (25%, 50%, 75%) y máximo.



import pandas as pd
df = pd.DataFrame ([
    {
        'nombre' : 'Ana',
        'edad' : 23,
        'puntos' : 43,
        'estudios_superiores' : True
    },
    {
        'nombre' : 'Paco',
        'edad' : 21,
        'puntos' : 38,
        'estudios_superiores' : False
    },
    {
        'nombre' : 'Marta',
        'edad' : 19,
        'puntos' : 41,
        'estudios_superiores' : True
    },
    {
        'nombre' : 'Luis',
        'edad' : 25,
        'puntos' : 35,
        'estudios_superiores' : False
    },
    {
        'nombre' : 'Elena',
        'edad' : 22,
        'puntos' : 39,
        'estudios_superiores' : True
    },
    {
        'nombre' : 'Carlos',
        'edad' : 20,
        'puntos' : 36,
        'estudios_superiores' : True
    },
    {
        'nombre' : 'Sara',
        'edad' : 18,
        'puntos' : 34,
        'estudios_superiores' : False
    },
    {
        'nombre' : 'Miguel',
        'edad' : 27,
        'puntos' : 45,
        'estudios_superiores' : False
    },
    {
        'nombre' : 'Lucia',
        'edad' : 21,
        'puntos' : 42,
        'estudios_superiores' : True
    },
    {
        'nombre' : 'Andres',
        'edad' : 24,
        'puntos' : 37,
        'estudios_superiores' : False
    }
])

print("Ejericico de Explorar el DataFrame")
# Solo mostrara las 5 primeras filas
print(df.head()) 

# Muestra las filas,columnas
print(df.shape)

# muestra las columnas
print(df.columns)

# muestra los tipos de df de las columnas
print(df.dtypes)

# muestra info de lo que es cada cosa con mas detalle
print("----------------")
print(df.info())

# muestra un resumen estadístico de las columnas numéricas del DataFrame.
print("----------------")
print(df.describe())


print("Ejercicio 4. Crear una regla de seleccion  y Ejercicio 5 añadir una nueva columna")
# con el indice miramos la fila que queremos acceder y con valor accedemos a esos valores
for indice,valor in df.iterrows():
    if valor['edad'] >= 22 and valor['puntos'] > 40:
        df.loc[indice,'apto'] = True
    elif valor['edad'] < 22 and valor['estudios_superiores'] and valor['puntos'] >= 35:
        df.loc[indice,'apto'] = True
    else:
        df.loc[indice,'apto'] = False

print(df)

print("Ejercicio 6. Contar valors aptas y no aptas")
"""
SOLUCION SIN USAR LA LIBERRIA PANDAS
aptas = 0
no_aptas = 0

for indice,valor in df.iterrows():
    if valor['apto']:
        aptas += 1
    else:
        no_aptas +=1

"""
print(df['apto'].value_counts())


print("Ejercicio 7. Filtrar candidatos aptos")

candidatos_aptos = pd.DataFrame(columns=df.columns) # nos creamos el nuevo df con la misma estructura que el anterior

for indice,valor in df.iterrows():
    if valor['apto']:
        candidatos_aptos.loc[indice] = valor


print(candidatos_aptos)


print("Ejercicio 8. Filtrar candidatos con estudios superiores")

estudios_superiores = pd.DataFrame(columns=df.columns) 

for indice,valor in df.iterrows():
    if valor['estudios_superiores']:
        estudios_superiores.loc[indice] = valor


print(estudios_superiores)
print("Valores de Apto: ")

print(estudios_superiores['estudios_superiores'].value_counts())
print(estudios_superiores['apto'].value_counts())


print("Ejercicio 9. Ordenar los candidatos")

print("De menor a mayor")
print(df.sort_values('puntos'))
print("De mayor a menor")
print(df.sort_values('puntos', ascending=False))

print("Ejercicio 10. Calcular estadísticas")

print(f" Edad media: {df['edad'].mean()}")
print(f" Puntuación media: {df['puntos'].mean()}")
print(f" Puntuacion máxima: {df['puntos'].max()}")
print(f" Puntuacion mínima: {df['puntos'].min()}")
print(f" Edad de la persona mas joven: {df['edad'].min()}")
print(f" Edad de la persona mas mayor: {df['edad'].max()}")

print("Ejercicio 11. Crear una columna de nivel")

for indice,valor in df.iterrows():
    if valor['puntos'] >= 40:
        df.loc[indice, 'nivel'] = 'alto'
    elif valor['puntos'] >= 35 and valor['puntos'] <= 39:
        df.loc[indice,'nivel'] = 'medio'
    else:
        df.loc[indice,'nivel'] = 'bajo'

print(df)

print("Ejercicio 12. Agrupar por nivel")

resultado = df.groupby('nivel').agg(
     personas_num = ('nombre', 'count'),
    edad_media=('edad', 'mean'),
    puntos_medio=('puntos', 'mean')
)

print(f"Resultados: {resultado}")

print("Ejercicio 13. Seleccionar columnsa concretas")
df2 = df[['nombre', 'puntos','apto']]
print(df2)

print("Ejercicio 14. Renombrar columnas")
df2_limpio = df2.rename(columns={'nombre':'Nombre del candidato'})
df2_limpio = df2_limpio.rename(columns={'puntos':'Puntuación'})
print(df2_limpio)

print("Ejercicio 15. Repetir la práctica en google Colab")
