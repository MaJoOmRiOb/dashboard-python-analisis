import pandas as pd
import numpy as np
from datetime import datetime

def calculate_kpis(df):
    """
    Calcula KPIs principales y determina alertas.
    Returns: Dict con valores, deltas y estado de alerta
    """
    # 1. Ingresos Totales de los últimos 30 días
    last_30_days = df.tail(30)
    ingresos_total = last_30_days['ingresos_diarios'].sum()
    
    # Comparativa vs mes anterior (simple: los 30 días previos a eso)
    prev_30_days = df.iloc[-60:-30]
    ingresos_prev = prev_30_days['ingresos_diarios'].sum()
    
    # Evitar división por cero
    if ingresos_prev == 0:
        delta_ingresos = 100.0
    else:
        delta_ingresos = ((ingresos_total - ingresos_prev) / ingresos_prev) * 100
    
    # 2. Usuarios Activos (Promedio mensual)
    usuarios_promedio = last_30_days['usuarios_activos'].mean()
    usuarios_prev = prev_30_days['usuarios_activos'].mean()
    
    if usuarios_prev == 0:
        delta_usuarios = 100.0
    else:
        delta_usuarios = ((usuarios_promedio - usuarios_prev) / usuarios_prev) * 100
    
    # 3. Tasa de Conversión (Simulada, depende de leads vs ventas)
    # Suponiendo que 'Ingresos' correlaciona con conversion. En un caso real usaríamos ventas / visitas.
    tasa_conversion = (last_30_days['ingresos_diarios'].mean() / 150000) # Dummy formula

    # 4. CAC (Costo de Adquisición de Clientes) - Simulado como promedio del costo_adquisicion
    # En un caso real, esto se calcularía como gasto en marketing dividido por número de clientes adquiridos en el periodo.
    cac_promedio = last_30_days['costo_adquisicion'].mean()

    
    return {
        "ingresos": {
            "valor": f"${ingresos_total:,.0f}",
            "delta": delta_ingresos,
            "alerta": "normal" if delta_ingresos > 0 else "warning"
        },
        "usuarios": {
            "valor": int(usuarios_promedio),
            "delta": delta_usuarios,
            "alerta": "normal" if delta_usuarios > 0 else "critical"
        },
        "conversion": {
            "valor": f"{tasa_conversion:.2f}%",
            "delta": np.random.uniform(-0.5, 1.2), # Simulado
            "alerta": "success" if tasa_conversion > 0.05 else "warning"
        },
        "cac": {
            "valor": f"${cac_promedio:.0f}",
            "delta": np.random.uniform(2, 8), # Simulado
            "alerta": "inverse" if cac_promedio < 20 else "critical"
        }
    }

def get_alerts(kpis):
    """
    Genera lista de mensajes de alerta basados en los KPIs
    """
    alerts = []
    
    # Lógica de negocio simple
    ingresos_delta = kpis['ingresos']['delta']
    
    if ingresos_delta > 10:
        alerts.append(("success", "¡Récord de ventas! Crecimiento superior al 10% mensual."))
    elif ingresos_delta < -5:
        alerts.append(("error", "Alerta Crítica: Los ingresos han caído significativamente."))
    else:
        alerts.append(("info", "Estabilidad operativa: Métricas dentro del rango normal."))
        
    return alerts
