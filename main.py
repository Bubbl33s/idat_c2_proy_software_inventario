import pyodbc

# Detalles de conexión con Autenticación Integrada
server = 'BUBBLES'
database = 'Inventario'

# Crea la cadena de conexión
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"

# Intenta conectarse
try:
    conn = pyodbc.connect(connection_string)
    print("Conexión exitosa a la base de datos.")
except pyodbc.Error as error:
    print("Error al conectar a la base de datos:", error)

# CURSOR
cursor = conn.cursor()

# MOSTRAR DATOS
query_read = "SELECT ID_inventarista, Apellidos, Nombres FROM TB_INVENTARISTA"

cursor.execute(query_read)

for row in cursor.fetchall():
    print(row)

# CERRAR LA CONEXIÓN
conn.close()
