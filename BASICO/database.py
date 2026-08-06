import sqlite3

BD="agente.bd"

def crear_tabla():
    conexion= sqlite3.connect(BD)
    cursor = conexion.cursor()
    cursor.execute("""
    
    CREATE TABLE IF NOT EXISTS conversaciones(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        usuario TEXT,

        agente TEXT

    )

    """)

    conexion.commit()
    conexion.close()
    
def guardar_conversacion(usuario,agente):
    conexion= sqlite3.connect(BD)
    cursor= conexion.cursor()
    cursor.execute(
        """
        INSERT INTO conversaciones(usuario,agente)
        VALUES(?,?)
        """,
        (usuario,agente)
        
    )
    conexion.commit()
    conexion.close()

def mostrar_historial():
    conexion= sqlite3.connect(BD)
    cursor= conexion.cursor()
    cursor.execute(
        """
        SELECT * FROM conversaciones
        """)
    datos= cursor.fetchall()
    conexion.close()
    return datos
          