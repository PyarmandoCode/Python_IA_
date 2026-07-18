"""
Reporte de Ventas
- Total de ventas
- Venta más alta
- Venta más baja
- Promedio de ventas
"""
def Leer_ventas():
    archivo = open("ventas.txt","r")
    
    #ventas = [250,180,320,150,400,210,350]
    ventas=[]
    for linea in archivo:
        ventas.append(float(linea.strip()))
    archivo.close()
    return ventas  

def mostrar_reporte(ventas):
    total = sum(ventas)
    promedio = total / len(ventas)
    mayor = max(ventas)
    menor = min (ventas)
    print("=" * 35)
    print("   REPORTE DE VENTAS")
    print("=" * 35)
    print("Cantidad de ventas :", len(ventas))
    print("Total vendido      :", total)
    print("Venta mayor        :", mayor)
    print("Venta menor        :", menor)
    print("Promedio       :", round(promedio,2))
    print("=" * 35)
    
      
mostrar_reporte(Leer_ventas())    