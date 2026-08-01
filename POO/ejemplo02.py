marca = "Toyota"
color= "Rojo"
velocidad = 0
encencido = False

def encender():
    global encencido
    encendido=True
    print("El Auto esta encencido")
    
def apagar():
    global encencido
    global velocidad
    if velocidad ==0:
        print("El Auto esta apagado")
    else:
        print("El Auto esta encendido")    
        
    
        