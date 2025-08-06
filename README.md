# 🚀 Análisis OLAP Multidimensional con Python y Streamlit

Este proyecto implementa un sistema completo de análisis OLAP (Procesamiento Analítico en Línea) que permite explorar datos multidimensionales de ventas mediante diferentes operaciones analíticas, visualizaciones interactivas y exportación para Power BI.

---

## 📋 Contenido del Proyecto

- `app.py`: Aplicación Streamlit interactiva para análisis OLAP.
- `generador_ventas_csv.py`: Script para generar datos de ventas simulados.
- `olap_practica.py`: Implementación básica de operaciones OLAP con pandas.
- `ventas.csv`: Dataset generado (5000 registros).
- `cubo_para_powerbi.xlsx`: Salida en Excel para análisis en Power BI.
- `README.md`: Este archivo.

---

## 🌟 Características Principales

✅ **Operaciones OLAP completas:**
- **Roll-up** (agregación)
- **Drill-down** (desagregación)
- **Slice/Dice** (filtrado multidimensional)
- **Pivot** (rotación de perspectivas)

✅ **Visualizaciones interactivas con Plotly:**
- Gráficos de barras agrupadas
- Heatmaps para comparaciones
- Gráficos de líneas temporales

✅ **Funcionalidades adicionales:**
- Filtros interactivos por producto, región y año
- Exportación de resultados a Excel
- Métricas clave en tiempo real

---

## 🛠️ Requisitos Técnicos

- Python 3.8 o superior
- Librerías necesarias:
  ```bash
  streamlit
  pandas
  plotly
  numpy
  openpyxl
