import pyodbc
import random


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

        if not hasattr(self, 'conn') or self.conn is None:
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
# CRUD
# PRODUCTO -----------------------------------------------------------------------------------------------------------
    def create_producto(self, data):
        try:
            query = '''INSERT INTO TB_PRODUCTO (Descripcion_producto, Precio, Estado_producto, Stock_producto, 
                    Peso_producto, Fecha_de_ingreso, ID_subfamilia)
                    VALUES (?, ?, ?, ?, ?, ?, ?)'''
            
            self.cursor.execute(query, data)
            self.conn.commit()
            return True

        except pyodbc.Error as e:
            print(f"Error al insertar producto en la base de datos: {e}")
            return False

    def update_producto(self, data):
        try:
            query = '''UPDATE TB_PRODUCTO
                    SET Descripcion_producto = ?, Precio = ?, Estado_producto = ?, Stock_producto = ?, 
                        Peso_producto = ?, Fecha_de_ingreso = ?, ID_subfamilia = ?
                    WHERE ID_producto = ?'''

            # Reordenamos la data para que el ID sea el último en la lista
            data_reordered = data[1:] + (data[0],)
            
            self.cursor.execute(query, data_reordered)
            self.conn.commit()

            # Verificamos si se hizo alguna actualización
            if self.cursor.rowcount == 0:
                print("No se encontró el producto con el ID especificado.")
                return False
            return True

        except pyodbc.Error as e:
            print(f"Error al actualizar producto en la base de datos: {e}")
            return False
        
    def delete_producto(self, producto_id):
        try:
            query = '''DELETE FROM TB_PRODUCTO WHERE ID_producto = ?'''
            
            self.cursor.execute(query, (producto_id,))
            self.conn.commit()

            if self.cursor.rowcount == 0:
                print("No se encontró el producto con el ID especificado.")
                return False
            return True

        except pyodbc.Error as e:
            print(f"Error al eliminar producto de la base de datos: {e}")
            return False

# INVENTARISTA ---------------------------------------------------------------------------------------------------
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

    def update_inventarista(self, data):
        try:
            query = '''UPDATE TB_INVENTARISTA
                    SET Apellidos = ?, Nombres = ?, Direccion = ?, Tipo_Documento = ?, Numero_documento = ?, 
                        Fecha_de_nacimiento = ?, Sexo = ?, Sueldo = ?, Turno = ?, ID_ubigeo = ?, 
                        Telefono = ?, Correo = ?, Password = ?
                    WHERE ID_inventarista = ?'''

            # Reordenamos la data para que el ID sea el último en la lista
            data_reordered = data[1:] + (data[0],)
            
            self.cursor.execute(query, data_reordered)
            self.conn.commit()

            # Verificamos si se hizo alguna actualización
            if self.cursor.rowcount == 0:
                print("No se encontró el inventarista con el ID especificado.")
                return False
            return True

        except pyodbc.Error as e:
            print(f"Error al actualizar en la base de datos: {e}")
            return False

    def delete_inventarista(self, inventarista_id):
        try:
            query = '''DELETE FROM TB_INVENTARISTA WHERE ID_inventarista = ?'''
            
            self.cursor.execute(query, (inventarista_id,))
            self.conn.commit()
            return True

        except pyodbc.Error as e:
            print(f"Error al eliminar al inventarista de la base de datos: {e}")
            return False

# TB_SESION --------------------------------------------------------------------------------
    # Método para obtener el siguiente ID de sesión
    def get_next_session_id(self):
        try:
            query = "SELECT TOP 1 ID_sesion FROM TB_SESION ORDER BY ID_sesion DESC"
            self.execute(query)
            last_id = self.cursor.fetchone()[0]
            last_num = int(last_id[1:])
            next_num = str(last_num + 1).zfill(5)
            return "S" + next_num
        except:
            return "S00001"
    
    # Método para obtener un ID_pocket aleatorio
    def get_random_pocket_id(self):
        query = "SELECT ID_pocket FROM TB_POCKET"
        self.execute(query)
        all_ids = [row[0] for row in self.cursor.fetchall()]
        return random.choice(all_ids)

    # Método para insertar una nueva sesión
    def start_session(self, user_id):
        session_id = self.get_next_session_id()
        pocket_id = self.get_random_pocket_id()
        query = """INSERT INTO TB_SESION (ID_sesion, ID_inventarista, ID_pocket, Fecha_sesion, Hora_inicio)
                   VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"""
        self.execute(query, session_id, user_id, pocket_id)
        self.conn.commit()
        return session_id  # Esto es útil para actualizar la sesión al final.

    # Método para finalizar una sesión
    def end_session(self, session_id):
        query = "UPDATE TB_SESION SET Hora_fin = CURRENT_TIMESTAMP WHERE ID_sesion = ?"
        self.execute(query, session_id)
        self.conn.commit()

    def insert_cambio_sesion(self, session_id, product_id, cantidad_cambiada):
        self.cursor.execute("SELECT MAX(ID_cambio) FROM TB_CAMBIOS_SESION")
        last_id = self.cursor.fetchone()[0]
        if last_id:
            new_id = str(int(last_id) + 1).zfill(12)
        else:
            new_id = '1'.zfill(12)

        try:
            query = '''INSERT INTO TB_CAMBIOS_SESION (ID_cambio, ID_sesion, ID_producto, Cantidad_cambiada)
                    VALUES (?, ?, ?, ?)'''
            self.cursor.execute(query, new_id, session_id, product_id, cantidad_cambiada)
            self.conn.commit()
            return True
        except pyodbc.Error as e:
            print(f"Error al insertar cambio en la base de datos: {e}")
            return False

    def close_connection(self):
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()
            print("Conexión terminada")
            self.conn = None
            
    def __del__(self):
        self.close_connection()
