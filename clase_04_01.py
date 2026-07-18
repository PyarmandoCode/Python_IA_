"""
Leer un archivo CSV y mostrar:
-Total de estudiantes
-Promedio general
-Alumno con mayor nota
-Alumnos aprobados
-Alumnos desaprobados
"""
def leer_estudiantes():
    archivo= open("estudiantes.csv","r",encoding="utf-8")
    estudiantes = []
    next(archivo) # Saltar el encabezado
    
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre = datos[0]
        nota = float(datos[1])
        estudiantes.append([nombre,nota])
    
    archivo.close()
    return estudiantes

def mostrar_reporte(lista):
    total = len(lista)   
    suma = 0
    mayor_nota = 0
    menor_nota = 0 
    aprobados = 0
    desaprobados=0
    
    for alumno in lista:
        nombre = alumno[0]
        nota = alumno[1]
        
        suma += nota
        if nota > mayor_nota:
            mayor_nota = nota
            mejor_alumno = nombre
        
        if nota >= 11:
            aprobados +=1
        else:
            desaprobados +=1  
    
    promedio = suma / total    
    
    print("=" * 40)
    print("     REPORTE DE ESTUDIANTES")
    print("=" * 40)  
    print("Total estudiantes :", total)
    print("Promedio general  :", round(promedio,2))
    print("Mejor alumno      :", mejor_alumno)
    print("Mayor nota        :", mayor_nota)
    print("Aprobados         :", aprobados)
    print("Desaprobados      :", desaprobados)
    print("=" * 40)         

estudiantes = leer_estudiantes()

mostrar_reporte(estudiantes)            
        
    