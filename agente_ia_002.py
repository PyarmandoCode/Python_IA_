# =====================================
# AGENTE IA CON SQLITE
# =====================================

import datetime
import random
import database

# Crear tabla al iniciar

database.crear_tabla()

# -------------------------------------
# Cerebro del agente
# -------------------------------------

def pensar(mensaje):

    mensaje = mensaje.lower()

    if "hola" in mensaje:

        respuesta="Hola  soy PythonBot"


    elif "nombre" in mensaje:

        respuesta="Mi nombre es PythonBot"


    elif "hora" in mensaje:

        ahora=datetime.datetime.now()

        respuesta=f"La hora es {ahora.hour}:{ahora.minute}"

    elif "ayuda" in mensaje:

        respuesta="""

        Puedo ayudarte con:

        - Saludos
        - Hora
        - Mi nombre

        """

    else:

        respuesta=random.choice(

            [

            "Todavía estoy aprendiendo",

            "No tengo esa respuesta",

            "Puedes preguntarme otra cosa"

            ]

        )


    # Guardar en SQLite

    database.guardar_conversacion(

        mensaje,

        respuesta

    )

    return respuesta

# -------------------------------------
# Programa principal
# -------------------------------------

print("============================")

print("AGENTE IA SQLITE")

print("============================")

print("Escribe salir para terminar")


while True:


    pregunta=input("\nUsuario: ")

    if pregunta.lower()=="salir":

        break

    respuesta=pensar(pregunta)

    print("\nIA:",respuesta)


print("\n===== HISTORIAL GUARDADO =====")


datos=database.mostrar_historial()

for fila in datos:

    print(fila)