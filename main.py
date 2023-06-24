#Clase 11 Machine Learning
#Jeyfrey Calero
#20/06/2023
# pagina para descargar iconos => https://www.webfx.com/tools/emoji-cheat-sheet/


import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Ventas", page_icon="🛒", layout="wide")

st.header("ApiAnalisisDatosVentas")
st.markdown("##")
with open("Style.css") as file:
    st.markdown(f'<style> {file.read()}</style>', unsafe_allow_html=True)
theme_plotly = None

df=pd.read_excel("datos.xlsx", sheet_name="datos")
table1, table2=st.tabs(["Bases datos excel", "Porcentaje ventas"])

with table1:
    with st.expander("Mostrar datos"):
        mostrar_datos = st.multiselect("filtrar", df.columns, default=["VENTAS", "FECHA", "ESTADO",	"ID_YEAR", "LINEA_PRODUCTO", "NOMBRE_CLIENTE",	"CIUDAD", "PAIS"])
        st.dataframe(df[mostrar_datos], use_container_width=True)

with table2.caption("Mis porcentajes"):
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.info("25%",icon="💰")
        st.metric(label="U$D", value=f'{np.percentile(df["VENTAS"],25):,.2f}')
    
    with col2:
        st.info("50%",icon="💰")
        st.metric(label="U$D", value=f'{np.percentile(df["VENTAS"],50):,.2f}')

    with col3:
        st.info("75%",icon="💰")
        st.metric(label="U$D", value=f'{np.percentile(df["VENTAS"],75):,.2f}')
        
    with col4:
        st.info("100%",icon="💰")
        st.metric(label="U$D", value=f'{np.percentile(df["VENTAS"],100):,.2f}')

    with col5:
        st.info("0%",icon="💰")
        st.metric(label="U$D", value=f'{np.percentile(df["VENTAS"],0):,.2f}')
    
def filtrar_datos():
    columna =  st.sidebar.selectbox("Selecciona una columna", ["PAIS", "LINEA_PRODUCTO", "CIUDAD"])
    tipo_columna = st.sidebar.radio("Elige una categoría", ["Categoría", "Numérica"])
    col1, col2 = st.columns([2,1])

    with col1:
        if tipo_columna == "Categoría":
             mydf = pd.DataFrame(df[columna].value_counts())
             fig = px.bar(mydf, title="Valor Categoría", orientation="v") # La orientación no acepta STR por eso VERTICAL = "v" HORIZONTAL ="h" 
             fig.update_layout(legend_title=None, xaxis_title="Observaciones", yaxis_title="Conteo")
             st.write(fig, theme=theme_plotly)
        else:
            st.subheader("Total porcentaje")
            st.dataframe(df["VENTAS"].describe(), use_container_width=True)
    with col2:
        st.subheader("Total ventas") 
        st.metric(label="U$D", value=f'{np.sum(df["VENTAS"],0):,.2f}',help="sum", delta=np.average(df["VENTAS"]), delta_color="inverse")

filtrar_datos()

    

