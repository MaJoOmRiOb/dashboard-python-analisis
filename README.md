# 📊 Dashboard Estratégico CRM (Python + Streamlit)

> **Un dashboard interactivo de alto nivel para el análisis de ventas y rendimiento comercial**, construido con tecnologías de Data Science modernas.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-ff4b4b)
![Plotly](https://img.shields.io/badge/Visualizaci%C3%B3n-Plotly-3f4f75)

## 💡 Sobre el Proyecto

Este proyecto simula un entorno de análisis de datos para una empresa SaaS o Retail. A diferencia de dashboards estáticos (Excel/PowerBI), este aplicativo genera **datos en tiempo real**, calcula **tendencias estadísticas** (regresión lineal) y utiliza **lógica de negocio** para detectar anomalías automáticamente.

El objetivo es demostrar cómo Python puede integrar:
1.  **Ingeniería de Datos (ETL):** Generación y limpieza de pandas DataFrames simulados con patrones realistas.
2.  **Lógica de Negocio:** KPIs dinámicos y sistemas de alerta basados en umbrales.
3.  **Visualización Avanzada:** Gráficos interactivos y mapas geoespaciales de rendimiento.

---

## 🚀 Características Clave

*   **Generador de Datos "Faker":** Simulación matemática de ventas con estacionalidad, tendencias y ruido aleatorio (NumPy).
*   **Sistema de Alertas Inteligentes:** Algoritmo que evalúa el rendimiento (Ingresos/Usuarios) y notifica automáticamente si hay caídas críticas o récords históricos.
*   **Visualización Geoespacial:** Mapa de calor de ventas en ciudades clave de región LATAM.
*   **Análisis Estadístico:** Proyección de tendencia de ingresos mediante regresión lineal (OLS).
*   **Filtros Interactivos:** Control total sobre rangos de fechas y regiones desde el sidebar.
*   **Soporte de Modo Oscuro:** Interfaz adaptativa que detecta la configuración del tema del sistema operativo.

---

## 🛠️ Arquitectura del Proyecto

El código sigue principios de **Clean Code** y **Modularidad**, separando la interfaz de la lógica y los datos.

```text
dashboard-python-analisis/
│
├── app.py                 # 🎮 Controlador Principal: Interfaz de usuario (Streamlit)
│
├── modules/               # 🧠 Lógica de Negocio Desacoplada
│   ├── data_generator.py  # Fábrica de Datos: Simulación de series temporales
│   ├── metrics.py         # Motor de Cálculo: Lógica de KPIs y Alertas
│   └── charts.py          # Capa Visual: Funciones de graficado (Plotly)
│
├── dashboard_env/         # 🐍 Entorno Virtual (Aislado)
├── requirements.txt       # 📦 Dependencias del proyecto
└── README.md              # 📄 Documentación (Estás aquí)
```

### Descripción de Módulos

*   **`app.py`**: Orquesta la aplicación. Gestiona el estado de la sesión, los filtros del usuario, invoca a los módulos y define el layout de la página.
*   **`modules/data_generator.py`**: Utiliza `numpy` para crear distribuciones normales y tendencias lineales que simulan el comportamiento real de un mercado, evitando la necesidad de archivos CSV estáticos.
*   **`modules/metrics.py`**: Contiene la lógica pura para comparar mes actual vs mes anterior (`delta`) y decidir si mostrar una alerta de éxito 🟢, advertencia 🟠 o error 🔴.
*   **`modules/charts.py`**: Encapsula la complejidad de `plotly.graph_objects` y `plotly.express` para mantener el código principal limpio y reutilizable.

---

## 💻 Instalación y Ejecución Local

Sigue estos pasos para correr el dashboard en tu máquina:

### 1. Clonar o Descargar
```bash
git clone <tu-repositorio-url>
cd dashboard-python-analisis
```

### 2. Crear Entorno Virtual (Recomendado)
Para mantener las dependencias aisladas del sistema:
```bash
# Windows
python -m venv dashboard_env
.\dashboard_env\Scripts\Activate

# Nota: Si obtienes error de permisos en PowerShell, ejecuta primero:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Mac/Linux
python3 -m venv dashboard_env
source dashboard_env/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la Aplicación
```bash
streamlit run app.py
```
El dashboard se abrirá automáticamente en tu navegador (usualmente en `http://localhost:8501`).

---

## 📈 Próximos Pasos (Roadmap)
- [ ] Conexión a base de datos SQL real (PostgreSQL/SQLite).
- [ ] Implementación de modelo de Machine Learning (Random Forest) para predicción de Churn.
- [ ] Exportación de reportes a PDF.

---
**Desarrollado por M Rivera** — *Analista CRM*
