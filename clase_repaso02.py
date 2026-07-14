"""
ANALIZADOR DE SENTIMIENTOS
-PROCESAMIENTO DE LENGUAJE NATURAL (NLP)
"""

texto = input("Escriba una Frase:").lower()
posivas = [
    "feliz",
    "genial",
    "excelente",
    "amor",
    "gracias"
] 
negativos = [
    "adios",
    "mal",
    "terrible",
    "feo",
    "triste"
]

if any(p in texto for p in posivas):
    print("Sentimiento Positivo")
elif any(n in texto for n in negativos):
    print("Sentimiento Negativo")
else:
    print("Sentimiento Neutral")    
        
    