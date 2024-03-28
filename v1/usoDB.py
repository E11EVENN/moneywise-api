import psycopg2

class Database:
    def __init__(self, hostname, username, password, database):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.hostname,
                user=self.username,
                password=self.password,
                dbname=self.database
            )
            print("Conexión exitosa a la base de datos PostgreSQL")
        except Exception as e:
            print(f"No se pudo conectar a la base de datos: {e}")

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()
            print("Conexión cerrada exitosamente")

    def execute_query(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")

# Configuración de la conexión a la base de datos PostgreSQL
db_config = {
    'hostname': 'localhost',
    'username': 'postgres',
    'password': '1234567890',
    'database': 'postgres'
}

# Crear una instancia de la clase Database
db = Database(**db_config)

# Conectar a la base de datos
db.connect()

# Ejemplo de uso: ejecutar una consulta SQL
query = "SELECT * FROM pais"
results = db.execute_query(query)
for row in results:
    print(row)

# No olvides cerrar la conexión cuando hayas terminado
db.disconnect()