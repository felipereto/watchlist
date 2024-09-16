import yfinance as yf
from datetime import datetime
import pandas as pd

# Definir el rango de fechas
start_date = "2020-05-01"  # Fecha de inicio
end_date = datetime.today().strftime('%Y-%m-%d')  # Fecha de fin (hoy)

tickers = ["BBAR.BA", "CEPU.BA", "AAPL.BA", "TGNO4.BA", "PAMP.BA", "AMZN.BA"]

# Obtener los datos históricos desde 2020-05-01 hasta hoy
stock_data = yf.download(tickers, start=start_date, end=end_date, interval="1d")

# Seleccionar las cotizaciones de cierre
df_close = stock_data['Close']

# Usar melt para transformar las columnas en filas
df_melted = df_close.reset_index().melt(id_vars="Date", var_name="Ticker", value_name="Close")

# Mostrar el DataFrame transformado
print(df_melted)
