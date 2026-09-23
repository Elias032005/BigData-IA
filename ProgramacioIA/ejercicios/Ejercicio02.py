
#! Ejercicio 1. Listas: COntrol de notas
"""
- Crea una lista llamada notas con cinco calificaciones: 6, 8, 5, 9 y 7.
- Guarda en una variable primera_nota el primer elemento de la lista.
- Guarda en una variable ultima_nota el último elemento de la lista.
- Cambia la segunda nota de la lista por un 10.
- Añade una nueva nota, 8, al final de la lista.
- Guarda en una variable total_notas la cantidad de notas que hay en la lista.
- Muestra por consola la lista final, la primera nota, la última nota y el total de notas.
"""
notas = [6,8,5,9,7]
primera_nota = notas[0]
ultima_nota = notas[4]
notas[1] = 10
notas.append(8)
total_notas = len(notas)
print("Solución del ejercicio 1:")
print(f"Lista final: {notas}" )
print(f"Primera nota: {primera_nota}")
print(f"Última nota: {ultima_nota}")
print(f"Total notas: {total_notas}")


#! Ejercicio 2. Tuplas: Datos fijos de un producto

"""
- Crea una tupla llamada producto con tres datos: nombre del producto, precio y unidades disponibles.
- Por ejemplo: ("teclado", 25.50, 12).
- Guarda cada dato de la tupla en una variable diferente: nombre, precio y unidades.
- Calcula el valor total del stock multiplicando precio por unidades.
- Muestra por consola el nombre del producto, el precio, las unidades y el valor total del stock.
"""

producto = ("pc", 520.50, 10)
nombre = producto[0]
precio = producto[1]
unidades = producto[2]

valor_total = precio * unidades

print(f"El pruducto: {nombre} tiene el precio {precio} y las unidades {unidades} y el valor del stock {valor_total}")

