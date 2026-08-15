import psycopg2

try:
    conexion = psycopg2.connect(
        host="localhost",
        database="python_ia",
        user="postgres",
        password="Rioazulq12",
        port="5432"
    )
    print("Conexion exitosa a PostgresSQL")

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    registros = cursor.fetchall()

    for fila in registros:
        print(f"ID:{fila[0]}")
        print(f"Producto:{fila[1]}")
        print(f"Precio:{fila[2]}")
        print(f"Stock:{fila[3]}")
        print("==================")

    cursor.close()
    conexion.close()    
except Exception as error:
    print(error)    