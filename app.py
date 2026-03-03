import streamlit as st
import datetime
import pandas as pd
from modules.data_generator import get_data, get_funnel_data, get_regional_data
from modules.charts import create_trend_chart, create_funnel_chart, create_map_chart, create_bar_chart
from modules.metrics import calculate_kpis, get_alerts

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Dashboard Ejecutivo", page_icon="📊", layout="wide")

# --- CSS PERSONALIZADO (Integración visual) ---
st.markdown("""
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    /* Ajustes para Modo Oscuro */
    @media (prefers-color-scheme: dark) {
        .metric-card {
            background-color: #0e1117;
        }
        .stMetric {
            background-color: #262730;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
    }
</style>
""", unsafe_allow_html=True)


# --- SIDEBAR (Filtros) ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2920/2920329.png", width=50)
st.sidebar.title("Configuración")

# Filtro de Fechas
start_date = st.sidebar.date_input("Fecha Inicio", datetime.date(2024, 1, 1))
end_date = st.sidebar.date_input("Fecha Fin", datetime.date.today())

if start_date > end_date:
    st.sidebar.error("Error: La fecha de inicio debe ser anterior al fin.")

periodo_filter = st.sidebar.selectbox(
    "Filtrar por Periodo:",
    options=["Últimos 30 días", "Último trimestre", "Último año"],
    index=0
)

categoria_filter = st.sidebar.selectbox(
    "Filtrar por Categoría:",
    options=["General", "Ventas", "Marketing", "Producto"],
    index=0
)

comparacion_filter = st.sidebar.selectbox(
    "Comparar con:",
    options=["Periodo anterior", "Año pasado", "Promedio"],
    index=0
)

# --- CARGA DE DATOS ---
# Usamos caché para no recalcular en cada interacción
# @st.cache_data
def load_data():
    return get_data()

# Cargar datos principales
df = load_data()
df_funnel = get_funnel_data()
df_regional = get_regional_data()

# --- CÁLCULO DE MÉTRICAS ---
kpis = calculate_kpis(df)
alerts = get_alerts(kpis)

# --- LAYOUT PRINCIPAL ---
st.title("📊 Dashboard Ejecutivo de Ventas")
st.markdown("### Visión General del Rendimiento Comercial")

# 1. ALERTAS INTELIGENTES
for type, msg in alerts:
    if type == "success":
        st.success(f"✅ {msg}")
    elif type == "error":
        st.error(f"🚨 {msg}")
    else:
        st.info(f"ℹ️ {msg}")

st.markdown("---")
st.subheader("🔍 KPIs Clave y Tendencias")

# 2. KPIs (Key Performance Indicators)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💵 Ingresos Totales", kpis['ingresos']['valor'], f"{kpis['ingresos']['delta']:.1f}%")
with col2:
    st.metric("👥 Usuarios Activos", kpis['usuarios']['valor'], f"{kpis['usuarios']['delta']:.1f}%")
with col3:
    st.metric("🎯 Tasa Conversión", kpis['conversion']['valor'], f"{kpis['conversion']['delta']:.2f}%")
with col4:
    st.metric("💰 CAC Promedio", kpis['cac']['valor'], f"-{kpis['cac']['delta']:.1f}%") # Negativo 

st.markdown("---")

# 3. GRÁFICOS INTERACTIVOS

# Fila 1: Tendencia y Embudo
row1_col1, row1_col2 = st.columns([2, 1]) # Proporción 2:1

with row1_col1:
    st.subheader("📈 Evolución de Ingresos (con Tendencia)")
    fig_trend = create_trend_chart(df)
    st.plotly_chart(fig_trend, use_container_width=True)

with row1_col2:
    st.subheader("🔽 Embudo de Conversión (Leads -> Ventas)")
    fig_funnel = create_funnel_chart(df_funnel)
    st.plotly_chart(fig_funnel, use_container_width=True)

# Fila 2: Mapa Geográfico
st.subheader("🌍 Distribución Regional (LatAm)")

fig_map = create_map_chart(df_regional)
st.plotly_chart(fig_map, use_container_width=True)

# Fila 3: Gráfico de Barras
st.subheader("📊 Ventas por Ciudad")

fig_bar = create_bar_chart(df_regional)
st.plotly_chart(fig_bar, use_container_width=True)

# 4. TABLA DE DATOS (DETALLE)
with st.expander("Ver Datos Detallados (Tabla)"):
    st.dataframe(df) # Streamlit dataframe básico es más seguro