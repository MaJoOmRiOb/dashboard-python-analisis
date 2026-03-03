import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def get_data():
    # Generar rango de fechas
    hoy = datetime.today()
    dates = pd.date_range(start='2023-01-01', end=hoy, freq='D')
    n_days = len(dates)

    df = pd.DataFrame({
        'fecha': dates,
        'ingresos_diarios': np.random.randint(15000, 50000, n_days),
        'usuarios_activos': np.random.randint(3000, 12000, n_days),
        'tasa_conversion': np.random.uniform(0.8, 2.5, n_days),
        'costo_adquisicion': np.random.uniform(12, 45, n_days),
        'ltv_cliente': np.random.uniform(40, 180, n_days) # Lifetime Value cliente
    })

    # Actualizar ingresos diarios para simular una tendencia de crecimiento
    df['ingresos_diarios'] *= (1 + np.arange(len(df)) * 0.0001) # tendencia aproximadamente 0.01% diario
    
    return df

def get_funnel_data():
    """Retorna datos para el gráfico de embudo"""
    stages = ['Visitas Web', 'Leads Calificados', 'Oportunidades', 'Negociaciones', 'Ganadas']
    values = [15000, 4500, 2000, 800, 350] # Embudo clásico
    return pd.DataFrame({'etapa': stages, 'cantidad': values})

def get_regional_data():
    """Datos simulados por región/ciudad principal"""
    ciudades = ['Lima', 'Bogotá', 'Santiago', 'Buenos Aires', 'Quito', 'Sao Paulo', 'Ciudad de México', 'Caracas', 'Montevideo', 'Asunción']
    cities = {
        'ciudad': ciudades,
        'lat': [-12.0464, 4.7110, -33.4489, -34.6037, -0.1807, -23.5505, 19.4326, 10.4806, -34.9011, -25.2637],
        'lon': [-77.0428, -74.0721, -70.6693, -58.3816, -78.4678, -46.6333, -99.1332, -66.9036, -56.1645, -57.5759],
        'ventas': np.random.uniform(100000, 10000, len(ciudades))
    }
    return pd.DataFrame(cities)
