"""
-Entrenar un modelo de IA para predecir si un estudiante aprobara
o no segu sus horas de estudio
-Que es un Modelo ? es un sistema matematico que aprende patrones
de datos y utiliza lo aprendido para predecir resultados sobre
informacion nueva
-Scikit-learn(sklearn) es una libreria mas utilizada de pytho para crear
y entrenar modelos de machine learning
 - LogisticRegression().-Crear el Modelo
 - modelo.fit(x,y).-entrena el modelo utilizando nuestros datos
 - modelo.predict().-utiliza lo aprendido para predecir un resultado nuevo

DATOS DE ENTRENAMIENTO

Horas estudiadas     Resultado
1 hora               No aprueba
2 horas              No aprueba
3 horas              No aprueba
5 horas              Aprueba
6 horas              Aprueba
8 horas              Aprueba
        ↓
        ↓
   ENTRENAMIENTO
   modelo.fit(x,y)
        ↓
        ↓
  MODELO DE IA
        ↓
        ↓
Nuevo estudiante: 7 horas
modelo.predict([[7]])
        ↓
   PREDICCIÓN
        ↓
     APRUEBA
"""
#Programacion tradicional
horas = 7
if horas >=5:
    print("Aprueba")
else:
    print("No Aprueba")    
