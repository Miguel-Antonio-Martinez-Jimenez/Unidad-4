import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configuración inicial
np.random.seed(42)
random.seed(42)
total_registros = 5000

# Definición de dimensiones
productos = ['A', 'B', 'C', 'D', 'E']
regiones = ['Norte', 'Sur', 'Este', 'Oeste', 'Centro']

# Rango de fechas (2 años)
fecha_inicio = datetime(2023, 1, 1)
fecha_fin = datetime(2024, 12, 31)
diferencia_dias = (fecha_fin - fecha_inicio).days

# Generación de datos aleatorios
datos = []
for _ in range(total_registros):
    # Fecha aleatoria dentro del rango
    dias_aleatorios = random.randint(0, diferencia_dias)
    fecha = fecha_inicio + timedelta(days=dias_aleatorios)
    
    # Selección aleatoria de dimensiones
    producto = random.choice(productos)
    region = random.choice(regiones)
    
    # Ventas con distribución diferente por producto/región
    base_ventas = 50 if producto in ['A', 'B'] else 30
    variacion = random.randint(-20, 50)
    
    # Patrones estacionales
    if fecha.month in [11, 12]:  # Temporada alta
        variacion += random.randint(10, 30)
    elif fecha.month in [1, 2]:  # Temporada baja
        variacion -= random.randint(5, 15)
    
    # Patrones regionales
    if region == 'Norte':
        variacion += random.randint(5, 15)
    elif region == 'Sur':
        variacion -= random.randint(0, 10)
    
    ventas = max(10, base_ventas + variacion)  # Ventas mínimas de 10
    
    datos.append([fecha.date(), producto, region, ventas])

# Crear DataFrame
columnas = ['Fecha', 'Producto', 'Región', 'Ventas']
df = pd.DataFrame(datos, columns=columnas)

# Ordenar por fecha
df = df.sort_values('Fecha')

# Guardar a CSV
df.to_csv('ventas.csv', index=False)

print(f"Archivo 'ventas.csv' generado con {len(df)} registros")
print("Muestra de los datos:")
print(df.head())