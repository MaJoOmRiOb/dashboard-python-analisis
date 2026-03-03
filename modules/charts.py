import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def create_trend_chart(df):
    
    # Gráfico de Tendencia de Ingresos Diarios con Regresión Lineal
    
    # Agregar columna numérica para regresión
    x = np.arange(len(df))
    # Calcular línea de tendencia simple con Numpy (y = mx + b)
    z = np.polyfit(x, df['ingresos_diarios'], 1)
    p = np.poly1d(z)
    
    # Crear gráfico base
    fig = px.line(df, x='fecha', y='ingresos_diarios', title='Evolución de Ingresos', template='plotly_white')

    # fig = go.Figure()

    # # Añadir línea de tendencia
    # fig.add_trace(
    #     go.Scatter(
    #         x=df['fecha'],
    #         y=df['ingresos_diarios'],
    #         mode='lines',
    #         name='Ingresos Reales'
    #     )
    # )
    
    # Añadir línea de tendencia
    fig.add_trace(
        go.Scatter(
            x=df['fecha'],
            y=p(x),
            mode='lines',
            name='Tendencia (Regresión)',
            line=dict(color='red', dash='dash')
        )
    )
    
    # Ajustes estéticos (Eliminar grid excesivo)
    fig.update_layout(template='plotly_white', height=500)
    
    return fig

def create_funnel_chart(df_funnel):
    
    # Gráfico de Embudo de Conversión
    
    # Calcular porcentajes de retención entre cada paso
    # (Opcional, Plotly lo hace automático si usas FunnelArea)
    
    fig = go.Figure(go.Funnel(
        y = df_funnel['etapa'],
        x = df_funnel['cantidad'],
        textinfo = 'value+percent initial'
    ))
    
    fig.update_layout(template='plotly_white', height=500)
    
    return fig

def create_map_chart(df_regions):
    
    # Mapa de Calor Geográfico (Ciudades principales)
    
    # Usamos Scatter Mapbox para círculos que varían por tamaño (ventas) y color (ventas)
    fig = px.scatter_mapbox(
        df_regions,
        lat='lat',
        lon='lon',
        hover_name='ciudad',
        hover_data=['ventas'],
        color='ventas',
        size='ventas',
        color_continuous_scale=px.colors.cyclical.IceFire, 
        size_max=35, 
        zoom=3,
        mapbox_style='open-street-map' # Estilo gratis, no requiere token
    )
    
    # fig.update_layout(title='🌍 Distribución de Ventas por Ciudad Clave')
    return fig

def create_bar_chart(df):
    
    # Gráfico de Barras para comparar ventas por ciudad
    
    fig = px.bar(
        df,
        x='ciudad',
        y='ventas',
        color='ventas',
        color_continuous_scale='Viridis',
        title='🏢 Ventas por Ciudad'
    )

    fig.update_layout(xaxis_title='Ciudad', yaxis_title='Ventas', height=500, template='plotly_white', showlegend=False)
    
    return fig