
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca,
        self.modelo = modelo

class CochePruebas:
    def __init__ (self):
        self.velocidad = 0

    def acelerar(self):

        self.velocidad +=  10

    def detener(self):
        
        self.velocidad = 0


class Vehiculo(Coche):

    def descubrir(self):
        
        print(f"El coche tiene la marca: {self.marca} con el modelo: {self.modelo}")

class CocheElectrico(Vehiculo):
    def __init__(self,marca,modelo,autonomia_km):
        super().__init__(marca,modelo)
        self.autonomia_km = autonomia_km

    def describir(self):
        descripcion = super().descubrir()
        return f"{descripcion}. Su autonomio es de {self.autonomia_km} km"

class Motor:
    def __init__ (self, modelo):
        self.modelo = modelo

    
    def arrancar(self):
        print("Motor en marcha")

    

class MotorGasolina(Motor):
        def arrancar(self):
            return  f"Motor gasolina en marcha"

class MotorElectrico(Motor):
        def arrancar(self):
            return  f"Motor eléctrico en marcha"
            

# Ejercicio 1. Crear una clase y sus objetos

coche01 = Coche("SEAT", "LEON")
coche02 = Coche("Nissan", "Qashqai")

print(f"El coche01 es de la marca: {coche01.marca} con el modelo: {coche01.modelo}")
print(f"El coche02 es de la marca: {coche02.marca} con el modelo: {coche02.modelo}")

coche01.modelo = "Arona"

print(f"El coche01 es de la marca: {coche01.marca} con el modelo: {coche01.modelo}")


# Ejercicio 2. Modificar el estado de un objeto

coche03 = CochePruebas()
coche04 = CochePruebas()

coche03.acelerar()
coche03.acelerar()
coche04.acelerar()
coche04.acelerar()

print(f"El coche3 tiene: {coche03.velocidad} velocidad" )
print(f"El coche4 tiene: {coche04.velocidad} velocidad" )

coche04.detener()

print(f"El coche3 tiene: {coche03.velocidad} velocidad" )
print(f"El coche4 tiene: {coche04.velocidad} velocidad" )

# Ejercicio 3. Heredar atributos y métodos

coche05 = CocheElectrico("peugeot", "208","1250")
coche05.descubrir()

#Ejercicio 4. Sobrescribir un método heredado

motorgasolina = MotorGasolina("Gasolina 95")
motorelectrico = MotorElectrico("Electrico 150 Kw")

print(motorgasolina.modelo)
print(motorgasolina.arrancar())

print(motorelectrico.modelo)
print(motorelectrico.arrancar())

# Ejercicio 5. Polimorfos

def poner_en_marcha(motor):
    return motor.arrancar()

motores = [motorgasolina, motorelectrico]



for motor in motores:
    print(poner_en_marcha(motor))

# Ejericcio 6. Ampliar un método heredado con super()

coche06 = CocheElectrico("Peugeot", "208", 350)

print(coche06.describir())
print(coche06.marca)
print(coche06.modelo)
print(coche06.autonomia_km)

# Ejercicio 7. Mostrar datos con f-strings

marca = "Seat"
modelo = "Ibiza"
anio = 2020

print(f"El coche es un {marca} {modelo} del año {anio}.")

# Ejercicio 8. Gestionar una entrada incorrecta

try:
    kilometros = int(input("Introduce los kilómetros recorridos: "))
    print("Kilómetros indicados:", kilometros)
except ValueError:
    print("Debes escribir un número entero.")

print("Programa finalizado.")