"""
 Practica # 1 Implementar ejercicio el paradigma estructurado VS OO

 Elaborar un programa que calcule el area de un rectangulo
"""

print("\033c")

#Implementar el paradigma estructurado
def area_rectangulo(base,altura):
    return base*altura

print(area_rectangulo(5,3))

#Implementar el paradigma Orientado a Objetos (OO)
class Rectangulos:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def area(self):
        return self.base * self.altura
rect=Rectangulos(5,3) #crear o instanciar un objeto "rectangulo1" de la clase "Rectangulos"
print(rect.area())

    
