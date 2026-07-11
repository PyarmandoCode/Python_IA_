import datetime
import random
#Memoria Temporal
historial = []
#Funcion que analiza el mensaje
def analizar_mensaje(mensaje):
    mensaje=mensaje.lower()
    historial.append(
        {
            "usuario":mensaje
        
         }
        )
    #Inteligencia del Agente
    if "hola" in mensaje:
        respuesta="Hola Soy tu Agente de IA"
    elif "nombre" in mensaje:
        respuesta="Mi Nombre es PythonBot"    
    elif "hora" in mensaje:
        hora = datetime.datetime.now()  
        respuesta = (
            f"La Hora actual es "
            f"{hora.hour}:{hora.minute}"
        )  
    elif "ayuda" in mensaje:
        respuesta = """
        #Puedo Ayudarte con:
        #-Saludos
        #-Hora Actual
        #-Mi Nombre
        """
    else:
        respuestas =[
            "No Entiendo todavia",
            "Estoy Aprendiendo esa respuesta",
            "Puedes Preguntarme algo diferente"
        ]    
        respuesta= random.choice(respuestas)
    historial.append(
        {
            "agente":respuesta
        }
    )    
    return respuesta

def usar_agente():
    print("*********Memoria del Agente***********")
    for dato in historial:
        print(dato)
    print("********************************")
    print("Mi Primer Agente IA")
    print("********************************")
    print("Escribe 'salir' para terminar ")
    while True:
        pregunta=input("Usuario==>")
        if pregunta.lower()=="salir":
            print("Agente Finalizado")
            break
        respuesta=analizar_mensaje(pregunta)
        print("\nIA:",
              respuesta
              )
        
usar_agente()        
            
        



