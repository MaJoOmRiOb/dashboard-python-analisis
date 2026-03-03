# Plan de Proyecto: Dashboard Estratégico CRM (Python + Streamlit)

> **Objetivo:** Crear una aplicación web interactiva que demuestre habilidades avanzadas en Ingeniería de Datos, Lógica de Negocio (CRM) y Visualización. Este proyecto servirá como pieza central técnica en el portafolio.

---

## 1. Stack Tecnológico y Racional

La elección de tecnologías no es aleatoria; responde a criterios de eficiencia, escalabilidad y estándares de la industria de datos.

| Tecnología | Racional (El "Por qué") |
| :--- | :--- |
| **Python 3.10+** | Lenguaje universal para Data Science. Permite integrar lógica de negocio compleja (scripts de cálculo) que SQL o Excel no pueden manejar fácilmente. |
| **Streamlit** | Framework que convierte scripts de Python en web apps en minutos. **Decisión:** Se elige sobre Django/Flask porque el foco es el *dato* y la *interactividad*, no el desarrollo web frontend tradicional. |
| **Pandas & NumPy** | Estándar de la industria para manipulación vectorial de datos. Esencial para limpiar, filtrar y agregar grandes volúmenes de simulaciones. |
| **Plotly Express** | Librería de gráficos interactivos. **Decisión:** Se elige sobre Matplotlib/Seaborn porque un dashboard web debe permitir *hacer zoom, filtrar y ver tooltips* (hover), algo que las imágenes estáticas no permiten. |
| **Scikit-Learn (Opcional)** | Para la regresión lineal simple. Añade una capa de "Machine Learning" real al cálculo de tendencias. |

---

## 2. Arquitectura del Proyecto

Para demostrar "Clean Code" y mantenibilidad, no usaremos un archivo gigante `app.py`. Usaremos una estructura modular.

```text
dashboard-python-analisis/
│
├── .gitignore             # Archivos a ignorar (venv, .DS_Store)
├── README.md              # Documentación técnica para el repositorio
├── requirements.txt       # Dependencias (reproducibilidad)
│
├── app.py                 # Punto de entrada (Layout principal y UI)
│
└── modules/               # Módulos de lógica separada
    ├── __init__.py
    ├── data_generator.py  # Fábrica de datos (Simulación empresarial)
    ├── charts.py          # Lógica de visualización (Plotly)
    └── metrics.py         # Cálculos de KPIs y lógica de alertas
```

---

## 3. Generación de Datos (Faker & Numpy)

En lugar de cargar un CSV estático, generaremos datos al vuelo. Esto demuestra capacidad de manejar datos dinámicos.

*   **Ingresos:** Serie de tiempo con tendencia estacional + ruido aleatorio (usando `numpy.random`).
*   **Usuarios:** Crecimiento exponencial suave.
*   **Embudo:** Generación lógica donde `Leads > Oportunidades > Cierres`.
*   **Regiones:** Asignación ponderada para que algunas regiones (ej. Lima/Bogotá) tengan más peso que otras.

---

## 4. Diseño de Interfaz y UX

### A. Sidebar (Panel de Control)
*   **Filtros Globales:** Afectan a todo el dashboard.
    *   *Rango de Fechas:* Selector de calendario.
    *   *Región:* Multiselect (Perú, Colombia, Chile, etc.).
    *   *Segmento:* Negocio (B2B vs B2C).

### B. KPI Row (Métricas en Tiempo Real)
Uso de `st.metric` para mostrar el valor actual y el `delta` (comparación con el mes anterior).
*   **Ingresos Totales** (ej. $120k `↑ 12%`)
*   **Usuarios Activos** (ej. 1,200 `↓ 5%`)
*   **CAC (Costo de Adquisición)** (ej. $45 `↑ 2%` - *Alerta: Rojo si sube*)

### C. Sistema de Alertas Inteligentes
Bloque condicional al inicio del dashboard que analiza los KPIs.
*   🟢 **Éxito:** "Récord histórico de ventas superado".
*   🟠 **Advertencia:** "El CAC ha subido un 10% esta semana".
*   🔴 **Crítico:** "La tasa de conversión está por debajo del límite (2%)".

---

## 5. Visualizaciones Clave

### 1. Tendencia de Ingresos con Regresión Lineal
*   **Gráfico:** Línea de tiempo (Line Chart).
*   **Valor Agregado:** Superponer una línea punteada de tendencia calculada (Regresión OLS) para responder: _"¿Vamos subiendo o bajando realmente más allá del ruido diario?"_

### 2. Embudo de Conversión (Funnel Chart)
*   **Gráfico:** Funnel Area.
*   **Datos:** `Visitas Web -> Leads -> Oportunidades -> Ventas Cerradas`.
*   **Insight:** Tasa de conversión entre cada paso visible al pasar el mouse.

### 3. Mapa de Calor Geográfico (Estrategia)
*   **Reto:** Los mapas de contorno (Choropleth) requieren archivos GeoJSON pesados que complican la carga.
*   **Solución Propuesta:** `Plotly Density Mapbox` o `Scatter Map`.
    *   Usaremos coordenadas (Lat/Lon) de ciudades principales de Sudamérica (Lima, Bogotá, Santiago, Buenos Aires).
    *   El tamaño de la burbuja representará el volumen de ventas.
    *   El color representará la rentabilidad.
    *   *Ventaja:* Carga rápido, es interactivo y muy estético sin necesidad de polígonos complejos.

---

## 6. Pasos de Implementación

- [x] **Inicio:** Crear repo y entorno virtual (`python -m venv dashboard_env`).
- [x] **Base:** Crear `modules/data_generator.py` y probar que genera DataFrames correctos.
  - *Nota:* Se corrigió el orden de parámetros en `np.random` para evitar errores de rango.
- [x] **UI Esqueleto:** Montar `app.py` con el sidebar y los contenedores vacíos.
- [x] **Gráficos:** Implementar uno por uno en `modules/charts.py` y conectarlos.
- [x] **Refinamiento:** Ajustar colores, textos, agregar Alertas Inteligentes y soporte para **Modo Oscuro**.
- [x] **Deploy:** Listo para subir a Streamlit Cloud.
