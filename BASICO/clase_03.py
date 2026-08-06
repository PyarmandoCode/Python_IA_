"""
¿Qué son las colecciones?
Son estructuras que permiten almacenar múltiples datos.
Lista → Lista de estudiantes
Tupla → Coordenadas GPS del edificio
Set → Cursos únicos disponibles
Diccionario → Datos de cada estudiante
"""
#Listas Son ordenadas.Permiten repetidos.Se pueden modificar.
#estudiantes = ["Juan","Pedro","Maria"]
#estudiantes.append("Carlos")
#estudiantes.insert(1,"Percy")
#estudiantes.pop(2)
#print(estudiantes)

"""
peliculas = [
    "Avatar",
    "Titanic",
    "Batman",
    "Joker"
]
peliculas.append("Mario Bros")
peliculas.remove("Batman")
peliculas.sort()
for pelicula in peliculas:
    print(f"La pelicula siguiente es {pelicula}")
    
#print(peliculas)

"""
"""
CARRITO DE COMPRA INNOVADOR
"""


carrito = []

def mostrar_carrito():
    for producto in carrito:
        print(producto)
        
while True:
    print("1 - Agregar")
    print("2 - Eliminar")
    print("3 - Mostrar")
    print("4 - Salir")
    op= input()
    if op =="1":
        carrito.append(input("producto:"))
    elif op=="2":
        carrito.remove(input("Eliminar:"))
    elif op=="3":
        mostrar_carrito()
        #print(sorted(carrito))    
    else:
        break        
