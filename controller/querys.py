import pyodbc


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)

        return cls._instance

    def __init__(self):
        self.server = 'BUBBLES'
        self.database = 'Inventario'
        self.connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes;"
        self.connect()

    def connect(self):
        try:
            self.conn = pyodbc.connect(self.connection_string)
            print("Conexión exitosa a la base de datos.")
        except pyodbc.Error as error:
            print("Error al conectar a la base de datos:", error)
            return None

        self.cursor = self.conn.cursor()
        
    def execute(self, query, *args):
        try:
            if not self.conn:
                self.connect()
            self.cursor.execute(query, *args)
        except pyodbc.Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    def get_users_dict(self):
        query_users_dict = "SELECT ID_inventarista, Password, Apellidos, Nombres from TB_INVENTARISTA"
        self.execute(query_users_dict)
        users_dict = {val[0]: (val[1], f"{val[2]} {val[3]}") for val in self.cursor.fetchall()}
        return users_dict

    def get_products_list(self):
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
        self.execute(query_producto)
        productos = [list(row) for row in self.cursor.fetchall()]
        return productos

    def update_stock_for_user(self, value, product_id):
        update_query = """
        UPDATE TB_PRODUCTO
        SET Stock_producto = ?
        WHERE ID_producto = ?;
        """
        try:
            self.execute(update_query, value, product_id)
            self.conn.commit()
        except pyodbc.Error as e:
            print(f"Error al actualizar el stock: {e}")

    def get_inven_list(self):
        query_inventarista = """
        SELECT 
            ID_inventarista,
            Password,
            Apellidos,
            Nombres,
            CASE
                WHEN Tipo_Documento = 1 THEN 'DNI'
                ELSE 'Pasaporte'
            END AS Tipo_Droducto,
            Numero_documento,
            Direccion,
            ID_ubigeo,
            Telefono,
            Correo,
            Fecha_de_nacimiento,
            Sexo,
            Sueldo,
            CASE
                WHEN Turno = 'M' THEN 'Mañana'
                WHEN Turno = 'T' THEN 'Tarde'
                ELSE 'Noche'
            END AS Turno
        FROM TB_INVENTARISTA
        """
        self.execute(query_inventarista)
        inventaristas = [list(row) for row in self.cursor.fetchall()]
        return inventaristas

    def create_inventarista(self, data):
        try:
            query = '''INSERT INTO TB_INVENTARISTA (ID_inventarista, Apellidos, Nombres, Direccion, Tipo_Documento, 
                       Numero_documento, Fecha_de_nacimiento, Sexo, Sueldo, Turno, ID_ubigeo, Telefono, Correo, Password)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            
            self.cursor.execute(query, data)
            self.conn.commit()
            return True

        except pyodbc.Error as e:
            print(f"Error al insertar en la base de datos: {e}")
            return False

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Conexión terminada")
            self.conn = None

    def __del__(self):
        self.close_connection()
