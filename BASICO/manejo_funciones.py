"""
Funciones Definidas por el Usuario(DUF)
Funciones Integradas 
- Matematicas , Cadena Texto , Fechas , Aleatorios

"""
def total_ventas(venta1,venta2):
    total = float(venta1)+ float(venta2)
    return total

#print(total_ventas(1600,1700))


import math #importar todo el modulo
from datetime import datetime #importar una funcion en especifica
import random
import string

"""
numero=25
print(math.sqrt(numero)) #Raiz Cuadrada
print(math.pow(2,5)) #Potencia
print(math.factorial(numero))
print(math.ceil(4.2))
print(math.floor(4.9))
print(math.pi)
print(math.e)

lista = [8,4,9,2,15]
print(max(lista))
print(min(lista))
print(sum(lista))
print(len(lista))
print(sorted(lista))

hoy = datetime.now()
print(hoy)
print(hoy.day)
print(hoy.year)
print(hoy.hour)
print(hoy.minute)
"""

fecha = datetime.now()
#print(fecha.strftime("%d/%m/%Y"))
#print(fecha.strftime("%H:%M:%S"))
inicio = datetime(2026,7,1)
fin = datetime.now()
dias = fin - inicio
#print(dias.days)

#print(random.randint(1,1000))
#print(random.random())
colores = ["Rojo","Azul","Verde","Negro"]
#print(random.choice(colores))
#print(random.shuffle(colores))

"""
Contraseña Aleatoria
"""
caracteres = string.ascii_letters + string.digits
#print(caracteres)
#password = ""
#for i in range(10):
#    password += random.choice(caracteres)
#print(password)    


numeros = [1,2,3,4,5]
random.shuffle(numeros)
print(numeros)