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


def get_users_dict():
    query_users = "SELECT ID_inventarista, Password from TB_INVENTARISTA"
    cursor.execute(query_users)

    users_dict = {v.lower(): k for v, k in cursor.fetchall()}

    return users_dict


def get_product_list():
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
    productos = []

    for row in cursor.fetchall():
        dato = [r for r in row]

        productos.append(dato)

    return productos


def cerrar_conexion():
    # CERRAR LA CONEXIÓN
    conn.close()


if __name__ == "__main__":
    print(get_users_dict())
