"""
Un hospital registra pacientes conforme llegan a Emergencias.
El sistema debe seguir registrando pacientes hasta que el usuario escriba FIN.
Cada paciente tendrá:

- Nombre
- Edad
- Diagnóstico

Toda la información se almacenará en un diccionario.
"""

pacientes = {}
contador = 1

while True:
    nombre = input("Nombre del Paciente (FIN para terminar)")
    if nombre.upper() =="FIN":
        break
    edad = int(input("Edad:"))
    diagnostico = input("Diagnostico:")
    
    pacientes[contador] = {
        "nombre":nombre,
        "edad":edad,
        "diagnostico":diagnostico
    }
    contador += 1
print("Pacientes Registrados")    

for codigo,datos in pacientes.items():
     print("Código:", codigo)
     print("Nombre:", datos["nombre"])
     print("Edad:", datos["edad"])
     print("Diagnostico:", datos["diagnostico"])
     print("=============================")
     
    
    

