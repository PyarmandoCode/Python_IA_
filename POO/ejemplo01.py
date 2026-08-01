"""
"""
class Auto:

    # Constructor
    def __init__(self, marca, color, asientos, velocidad, encendido):
        self.marca = marca
        self.color = color
        self.asientos = asientos
        self.velocidad = velocidad
        self.encendido = encendido

    def encender(self):
        self.encendido = True
        print(f"El Auto {self.marca} está encendido")


    def apagar(self):
        if self.velocidad == 0:
            self.encendido = False
            print(f"El Auto {self.marca} está apagado")
        else:
            print(f"El Auto {self.marca} no puedes apagarlo porque está en movimiento")


auto1 = Auto("Toyota","Negro",4,0,False)
auto2 = Auto("Datsun","Amarillo",4,0,False)
auto3 = Auto("Volkswagen","Blanco",2,4,True)
auto4 = Auto("Chevrolet","Gris",5,2,True)


auto4.apagar()