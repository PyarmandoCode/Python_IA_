"""
Conjunto (SET)
- No Permite elementos repetidos
- No Mantiene un orden especifico
- Se Puede agregar y eliminar elementos
- Es muy rapido para buscar Informacion
- Se define con llaves {}
"""

frutas = {"Manzana","Pera","Uva"}
#print(type(frutas))
#print(frutas)

#Lista
ventas = {
    "Laptop",
    "Mouse",
    "Laptop",
    "Teclado",
    "Mouse",
    "Monitor"
}

#print(ventas)
#Operaciones entre conjuntos
"""
Unir
"""
python = {
    "Juan",
    "Ana",
    "Pedro"
}

java = {
    "Pedro",
    "Luis",
    "Carlos"
}

java.clear()
java.add("Martin")
java.remove("Luis")

#todos = python.union(java)
#print(todos)
print(f"esto es ejemplo de union {python.intersection(java)}")
print(f"esto es un ejemplo de diferencia {python.difference(java)}")



