import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Cubo OLAP Interactivo", layout="wide")
st.title("📊 Análisis Multidimensional con Cubos OLAP")

# Carga de datos (simulados si no existe el archivo)
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("ventas.csv", parse_dates=["Fecha"])
    except:
        # Generar datos de ejemplo si no hay archivo
        import numpy as np
        np.random.seed(42)
        fechas = pd.date_range(start="2023-01-01", end="2024-12-31", freq="D")
        productos = ["A", "B", "C", "D"]
        regiones = ["Norte", "Sur", "Este", "Oeste"]
        data = {
            "Fecha": np.random.choice(fechas, 5000),
            "Producto": np.random.choice(productos, 5000),
            "Región": np.random.choice(regiones, 5000),
            "Ventas": np.random.randint(50, 500, 5000)
        }
        df = pd.DataFrame(data)
        df.to_csv("ventas.csv", index=False)
    
    df["Mes"] = df["Fecha"].dt.month_name()
    df["Trimestre"] = df["Fecha"].dt.to_period("Q").astype(str)
    df["Año"] = df["Fecha"].dt.year
    return df

df = load_data()

# Sidebar con controles OLAP
st.sidebar.header("🔧 Controles OLAP")

# Filtros (Slice/Dice)
productos = st.sidebar.multiselect(
    "Seleccionar Productos", 
    df["Producto"].unique(), 
    default=df["Producto"].unique()
)

regiones = st.sidebar.multiselect(
    "Seleccionar Regiones", 
    df["Región"].unique(), 
    default=df["Región"].unique()
)

años = st.sidebar.multiselect(
    "Seleccionar Años", 
    df["Año"].unique(), 
    default=df["Año"].unique()
)

# Operaciones OLAP
operacion = st.sidebar.radio(
    "Operación OLAP", 
    ["Raw Data", "Roll-up (Año/Producto)", "Drill-down (Mes/Región)", "Pivot (Región vs. Producto)"]
)

# Aplicar filtros
filtered_df = df[
    (df["Producto"].isin(productos)) &
    (df["Región"].isin(regiones)) &
    (df["Año"].isin(años))
]

# Mostrar resultados según operación
st.header(f"🧮 {operacion}")
if operacion == "Raw Data":
    st.dataframe(filtered_df, height=400)

elif operacion == "Roll-up (Año/Producto)":
    rollup = filtered_df.groupby(["Año", "Producto"])["Ventas"].sum().reset_index()
    fig = px.bar(
        rollup, 
        x="Año", 
        y="Ventas", 
        color="Producto", 
        barmode="group",
        title="Roll-up: Ventas Agregadas por Año y Producto"
    )
    st.plotly_chart(fig, use_container_width=True)

elif operacion == "Drill-down (Mes/Región)":
    drill = filtered_df.groupby(["Año", "Mes", "Región"])["Ventas"].sum().reset_index()
    fig = px.line(
        drill, 
        x="Mes", 
        y="Ventas", 
        color="Región", 
        facet_col="Año",
        title="Drill-down: Ventas por Mes y Región"
    )
    st.plotly_chart(fig, use_container_width=True)

elif operacion == "Pivot (Región vs. Producto)":
    pivot = filtered_df.pivot_table(
        values="Ventas", 
        index="Región", 
        columns="Producto", 
        aggfunc="sum", 
        fill_value=0
    )
    fig = px.imshow(
        pivot,
        labels=dict(x="Producto", y="Región", color="Ventas"),
        title="Pivot: Matriz Región vs. Producto (Heatmap)"
    )
    st.plotly_chart(fig, use_container_width=True)

# Métricas resumen
st.sidebar.divider()
st.sidebar.subheader("📊 Métricas Clave")
total_ventas = filtered_df["Ventas"].sum()
avg_ventas = filtered_df["Ventas"].mean()
st.sidebar.metric("Ventas Totales", f"${total_ventas:,.0f}")
st.sidebar.metric("Promedio por Transacción", f"${avg_ventas:,.2f}")

# Instrucciones
with st.expander("ℹ️ Cómo usar esta app"):
    st.markdown("""
    - **Slice/Dice**: Usa los filtros para seleccionar subconjuntos de datos.
    - **Roll-up**: Agrupa datos por año y producto.
    - **Drill-down**: Explora ventas mensuales por región.
    - **Pivot**: Matriz de calor para comparar regiones y productos.
    """)

# Exportar a Excel
if st.button("💾 Exportar a Excel"):
    filtered_df.to_excel("datos_filtrados.xlsx", index=False)
    st.success("¡Archivo exportado como 'datos_filtrados.xlsx'!")