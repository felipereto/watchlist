import requests
import pandas as pd
from datetime import datetime

# Obtenemos la fecha actual
today = datetime.today().strftime('%Y-%m-%d')

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
    # Convertimos la respuesta en JSON (si es el caso)
    data = response.json()

    # Convertimos los datos en un DataFrame de pandas
    df = pd.DataFrame(data)

    # Mostramos el DataFrame
    print(df)
else:
    print(f"Error al realizar la solicitud: {response.status_code}")
