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
query_producto = """
SELECT
    P.ID_producto,
    P.Descripcion_producto,
    P.Precio,
    CASE WHEN P.Estado_producto = 1 THEN 'Activo' ELSE 'Inactivo' END AS Estado_producto,
    P.Stock_producto,
    P.Peso_producto,
    P.Fecha_de_ingreso,
    SF.Descripcion_subfamilia,
    F.Descripcion_familia,
    L.Descripcion_linea
FROM TB_PRODUCTO P
JOIN TB_SUBFAMILIA SF ON P.ID_subfamilia = SF.ID_subfamilia
JOIN TB_FAMILIA F ON SF.ID_familia = F.ID_familia
JOIN TB_LINEA L ON F.ID_linea = L.ID_linea
"""

cursor.execute(query_producto)

for row in cursor.fetchall():
    # Convierte los campos Decimal y datetime.date a float y str, respectivamente.
    id_producto = row[0]
    descripcion_producto = row[1]
    precio = float(row[2])
    estado_producto = row[3]
    stock_producto = row[4]
    peso_producto = float(row[5])
    fecha_de_ingreso = str(row[6])
    descripcion_subfamilia = row[7]
    descripcion_familia = row[8]
    descripcion_linea = row[9]

    # Imprime los datos.
    print(id_producto, descripcion_producto, precio, estado_producto, stock_producto,
          peso_producto, fecha_de_ingreso, descripcion_subfamilia, descripcion_familia, descripcion_linea)

# CERRAR LA CONEXIÓN
conn.close()