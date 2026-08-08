"""
Streamlit es una librería de Python que permite convertir 
programas de Python en aplicaciones web interactivas sin necesidad 
de saber HTML, CSS o JavaScript.
-Entorno virtual .-(venv) es un espacio aislado donde instalas las 
librerías que necesita un proyecto específico, sin afectar a otros proyectos ni a la instalación general de Python.
-pip.- pip es el administrador de paquetes de Python. 
Sirve principalmente para instalar librerías externas.
-Libreria.-es un conjunto de código ya creado por otros programadores 
que podemos reutilizar para no tener que programar todo desde cero.
"""
import streamlit as st

st.title("Mi primer sitio web en python")
st.header("Registro de Cliente")
st.write("Hola Mundo") #Mostrar Texto
st.success("Operacion realizada correctamente")
st.info("Informacion")
st.warning("Advertencia")
st.error("Ocurrio un error")

