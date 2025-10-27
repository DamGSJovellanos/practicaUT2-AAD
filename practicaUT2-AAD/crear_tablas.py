# practicaUT2-AAD/crear_tablas.py
# Script para crear las tablas necesarias para un videojuego en una base de datos remota en Turso.
import envyte
import libsql

# Obtener credenciales desde variables de entorno seguras
db_url = envyte.get("DB_URL")
api_token = envyte.get("API_TOKEN")

# Conexión a la base de datos remota en Turso
conn = libsql.connect("juego", sync_url=db_url, auth_token=api_token)
cursor = conn.cursor()

def limpiar_tablas(cursor):
    # --- BORRAR TODAS LAS TABLAS EXISTENTES DE LA BASE DE DATOS ---
    cursor.execute("PRAGMA foreign_keys = OFF;")

    # Obtener los nombres de todas las tablas existentes
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablas = [t[0] for t in cursor.fetchall()]

    # Eliminar cada tabla encontrada
    for tabla in tablas:
        cursor.execute(f"DROP TABLE IF EXISTS {tabla};")
        print(f"Tabla eliminada: {tabla}")

    cursor.execute("PRAGMA foreign_keys = ON;")
    conn.commit()

    print("Todas las tablas existentes han sido eliminadas correctamente.")

def add_tablas(cursor):
    # Habilitar claves foráneas
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Tabla: ubicaciones
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ubicaciones (
        id_ubicacion INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        tipo TEXT
    )
    """)

    # Tabla: personajes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS personajes (
        id_personaje INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        id_ubicacion INTEGER,
        da_objeto INTEGER NOT NULL DEFAULT 0,
        rol TEXT,
        FOREIGN KEY (id_ubicacion) REFERENCES ubicaciones(id_ubicacion)
    )
    """)

    # Tabla: enemigos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS enemigos (
        id_enemigo INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        nivel INTEGER DEFAULT 1,
        id_ubicacion INTEGER NOT NULL,
        drop_objetos INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY (id_ubicacion) REFERENCES ubicaciones(id_ubicacion)
    )
    """)

    # Tabla: objetos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS objetos (
        id_objeto INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        rareza TEXT DEFAULT 'comun',
        id_ubicacion INTEGER,
        id_personaje_dropea INTEGER,
        id_enemigo_dropea INTEGER,
        FOREIGN KEY (id_ubicacion) REFERENCES ubicaciones(id_ubicacion),
        FOREIGN KEY (id_personaje_dropea) REFERENCES personajes(id_personaje),
        FOREIGN KEY (id_enemigo_dropea) REFERENCES enemigos(id_enemigo)
    )
    """)

    # Tabla: personaje_objeto
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS personaje_objeto (
        id_personaje INTEGER NOT NULL,
        id_objeto INTEGER NOT NULL,
        cantidad INTEGER DEFAULT 1,
        PRIMARY KEY (id_personaje, id_objeto),
        FOREIGN KEY (id_personaje) REFERENCES personajes(id_personaje),
        FOREIGN KEY (id_objeto) REFERENCES objetos(id_objeto)
    )
    """)

    # Tabla: enemigo_objeto
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS enemigo_objeto (
        id_enemigo INTEGER NOT NULL,
        id_objeto INTEGER NOT NULL,
        probabilidad FLOAT DEFAULT 1.0,
        PRIMARY KEY (id_enemigo, id_objeto),
        FOREIGN KEY (id_enemigo) REFERENCES enemigos(id_enemigo),
        FOREIGN KEY (id_objeto) REFERENCES objetos(id_objeto)
    )
    """)

    conn.commit()
    print("Tablas creadas correctamente en la base de datos 'juego' en Turso.")

# --- Flujo principal ---
if __name__ == "__main__":
    limpiar_tablas(cursor)
    add_tablas(cursor)
    conn.close()