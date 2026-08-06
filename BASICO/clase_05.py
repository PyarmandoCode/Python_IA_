"""
Una tienda de computadoras desea conocer cuánto dinero recaudó durante el día.
Cada producto tiene:
    Nombre
    Cantidad vendida
    Precio
Toda la información está almacenada en un diccionario.

ventas
│
├── Laptop
│      ├── cantidad = 3
│      └── precio = 3200
│
├── Mouse
│      ├── cantidad = 15
│      └── precio = 50
│
├── Teclado
│      ├── cantidad = 8
│      └── precio = 120
│
└── Monitor
       ├── cantidad = 5
       └── precio = 850
"""
ventas = {
     "Laptop": {"cantidad" : 3, "precio" : 3200}, #9600
     "Mouse": {"cantidad" : 15, "precio" : 50}, #750
     "Teclado": {"cantidad" : 8, "precio" : 120},#960
     "Monitor": {"cantidad" : 4, "precio" : 850} #3400
}
    
total = 0

for producto,datos in ventas.items():
    subtotal = datos["cantidad"] * datos["precio"]
    print(producto)
    print(f"Cantidad: {datos["cantidad"]}")
    print(f"Precio: {datos["precio"]}")
    print(f"Subtotal: {subtotal}")
    print("=============================")
    total += subtotal #9600+750+960+3400
    
print(f"TOTAL DEL DIA {round(total,2)}")