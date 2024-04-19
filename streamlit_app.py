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
        st.header('Mismatch de operaciones')
        mostrar_mismatch_de_operaciones()

    elif choice == ':warning: **Alertas**':
        st.header('Alertas')

def ingresar_operaciones():
    # Campos de entrada para ingresar la información
    operacion = st.text_input("Operación (máximo 10 caracteres)", max_chars=10)
    contraparte = st.selectbox("Contraparte", ['Banco de Chile', 'Internacional', 'Scotiabank', 'BCI']) #Se seleccionan las contrapartes de la lista desplegada
    tipo = st.selectbox("Tipo", ['swap', 'fwd']) #Se seleccionan las contrapartes de la lista desplegada
    tiempo = st.text_input("Tiempo (formato dd/mm/yyyy)") #Se debe infresar una fecha, indico el formato, pero no tengo claro cómo hacer que aparezca la típica casilla con un calendario desde la que seleccionar
    st.text("Para pata Activa:")
    divisa_a = st.selectbox("Moneda de pata activa", ['CLP', 'USD', 'EUR', 'JPY'])
    monto_a = st.number_input("Monto de pata activa", min_value=0.0) 
    tasa_a = st.number_input("Tasa de pata activa")
    st.text("Para pata Pasiva:")
    divisa_p = st.selectbox("Moneda de pata pasiva", ['CLP', 'USD', 'EUR', 'JPY'])
    monto_p = st.number_input("Monto de pata pasiva", min_value=0.0) 
    tasa_p = st.number_input("Tasa de pata pasiva")

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
            "Tiempo": tiempo,
            "Divisa A": divisa_a,
            "Monto A": monto_a,
            "Tasa A": tasa_a,
            "Divisa P": divisa_p,
            "Monto P": monto_p,
            "Tasa P": tasa_p,            
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

def mostrar_mismatch_de_operaciones():
    operaciones = obtener_operaciones()
    if operaciones:
        df = pd.DataFrame(operaciones)
        operaciones_en_curso = df[df['Mach'] == 'No']
        st.dataframe(operaciones_mismatch)
    else:
        st.write("No hay operaciones sin matchear.")

# Funciones citadas:
    # session_state -> Espacio de almacenamiento de streamlit
def guardar_operacion(operacion):
    if 'operaciones' not in st.session_state:
        st.session_state.operaciones = []
        
    st.session_state.operaciones.append(operacion)

def obtener_operaciones():
    if 'operaciones' in st.session_state:
        return st.session_state.operaciones
    else:
        return []

if __name__ == "__main__":
    main()
