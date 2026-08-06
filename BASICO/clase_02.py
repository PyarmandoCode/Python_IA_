"""
✅ Listas
✅ Bucles for y while
✅ Condicionales if/elif/else
✅ Funciones
✅ Entrada de datos por teclado
"""
#nombre = input("Ingrese el nombre de una persona:")
#print(f"Hola {nombre} Nos encontramos en la segunda clase de PYTHON CON IA")

#Lista donde se almacenaran los estudiantes
estudiantes = []
#Funcion para agregar estudiantes a la lista
def registrar_estudiantes():
    nombre=input("Ingrese el nombre del estudiante:")
    #Creando una lista para anadir notas
    notas =[]
    for i in range(3):
        nota = float(input(f"ingrese la nota {i+1}:"))
        notas.append(nota)
    #creando una lista para añadir el estudiante y sus tres notas    
    estudiante= [nombre,notas]   
    #Anadir dicho estudiante en la lista estudiantes
    estudiantes.append(estudiante) 
    print("Estudiante registrado correctamente")
    
def mostrar_estudiantes():
    if len(estudiantes)==0:
        print("No Existen estudiantes registrados")
    else:
        for estudiante in estudiantes:
            nombre=estudiante[0] #nombre
            notas=estudiante[1]  #notas
            promedio=calcular_promedio(notas)  
            print("************************")
            print(f"nombre {nombre}")
            print(f"notas {notas}")
            print(f"promedio {round(promedio,2)}")
            if promedio>=11:
                print("Estado APROBADO")
            else:
                print("Estado DESAPROBADO")    
            
def calcular_promedio(notas):
    suma=0
    for nota in notas:
        suma += nota
    promedio = suma / len(notas)    
    return promedio
                

#Programa Principal
while True:
    print("==========Menu===========")
    print("1-Registrar Estudiante")     
    print("2-Mostrar Estudiantes")
    print("3-Salir")             
    opcion= input("Seleccione una Opcion")
    if opcion =="1":
        registrar_estudiantes()
    elif opcion=="2":
        mostrar_estudiantes()
    else:
        break           

"""
estudiantes.append("Jorge")     
estudiantes.append("Manuel") 
estudiantes.append("Pedro")    
for i in estudiantes:
    print(i)
"""    

"""
CHALLERNGER HALLAR EL MEJOR ESTUDIANTE
- CREAR UNA FUNCION
- RECORRECOR LA LISTA DE ESTUDIANTES (F0R)
- COMPARAR LAS NOTAS (IF)
- CREAR UA VARIABLE DENTRO DEL FOR PARA TOMAR LA NOTA MAS ALTA
- IMPRIRLO
"""
