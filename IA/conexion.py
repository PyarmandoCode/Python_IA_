import psycopg2

try:
    conexion = psycopg2.connect(
        host="localhost",
        database="python_ia",
        user="postgres",
        password="",
        port="5432"
    )
    print("Conexion exitosa a PostgresSQL")

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    registros = cursor.fetchall()

    for fila in registros:
        print(fila)

    cursor.close()
    conexion.close()    
except Exception as error:
    print(error)    