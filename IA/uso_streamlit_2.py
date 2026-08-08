import streamlit as st

#nombre = input("Ingrese el nombre de la persona:")
#edad= input("Ingrese la edad de la persona:")
#print(f"Bienvenido {nombre} tu edad es {edad}")

st.title("Sistema de Bienvenida")
st.write("Ingrese sus datos")
nombre = st.text_input("Ingrese su nombre")

edad = st.number_input(
        "Ingrese la edad",
        min_value=0,
        max_value=120,
        step=1
        )

if st.button("Mostrar Informacion"):
    st.success("Datos Registrados")
    st.write(f"Nombre {nombre}")
    st.write(f"Edad {edad}")
