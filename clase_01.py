#QUE SON VARIABLES primitivas
nombre = "Armando" #cadena(str)
edad = 25 #entero(int)
precio = 15.50 #decimal(float)
activo = True #logica(bool)
casado = False
#print("Hola Mundo desde Bienvenido")
#print(type(precio)) #tipo de datos

#OPERADORES ARITMETICOS docstring
"""
| Operador | Nombre          | Ejemplo | Resultado |
| -------- | --------------- | ------- | --------- |
| +        | Suma            | 5 + 3   | 8         |
| -        | Resta           | 5 - 3   | 2         |
| *        | Multiplicación  | 5 * 3   | 15        |
| /        | División        | 5 / 2   | 2.5       |
| //       | División entera | 5 // 2  | 2         |
| %        | Módulo          | 5 % 2   | 1         |
| **       | Potencia        | 2 ** 3  | 8         |
"""
valor1 = 24
valor2 = 25.7
res = valor1 + valor2
res2 = valor1 - valor2
resm = valor1 * valor2
resd = valor1 / valor2
resr = valor1 % valor2
resp = valor1 ** valor2
#print(f"El resultado de la suma es {res} y el residuo:{resr}")
#Condicionales Operadore ternario
#Indentacion
edad = 16
#if edad>18:
#    print("Es mayor de edad")
#else:
#    print("Es menor de edad") 

#Condicionales Ternariales
#print("Es mayor de edad" if edad>=11 else "Es menor de edad") 

#Ciclos (Bucles) #Automatizar repeticiones
#For - Usar cuando sabes cuantas veces quieres repetir?
#While - Usar cuando quieres repetir mientras una condicion 
#sea Verdad
#for _ in range(15):
#    print("Hola Mundo")   
#print("fin del for")    

#i = 1
#while i <=5:
#    print(f"Numero {i}")
#    i +=1

#Funciones

def saludar(nombre):
    rpta=f"Hola {nombre} desde una funcion "
    return rpta


print(saludar("Jose"))