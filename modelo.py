import sqlite3 


class Contacto:

    def __init__(self, nombre, apellido, telefono, email, id = None):
        self.nombre = nombre
        self.apellido = apellido 
        self.telefono = telefono
        self.email = email
        self.id = id
    
    

class AdministradorDB:
    def __init__(self, agenda_db):
        # 1. Conectamos a la base de datos (se crea si no existe)
        self.conn = sqlite3.connect(agenda_db)
        self.cursor = self.conn.cursor()
        # 2. Creamos la tabla
        self.crear_tabla_contactos()

    def crear_tabla_contactos(self):
        """Crea la tabla Contactos si no existe."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Contactos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                telefono TEXT,
                email TEXT UNIQUE NOT NULL
            );
        """)
        self.conn.commit()
        print("Tabla 'Contactos' lista.")

    def cerrar_conexion(self):
        """Cierra la conexión con la base de datos."""
        self.conn.close()

    def agregar_contacto(self, nombre, apellido, telefono, email):
        # La sentencia SQL base
        sql_query = "INSERT INTO Contactos (nombre, apellido, telefono, email) VALUES (?, ?, ?, ?)"
        
        
        
        self.cursor.execute(sql_query, (nombre, apellido, telefono, email))
        
        
        self.conn.commit()
        print("Contacto agregado.")

        # Dentro de la clase AdministradorDB:

    def consultar_contactos(self):
        """Consulta y devuelve todos los contactos de la base de datos"""
        self.cursor.execute("SELECT id, nombre, apellido, telefono, email FROM Contactos")
        
        filas = self.cursor.fetchall() # fetchall() obtiene todas las filas del resultado
        
        lista_contactos = []
        for fila in filas:
            # Creamos un objeto Contacto por cada fila y lo agregamos a la lista
            contacto = Contacto(nombre=fila[1], apellido=fila[2], telefono=fila[3], email=fila[4], id=fila[0])
            lista_contactos.append(contacto)
            
        return lista_contactos
    

    def eliminar_contacto(self, id_contacto):
        """Elimina un contacto de la base de datos usando su id."""
        # El id va en una tupla, aunque sea un solo valor
        self.cursor.execute("DELETE FROM Contactos WHERE id = ?", (id_contacto,))
        self.conn.commit()
        print("Contacto eliminado.")


    def modificar_contacto(self, id_contacto, nombre, apellido, telefono, email):
        """Actualiza los datos de un contacto existente usando su id."""
        
        sql_query = """
            UPDATE Contactos
            SET nombre = ?, apellido = ?, telefono = ?, email = ?
            WHERE id = ?
        """
        
        # El orden de los datos en la tupla DEBE coincidir con el orden de los '?'
        datos = (nombre, apellido, telefono, email, id_contacto)
        
        self.cursor.execute(sql_query, datos)
        self.conn.commit()
        print("Contacto modificado.")

    # Dentro de la clase AdministradorDB en modelo.py

    def existe_contacto(self, nombre, apellido):
        """
        Verifica si ya existe un contacto con el mismo nombre y apellido,
        ignorando mayúsculas y minúsculas.
        """
        # Convertimos los datos de entrada a minúsculas antes de la consulta
        nombre_lower = nombre.lower()
        apellido_lower = apellido.lower()
        
        # Usamos la función LOWER() de SQL para comparar todo en minúsculas
        self.cursor.execute("SELECT 1 FROM Contactos WHERE LOWER(nombre) = ? AND LOWER(apellido) = ?", (nombre_lower, apellido_lower))
        
        return self.cursor.fetchone() is not None
        
        






