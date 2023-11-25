import datetime 
import time
import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np

@st.cache
def run_fxn(n: int) -> list:
    return range(n)

"""Generación de la webapp con streamlit"""
# Definir titulo
st.title("Titulo: Analitica de Datos")
#Definir Header/SubHeader
st.header('Este es un header')
st.subheader("Este es un subheader")
#Definir en texto
st.text("Texto: Hola Streamlit")
#Definición de MarkDown
st.markdown("Este es un markdown h1 \n ## Este es un h2 \n ### Este es un h3")
st.header("Colores de texto y mensajes de error")
st.success("Successful")
st.info("Información!")
st.warning("warning")
st.error("Error")
st.exception("NameError(no está definido)")
st.header("Obtener información de ayuda de Python")
st.help(range)
st.header("Widgets:")
st.subheader("Checkbox")

if st.checkbox("Show/Hide"):
    st.text("Mostrar u ocultar Widget")
    st.subheader("Radio buttons")

status = st.radio("Cual es su estatus", ("Activo", "Inactivo"))

if status == "Activo":
    st.success("Estás activo")
else: 
    st.warning("Inactivo")
    st.subheader("SelectBox")

occupation = st.selectbox(
    "Tu ocupación", ["Programador", "Científico de datos", "BI", "Ingeniero de Datos"]
)

st.write("Opción seleccionada:", occupation)
st.subheader("MultiSelect")

location = st.multiselect(
    "Donde trabajas?",
    ("México", "New York", "Guadalajara", "Monterrey", "Nepal", "Buenos Aires", "Caracas"),
)

st.write("Seleccionó:", len(location), "locaciones")
st.subheader("Slider")

level = st.slider("Cual es tu nivel?", 1, 5)
st.write("Nivel:", level)
st.subheader("Buttons")
#Buttons

if st.button("Acerca"):
    st.text("Streamlit es cool")
else:
    st.text("")

st.header("Como recibir un ena entrada y procesarla con streamlit?")
st.subheader("Recibiendo texto")
 
firstname = st.text_input("Escriba su nombre: ")
if st.button("Aceptar"):
    result = firstname.title()
    st.success(result)
st.subheader("Área de texto")

message = st.text_area("Escriba un mensaje")
if st.button("Aceptar1"):
    result = message.title()
    st.success(result)
st.subheader("Entrada de fecha")

today = st.date_input("Hoy es", datetime.datetime.now())
st.text(f"{today}")
st.subheader("Entrada de tiempo")
#Time
the_time = st.time_input("La hora es:", datetime.time())
st.text(f"{the_time}")
st.header("Trabajar con archivos de imagenes, audio o videos")
#Images
st.subheader("Archivo de imagen")
img = Image.open(""C:\Users\jum73\Pictures\f30e21da146bd3501555eec943a8898e.gif"")
st.image(img, width=300, caption="Simple Imagen")

st.header("Otras opciones que permite la función write")

st.subheader("Texto con write")
st.write("Texto con write")
st.write(range(10))
st.header("Desplegando código puro y json")
st.subheader("Código puro")
st.code("import numpy as pd")
with st.echo():
    df = pd.DataFrame()
st.subheader("Desplegado json")
st.text("Mostran json")
st.json({"Nombre":"John", "Apellido":"Doe", "Género":"Masculino"})
st.header("Mostrar una barra de progreso, spinner y balloons")
st.subheader("Barra de progreso")
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p+1)

st.subheader("Spinner")
with st.spinner("Espere..."):
    time.sleep(5)
    st.success("Finalizo!")
st.subheader("Balloons")

#Ballons
st.balloons()
st.header("Trabajando con data science")
df = pd.read_csv("Police.csv",index_col = 0)
st.subheader("Dataframe")
st.dataframe(df)
st.subheader("tabla")
st.table(df.head())
st.subheader("grafica")
chart_data = pd.DataFrame({
    
    "col1": np.random.randn(20),
    "col2": np.random.randn(20),
    "col3": np.random.choice(["A","B","C"],20),
})
st.line_chart(chart_data, x = "col1", y = "col2", color = "col3")

st.sidebar.header("Acerca")
st.sidebar.text("Tutoria de streamlit")
st.header("Trabajando con funciones")
st.write(list(run_fxn(10)))
