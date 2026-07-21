"""
clave:valor
#dict
"""
import datetime #Libreria
import csv
import math
import random

hoy = datetime.datetime.now() #Fecha del sistema

persona = {
    "nombre":"Carlos", #str
    "edad":17, #int
    "ciudad":'Lima', #str
    "activo":True, #bool
    "talla":1.90 #float
}

"""
print(type(persona))
print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])
"""

#diccionarios con condicionaes
"""
if persona["edad"]>=18:
    print("La Persona es Mayor de edad")
else:
    print("La Persona es Menor de edad")    
"""    
    
"""    
notas = {
    "Juan":18,
    "Ana":15,
    "Pedro":10,
    "Luis":20
}

for alumno,nota in notas.items():
    if nota>=13:
        print(alumno,"aprobo")
    else:
        print(alumno,"desaprobo")    
    

#for _ in range(3):

"""
#Diccionario Anidado
empleados  = {
    1:{
        "nombre":"Carlos",
        "edad":50,
        "sueldo":2500
    },
    2:{
        "nombre":"Ana",
        "edad":28,
        "sueldo":3500
    },
    3:{
        "nombre":"Jorge",
        "edad":60,
        "sueldo":7500
    }
}

#print(empleados[1]["nombre"])
#Recorrer diccionarios anidadados

for codigo,datos in empleados.items():
    print(f"Codigo {codigo}")
    for clave , valor in datos.items():
        print(clave,":",valor)
    print("=======================")    
        