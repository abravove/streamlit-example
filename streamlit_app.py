import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Arbitro bancario

Aplicación que permite comparar la información de las operaciones interbancarias. 

"""
def main():
    st.title('ABCD')  # Nombre de la aplicación

    st.write("[Iniciar sesión](#)")  # Enlace de inicio de sesión en la esquina superior derecha

    st.sidebar.title('Menú')
    options = ['Ingresar operaciones', 'Histórico de operaciones', 'Operaciones en curso', 'Mismatch de operaciones', 'Alertas']
    choice = st.sidebar.radio('Selecciona una opción', options)

    if choice == 'Ingresar operaciones':
        st.header('Ingresar operaciones')

        # Campos de entrada para ingresar la información
        operacion = st.text_input("Operación (máximo 10 caracteres)", max_chars=10)
        contraparte = st.selectbox("Contraparte", ['abc', 'eft', 'yuv', 'khi'])
        tipo = st.selectbox("Tipo", ['swap', 'fwd'])
        pata = st.selectbox("Pata", ['Paga', 'Recibe'])
        tiempo = st.text_input("Tiempo (formato dd/mm/yyyy)")
        monto = st.number_input("Monto", min_value=0.0)
        tasa = st.number_input("Tasa", min_value=0.0)

        # Botón para enviar los datos ingresados
        if st.button("Enviar"):
            # Aquí puedes procesar los datos ingresados, por ejemplo, guardarlos en una base de datos
            st.success("Datos enviados correctamente")

    elif choice == 'Histórico de operaciones':
        st.write("Aquí puedes ver el histórico de operaciones")
    elif choice == 'Operaciones en curso':
        st.write("Aquí puedes ver las operaciones en curso")
    elif choice == 'Mismatch de operaciones':
        st.write("Aquí puedes ver los mismatches de operaciones")
    elif choice == 'Alertas':
        st.write("Aquí puedes ver las alertas")

if __name__ == "__main__":
    main()
