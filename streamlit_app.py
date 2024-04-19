import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from datetime import datetime

"""
# Arbitro bancario

Almacenamiento y comparación de operaciones de derivados interbancarios. 

"""
def main():
    st.title('Arbitro bacario')  # Nombre de la aplicación

    # Descripción del menú de la izquierda.
    
    st.sidebar.title('Menú')

    options = [':pencil: **Ingresar operaciones**', ':chart_with_upwards_trend: **Histórico de operaciones**', ':hourglass_flowing_sand: **Operaciones en curso**', ':exclamation: **Mismatch de operaciones**', ':warning: **Alertas**']
    choice = st.sidebar.radio('Seleccione una vista', options)

    if choice == ':pencil: **Ingresar operaciones**':
        st.header('Ingresar operaciones')
        ingresar_operaciones()

    elif choice == ':chart_with_upwards_trend: **Histórico de operaciones**':
        st.header('Histórico de operaciones')
        mostrar_operaciones_historicas()

    elif choice == ':hourglass_flowing_sand: **Operaciones en curso**':
        st.header('Operaciones en curso')
        mostrar_operaciones_en_curso()

    elif choice == ':exclamation: **Mismatch de operaciones**':
        st.write("Operaciones que no hicieron match")

    elif choice == ':warning: **Alertas**':
        st.write("Alertas")

def ingresar_operaciones():
    # Campos de entrada para ingresar la información
    operacion = st.text_input("Operación (máximo 10 caracteres)", max_chars=10)
    contraparte = st.selectbox("Contraparte", ['abc', 'eft', 'yuv', 'khi']) #Se seleccionan las contrapartes de la lista desplegada
    tipo = st.selectbox("Tipo", ['swap', 'fwd']) #Se seleccionan las contrapartes de la lista desplegada
    pata = st.selectbox("Pata", ['Paga', 'Recibe']) #Se seleccionan las contrapartes de la lista desplegada
    tiempo = st.text_input("Tiempo (formato dd/mm/yyyy)") #Se debe infresar una fecha, indico el formato, pero no tengo claro cómo hacer que aparezca la típica casilla con un calendario desde la que seleccionar
    monto = st.number_input("Monto", min_value=0.0) 
    tasa = st.number_input("Tasa")
    mach = st.radio("¿Mach?", ["Sí", "No"]) #Aún no creo la relación, esto lo dejé así por el momento para probar si funciona.
    
    if st.button("Enviar"):
        # Fecha de ingreso de la operación (cuando se presiona enviar)
        fecha_ingreso = datetime.now().strftime('%d/%m/%Y')

        # Diccionario con la información de la operación
        nueva_operacion = {
            "Fecha de ingreso": fecha_ingreso,
            "Operación": operacion,
            "Contraparte": contraparte,
            "Tipo": tipo,
            "Pata": pata,
            "Tiempo": tiempo,
            "Monto": monto,
            "Tasa": tasa,
            "Mach": mach
        }

        guardar_operacion(nueva_operacion)
        st.success("Operación ingresada correctamente")

def mostrar_operaciones_historicas():
    operaciones = obtener_operaciones()
    if operaciones:
        df = pd.DataFrame(operaciones)
        st.dataframe(df)
    else:
        st.write("No se encuentran operaciones.")

def mostrar_operaciones_en_curso():
    operaciones = obtener_operaciones()
    if operaciones:
        df = pd.DataFrame(operaciones)
        operaciones_en_curso = df[df['Mach'] == 'Sí']
        st.dataframe(operaciones_en_curso)
    else:
        st.write("No hay operaciones en curso")

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
