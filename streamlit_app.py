import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Arbitro bancario

Aplicación que permite comparar la información de las operaciones interbancarias. 

"""
def main():
    st.title('Menú de Operaciones')

    # Opciones del menú
    opciones_menu = ['Ingresar operaciones', 'Histórico de operaciones', 
                     'Operaciones en curso', 'Mismatch de operaciones', 
                     'Alertas']

    # Mostrar menú en la barra lateral
    seleccion = st.sidebar.selectbox('Menú', opciones_menu)

    # Dependiendo de la selección, mostrar el contenido correspondiente
    if seleccion == 'Ingresar operaciones':
        mostrar_ingresar_operaciones()
    elif seleccion == 'Histórico de operaciones':
        mostrar_historico_operaciones()
    elif seleccion == 'Operaciones en curso':
        mostrar_operaciones_en_curso()
    elif seleccion == 'Mismatch de operaciones':
        mostrar_mismatch_operaciones()
    elif seleccion == 'Alertas':
        mostrar_alertas()

def mostrar_ingresar_operaciones():
    st.write('Aquí puedes ingresar nuevas operaciones.')

def mostrar_historico_operaciones():
    st.write('Aquí puedes ver el histórico de operaciones.')

def mostrar_operaciones_en_curso():
    st.write('Aquí puedes ver las operaciones en curso.')

def mostrar_mismatch_operaciones():
    st.write('Aquí puedes ver los casos de mismatch de operaciones.')

def mostrar_alertas():
    st.write('Aquí puedes ver las alertas.')

if __name__ == "__main__":
    main()
def generar_tabla():
    # Definir los datos
    datos = {
        'Fecha de ingreso': ['2024-03-13', '2024-03-14', '2024-03-15'],
        'Operación': ['Compra', 'Venta', 'Compra'],
        'Contraparte': ['Cliente A', 'Cliente B', 'Cliente C'],
        'Tipo': ['Acciones', 'Futuros', 'Opciones'],
        'Paga o recibe': ['Paga', 'Recibe', 'Paga'],
        'Tiempo': ['Corto plazo', 'Largo plazo', 'Corto plazo'],
        'Monto': [1000, 2000, 1500],
        'Tasa': [0.05, 0.03, 0.04],
        'Rescatar': [True, False, True]
    }

    # Crear DataFrame
    df = pd.DataFrame(datos)

    # Mostrar tabla
    st.write(df)

def main():
    st.title('Tabla de operaciones')
    generar_tabla()

if __name__ == "__main__":
    main()
