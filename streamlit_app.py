import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from datetime import datetime

"""
# Arbitro bancario

Aplicación que permite comparar la información de las operaciones interbancarias. 

"""
def main():
    st.title('ABCD')  # Nombre de la aplicación

    st.sidebar.title('Menú')

    options = [':pencil: **Ingresar operaciones**', ':chart_with_upwards_trend: **Histórico de operaciones**', ':hourglass_flowing_sand: **Operaciones en curso**', ':exclamation: **Mismatch de operaciones**', ':warning: **Alertas**']
    choice = st.sidebar.radio('Selecciona una opción', options)

    if choice == ':pencil: **Ingresar operaciones**':
        st.header('Ingresar operaciones')

        # Campos de entrada para ingresar la información
        operacion = st.text_input("Operación (máximo 10 caracteres)", max_chars=10)
        contraparte = st.selectbox("Contraparte", ['abc', 'eft', 'yuv', 'khi'])
        tipo = st.selectbox("Tipo", ['swap', 'fwd'])
        pata = st.selectbox("Pata", ['Paga', 'Recibe'])
        tiempo = st.text_input("Tiempo (formato dd/mm/yyyy)")
        monto = st.number_input("Monto", min_value=0.0)
        tasa = st.number_input("Tasa", min_value=0.0)
        
        # Nuevo campo para seleccionar "Sí" o "No" (o "Mach" y "No Mach")
        mach = st.radio("¿Mach?", ["Sí", "No"])

        # Botón para enviar los datos ingresados
        if st.button("Enviar"):
            # Obtiene la fecha de ingreso actual
            fecha_ingreso = datetime.now().strftime('%d/%m/%Y')

            # Crea un diccionario con la información de la operación
            nueva_operacion = {
                "Fecha de ingreso": fecha_ingreso,
                "Operación": operacion,
                "Contraparte": contraparte,
                "Tipo": tipo,
                "Pata": pata,
                "Tiempo": tiempo,
                "Monto": monto,
                "Tasa": tasa,
                "Mach": mach  # Agregar la variable Mach a la operación
            }

            # Guarda la operación en una lista o base de datos
            guardar_operacion(nueva_operacion)
            st.success("Operación ingresada correctamente")

    elif choice == ':chart_with_upwards_trend: **Histórico de operaciones**':
        st.header('Histórico de operaciones')
        # Obtiene todas las operaciones ingresadas
        operaciones = obtener_operaciones()

        # Muestra las operaciones en una tabla
        if operaciones:
            df = pd.DataFrame(operaciones)
            st.dataframe(df)
        else:
            st.write("No hay operaciones ingresadas")

    elif choice == 'Operaciones en curso':
        st.write("Aquí puedes ver las operaciones en curso")
    elif choice == 'Mismatch de operaciones':
        st.write("Aquí puedes ver los mismatches de operaciones")
    elif choice == 'Alertas':
        st.write("Aquí puedes ver las alertas")

# Función para guardar la operación en una lista (simulación de base de datos)
def guardar_operacion(operacion):
    # Puedes guardar la operación en una base de datos o en una lista
    # Aquí lo guardamos en una lista simulada
    if 'operaciones' not in st.session_state:
        st.session_state.operaciones = []

    st.session_state.operaciones.append(operacion)

# Función para obtener todas las operaciones guardadas
def obtener_operaciones():
    if 'operaciones' in st.session_state:
        return st.session_state.operaciones
    else:
        return []

if __name__ == "__main__":
    main()
