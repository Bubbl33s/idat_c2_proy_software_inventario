import pyodbc

# Detalles de conexión con Autenticación Integrada
server = 'BUBBLES'
database = 'Inventario'

# Crea la string para la conexión
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"

# Intenta conectarse a la base de datos
try:
    conn = pyodbc.connect(connection_string)
    print("Conexión exitosa a la base de datos.")
except pyodbc.Error as error:
    print("Error al conectar a la base de datos:", error)

# CURSOR
cursor = conn.cursor()


def get_users_dict():
    query_users_dict = "SELECT ID_inventarista, Password, Apellidos, Nombres from TB_INVENTARISTA"
    cursor.execute(query_users_dict)

    # Crea un diccionario con el usuario y contraseña de los inventaristas
    users_dict = {val[0]: (val[1], f"{val[2]} {val[3]}") for val in cursor.fetchall()}

    return users_dict


# Crea una lista con la tabla de productos de la base de datos
def get_products_list():
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

    # Llena la lista vacía
    for row in cursor.fetchall():
        dato = [r for r in row]

        productos.append(dato)

    return productos


def update_stock_for_user(value, product_id):
    update_query = """
    UPDATE TB_PRODUCTO
    SET Stock_producto = ?
    WHERE ID_producto = ?;
    """

    try:
        # Ejecuta el query con los parámetros proporcionados
        cursor.execute(update_query, value, product_id)
        conn.commit()

    except pyodbc.Error as e:
        print(f"Error al actualizar el stock: {e}")


def close_connection():
    # CERRAR LA CONEXIÓN
    conn.close()
    print("Conexión terminada")


if __name__ == "__main__":
    print(get_users_dict())
