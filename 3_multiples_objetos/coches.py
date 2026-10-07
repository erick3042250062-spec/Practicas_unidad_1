"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""
print("\033c")
class Coches:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self.__marca = marca
        self.__color = color
        self.__modelo = modelo
        self.__velocidad = velocidad
        self.__caballaje = caballaje
        self.__plazas = plazas    
    
    def acelerar(self):
        self.velocidad+=1
        print(f"Ahora la velocidad es: {self.__velocidad}")
    def frenar(self):
        self.velocidad-=1
        print(f"Ahora la velocidad es: {self.__velocidad}")
        
## Multiples instancias.
coche1=Coches("VW","Blanco","2022",220,150,5) 
coche2=Coches("Nissan","Azul", "2020",180,150,6)

print(f"El color del coche 1 es {coche1.__color}")
print(f"El color del coche 2 es {coche2.__color}")

for i in range (0,10,1):
    coche1.acelerar()
    
