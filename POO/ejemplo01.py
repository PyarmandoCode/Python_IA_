"""
"""
class Auto:
    #Constructor
    def __init__(self,marca,color,asientos):
        self.marca=marca
        self.color=color
        self.asientos=asientos
        self.velocidad=0
        self.encencido=False
    
    def encender(self):
        self.encencido=True
        print(f"El Auto, {self.marca},esta encendido")    
    
    def apagar(self):
        self.encencido=False    
        print(f"El Auto, {self.marca},esta apagado")    


auto1 = Auto("Toyoya","Negro",4)
auto2 = Auto("Datsun","Amarillo",4)
auto3 = Auto("Volswagen","Blanco",2)

#print(auto3.asientos)
#print(auto3.__dict__)
#print(auto2)
auto2.apagar()