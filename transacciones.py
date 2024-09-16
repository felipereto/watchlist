import psycopg2

# Parámetros de conexión
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)

# Crea un cursor
cur = conn.cursor()

# Ejecuta una consulta para obtener los datos de la tabla
cur.execute("SELECT * FROM transacciones;")

# Obtiene todos los resultados de la consulta
rows = cur.fetchall()

# Imprime los resultados
for row in rows:
    print(row)

# Cierra el cursor y la conexión
cur.close()
conn.close()
