import requests
import pandas as pd
from datetime import datetime, timedelta

# Función para generar una lista de fechas entre dos fechas
def generate_date_range(start_date, end_date):
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    return [(start + timedelta(days=x)).strftime('%Y-%m-%d') for x in range((end-start).days + 1)]

# Función para verificar si una fecha es fin de semana
def is_weekend(date_str):
    date = pd.to_datetime(date_str)
    return date.weekday() >= 5  # 5: Sábado, 6: Domingo

# Lista de feriados argentinos (a modo de ejemplo, puedes agregar más o actualizarlos)
feriados_arg = [
    '2024-01-01', '2024-02-12', '2024-02-13', '2024-03-24', '2024-03-29', '2024-04-02',
    '2024-05-01', '2024-05-25', '2024-06-20', '2024-07-09', '2024-08-17', '2024-10-12',
    '2024-12-08', '2024-12-25', '2022-03-24'
]

# Obtenemos la fecha actual
today = datetime.today().strftime('%Y-%m-%d')

# Agrego Header para que parezca que la solicitud viene de un navegador legítimo
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Definimos la fecha de inicio manualmente (o puedes calcularla dinámicamente)
start_date = '2020-05-01'

# URL dinámica con la fecha de hoy
url = f'https://mercados.ambito.com//dolarrava/cl/grafico/{start_date}/{today}'

# Realizamos la solicitud GET
response = requests.get(url, headers=headers)

# Revisamos si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    # Convertimos la respuesta en JSON
    data = response.json()
    
    # Convertimos los datos en un DataFrame de pandas
    df = pd.DataFrame(data[1:], columns=data[0])  # Ignoramos la primera fila y usamos los nombres de las columnas

    # Convertir la columna 'fecha' al formato de fecha
    df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

    # Generar el rango de fechas esperadas
    expected_dates = generate_date_range(start_date, today)

    # Verificar si faltan fechas
    missing_dates = set(expected_dates) - set(df['fecha'].tolist())

    if missing_dates:
        # Filtrar los fines de semana y feriados argentinos
        non_business_days = {date for date in missing_dates if is_weekend(date) or date in feriados_arg}
        business_days_missing = missing_dates - non_business_days

        if business_days_missing:
            print(f"Faltan datos para los siguientes días hábiles: {sorted(business_days_missing)}")
        else:
            print("Todas las fechas faltantes son fines de semana o feriados.")
    else:
        print("Hay cotización para todos los días.")
else:
    print(f"Error al realizar la solicitud: {response.status_code}")
