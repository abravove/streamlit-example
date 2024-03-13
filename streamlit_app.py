import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Arbitro bancario

Aplicación que permite comparar la información de las operaciones interbancarias. 

"""
def main():
    st.title('Árbitro bancario')  # Nombre de la aplicación

def main():
    st.sidebar.title('Menú')
    options = ['Ingresar operaciones', 'Histórico de operaciones', 'Operaciones en curso', 'Mismatch de operaciones', 'Alertas']
    choice = st.sidebar.radio('Selecciona una opción', options)

    if choice == 'Ingresar operaciones':
        st.write("Aquí puedes ingresar nuevas operaciones")
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
