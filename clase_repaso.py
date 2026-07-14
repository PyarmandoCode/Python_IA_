"""
¿Qué hace realmente ChatGPT cuando escribimos una pregunta?
-Buscar Informacion
-Piensa
-Responde
"""
nombre = "Armando" # str
edad = 30 # int
altura = 1.75 # float
activo = True # bool

#print(nombre)
#print(type(altura))

#Listas

preguntas = [
    "Hola",
    "Como estas?",
    "Explicame Python"
]
#print(preguntas)

#Diccionarios
persona = {
    "nombre":"Carlos",
    "edad":22,
    "pais":"Perú"
}

#print(persona["nombre"])
#print(persona["edad"])
#print(persona["pais"])

#funciones

def responder(pregunta):
    if pregunta =="1":
        respuesta ="Me Llamo PythonBot?"
    elif pregunta =="2":    
        respuesta ="Avanzado"
    elif pregunta =="3":    
        respuesta="De Nada"
    else:
        respuesta="No entendi tu pregunta recien estoy entrenando"    
    return respuesta
    
print(responder("4"))