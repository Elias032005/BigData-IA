"""
Ejercicio 1: Valores guardados en variables
a = 3
b = 5
c = a + b
 
print("a =", a)
print("b =", b)
print("c =", c)


Variable | Valor previsto |Tipo previsto |
---------|----------------|---------------|
    a           3                int
    b           5                int
    c           8                int
    
    
Ejercicio 2. Una variable puede cambiar de valor
edad = 15
edad = edad + 1
doble = edad * 2
 
print("edad =", edad)
print("doble =", doble)
  
  Variable | Valor previsto |Tipo previsto |
---------|----------------|---------------|

   edad         16              int
   doble        24              int
   
   
Ejercicio 3. Copiar valores entre variables
    a = 10
    b = a
    a = a + 5
    c = b + 2
     
    print("a =", a)
    print("b =", b)
    print("c =", c)

     Variable | Valor previsto |Tipo previsto |
    ---------|----------------|---------------|
        b          10               int
        a          15               int
        c          12               int
        
        
Ejercicio 4. Calcular un porcentaje
precio = 12
porcentaje_iva = 21
iva = precio * porcentaje_iva / 100
total = precio + iva
 
print("precio =", precio)
print("porcentaje_iva =", porcentaje_iva)
print("iva =", iva)
print("total =", total)

      Variable | Valor previsto |Tipo previsto |
    ---------|----------------|---------------|
      precio        12              int
   porcentaje_iva  21               int
   iva              2,52            float
   total            14,52           float
    
    
 Ejercicio 5. División normal y división entera
a = 17
b = 5
 
division = a / b
division_entera = a // b
resto = a % b
 
print("division =", division)
print("division_entera =", division_entera)
print("resto =", resto)

      Variable | Valor previsto |Tipo previsto |
    ---------|----------------|---------------|
    division       3,4              float
    division_entera  3              int
    resto           2               int


Ejercicio 6. Texto y números
nombre = "Laura"
edad = 16
texto_edad = "16"
mensaje = nombre + " tiene " + texto_edad + " años"
 
print("nombre =", nombre)
print("edad =", edad)
print("texto_edad =", texto_edad)
print("mensaje =", mensaje)

       Variable | Valor previsto |Tipo previsto |
    ---------|----------------|---------------|
       nombre      Laura             str
       edad         16               int
       texto_edad   "16"             str
       mensaje     "Laura tiene 16 años" str
        

Ejercicio 7. Comparaciones
a = 8
b = 12
 
mayor = a > b
iguales = a == b
distintos = a != b
 
print("mayor =", mayor)
print("iguales =", iguales)
print("distintos =", distintos)

       Variable | Valor previsto |Tipo previsto |
    ---------|----------------|---------------|
        mayor           False           bool
        iguales         False           bool
        distintos       True            bool
        
        
 Ejercicio 8. Operadores lógicos
edad = 17
tiene_permiso = True
 
puede_entrar = edad >= 16 and tiene_permiso
necesita_permiso = edad < 18
sin_permiso = not tiene_permiso
 
print("puede_entrar =", puede_entrar)
print("necesita_permiso =", necesita_permiso)
print("sin_permiso =", sin_permiso)

       Variable | Valor previsto |Tipo previsto |
    ---------|----------------|---------------|
    puede_entrar True               bool
    necesita_permiso    True        bool
    sin_permiso     False           bool
    
    Ejercicio 9. None y reasignación
dato = None
numero = 4
 
dato = numero * 3
numero = dato / 2
 
print("dato =", dato)
print("numero =", numero)

       Variable | Valor previsto |Tipo previsto |
    ---------|----------------|---------------|
        dato           12         int 
        numero          6.0         float   

    Ejercicio 10. Mezcla de operadores
a = 6
b = 4
c = 2.0
 
resultado = (a + b) * c / 4
comparacion = resultado == 5
 
print("a =", a)
print("b =", b)
print("c =", c)
print("resultado =", resultado)
print("comparacion =", comparacion)

       Variable | Valor previsto |Tipo previsto |
    ---------|----------------|---------------|
        a           6               int
        b           4               int
        c           2.0             float
        resultado   5               float
        comparacion True            bool
        

Ejercicios de recerca
Investiga y responde con tus propias palabras. Añade ejemplos sencillos de Python cuando sea posible.
a) ¿Qué es "castear"? Pon ejemplos y aplicaciones.
    Convertir un dato de un tipo a otro
    edad = "25"
    edad = int(edad)
    print(type(edad))
    
b) ¿Qué ocurre cuando aplicamos estos operadores a strings y booleanos? Pon ejemplos de cada caso.
OPERADOR    | CON STRING                         | CON BOOLEAN
------------|------------------------------------|---------------------------
+           | Une textos                         | Suma como 1/0
-           | Error                              | Operación numérica posible
*           | Repite el texto                    | Operación numérica posible
/           | Error                              | Operación numérica posible
==          | Compara textos                     | Compara booleanos
!=          | Compara si son diferentes          | Compara si son diferentes
<, >        | Compara el orden de los textos     | Compara False < True
and         | Evalúa valores truthy/falsy        | Operador lógico
or          | Evalúa valores truthy/falsy        | Operador lógico
not         | Evalúa truthy/falsy                | Invierte True/False
  
    
"""