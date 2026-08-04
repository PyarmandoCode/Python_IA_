"""
PROGRAMACION ORIENTADA A OBJETOS (POO)
-Paradigma de programación que organiza el código en objetos,
Cada objeto reúne:
- Atributos → características o datos.
- Métodos → acciones o comportamientos
- self -> es una referencia al objeto que se esta ejecutando
"""
class Auto:
    def __init__(self,marca,color,placa,desc):
        self.marca = marca
        self.color = color
        self.placa = placa
        self.desc = desc
    def encender (self):
        print(f"El {self.desc} esta encendido")    
    def apagar (self):
        print(f"El {self.desc} esta apagado")    

#Crear los objetos
auto1 = Auto("Toyota","Rojo","a44656","auto1")        
auto2 = Auto("Volswagen","Azul","3435435","auto2")
auto1.encender()
auto2.apagar()

    