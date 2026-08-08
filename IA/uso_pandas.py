"""
Pandas es una de las bibliotecas más populares de Python para 
manipular, analizar y procesar datos. Se utiliza especialmente 
en ciencia de datos, análisis de datos, inteligencia artificial y 
finanzas

DataFrame: una tabla bidimensional con filas y columnas 
(similar a una hoja de Excel o una tabla de una base de datos).

Que se puede Hacer?
-Leer datos desde diferentes origenes de datos:
 -CSV
 -EXCEL
 -JSON
 -SQL
-Filtrar y seleccionar datos.
-Limpiar datos (eliminar valores nulos, duplicados, etc.).
-Ordenar y agrupar información.
-Realizar cálculos y estadísticas.
-Combinar tablas.
-Preparar datos para modelos de aprendizaje automático.
"""


import pandas as pd
df = pd.read_csv("ventas_tienda.csv")
#print(df.head()) #Muestra las primeras 5 filas
filtro = df[df["vendedor"]=="Ana"]
filtro2 = df[df["metodo_pago"]=="Tarjeta"]
filtro3 = df[(df["vendedor"]=="Ana") & 
             (df["metodo_pago"]=="Yape")
             ]
filtro4 = df[(df["vendedor"]=="Ana") |
             (df["vendedor"]=="Carlos")]

filtro5= df[df["ciudad"].isin(["Lima","Trujillo","Cusco"])]

filtro6= df[df["estado"]=="Pendiente"].sort_values(
    by="precio_unitario",
    ascending=False
)
          
             

print(filtro6)



