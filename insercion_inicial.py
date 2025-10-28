from bd_conn import ejecutar_query, cerrar_conexion

# El borrado antes de la creacion de las tablas
def borrar_tablas():
    tablas = ["enemigo_objeto", "personaje_objeto", "objetos", "enemigos", "personajes", "ubicaciones"]
    for tabla in tablas:
        query = f"DROP TABLE IF EXISTS {tabla}"
        ejecutar_query(query)
    print("Tablas borradas correctamente.")

# Se crean las tablas
def crear_tablas():
    # Ubicaciones
    query_ubicaciones = """
    CREATE TABLE IF NOT EXISTS ubicaciones (
        id_ubicacion INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        tipo TEXT
    )
    """
    ejecutar_query(query_ubicaciones)

    # Personajes
    query_personajes = """
    CREATE TABLE IF NOT EXISTS personajes (
        id_personaje INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        id_ubicacion INTEGER REFERENCES ubicaciones(id_ubicacion),
        da_objeto BOOLEAN NOT NULL DEFAULT 0,
        rol TEXT
    )
    """
    ejecutar_query(query_personajes)

    # Enemigos
    query_enemigos = """
    CREATE TABLE IF NOT EXISTS enemigos (
        id_enemigo INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        nivel INTEGER DEFAULT 1,
        id_ubicacion INTEGER REFERENCES ubicaciones(id_ubicacion),
        drop_objetos BOOLEAN NOT NULL DEFAULT 0
    )
    """
    ejecutar_query(query_enemigos)

    # Objetos
    query_objetos = """
    CREATE TABLE IF NOT EXISTS objetos (
        id_objeto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        rareza TEXT DEFAULT 'comun',
        id_ubicacion INTEGER REFERENCES ubicaciones(id_ubicacion),
        id_personaje_dropea INTEGER REFERENCES personajes(id_personaje),
        id_enemigo_dropea INTEGER REFERENCES enemigos(id_enemigo)
    )
    """
    ejecutar_query(query_objetos)

    # Relacion personaje_objeto
    query_personaje_objeto = """
    CREATE TABLE IF NOT EXISTS personaje_objeto (
        id_personaje INTEGER REFERENCES personajes(id_personaje),
        id_objeto INTEGER REFERENCES objetos(id_objeto),
        cantidad INTEGER DEFAULT 1,
        PRIMARY KEY (id_personaje, id_objeto)
    )
    """
    ejecutar_query(query_personaje_objeto)

    # Relacion enemigo_objeto
    query_enemigo_objeto = """
    CREATE TABLE IF NOT EXISTS enemigo_objeto (
        id_enemigo INTEGER REFERENCES enemigos(id_enemigo),
        id_objeto INTEGER REFERENCES objetos(id_objeto),
        probabilidad FLOAT DEFAULT 1.0,
        PRIMARY KEY (id_enemigo, id_objeto)
    )
    """
    ejecutar_query(query_enemigo_objeto)

    print("Tablas creadas correctamente.")

# Inserciones a la base de datos
def insertar_ubicaciones():
    ubicaciones = [
        ("Ciudadela", "Ciudad principal del reino", "ciudad"),
        ("Bosque Oscuro", "Bosque tenebroso con enemigos", "mundo"),
        ("Mazmorra Abisal", "Mazmorra subterranea con jefes", "mazmorra")
    ]
    for nombre, descripcion, tipo in ubicaciones:
        query = "INSERT INTO ubicaciones (nombre, descripcion, tipo) VALUES (?, ?, ?)"
        ejecutar_query(query, [nombre, descripcion, tipo])

def insertar_personajes():
    personajes = [
        ("Aria", "Mercader amigable", 1, True, "mercader"),
        ("Borin", "NPC guia", 2, False, "NPC"),
        ("Ciri", "Comerciante de rarezas", 1, True, "mercader")
    ]
    for nombre, descripcion, id_ubicacion, da_objeto, rol in personajes:
        query = """
        INSERT INTO personajes (nombre, descripcion, id_ubicacion, da_objeto, rol)
        VALUES (?, ?, ?, ?, ?)
        """
        ejecutar_query(query, [nombre, descripcion, id_ubicacion, da_objeto, rol])

def insertar_enemigos():
    enemigos = [
        ("Goblin", "Enemigo debil", 1, 2, True),
        ("Troll", "Enemigo fuerte", 5, 3, True),
        ("Esqueleto", "Enemigo del bosque", 2, 2, False)
    ]
    for nombre, descripcion, nivel, id_ubicacion, drop_objetos in enemigos:
        query = """
        INSERT INTO enemigos (nombre, descripcion, nivel, id_ubicacion, drop_objetos)
        VALUES (?, ?, ?, ?, ?)
        """
        ejecutar_query(query, [nombre, descripcion, nivel, id_ubicacion, drop_objetos])

def insertar_objetos():
    objetos = [
        ("Espada de Madera", "Espada basica", "comun", 2, None, 1),
        ("Amuleto Raro", "Amuleto con poderes", "raro", None, 3, 2),
        ("Pocion de Vida", "Recupera salud", "comun", 1, 1, None)
    ]
    for nombre, descripcion, rareza, id_ubicacion, id_personaje_dropea, id_enemigo_dropea in objetos:
        query = """
        INSERT INTO objetos (nombre, descripcion, rareza, id_ubicacion, id_personaje_dropea, id_enemigo_dropea)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        ejecutar_query(query, [nombre, descripcion, rareza, id_ubicacion, id_personaje_dropea, id_enemigo_dropea])

# La funcion principal
def ingesta_inicial():
    borrar_tablas()
    crear_tablas()
    insertar_ubicaciones()
    insertar_personajes()
    insertar_enemigos()
    insertar_objetos()
    print("Ingesta inicial completada correctamente.")
    

if __name__ == "__main__":
    ingesta_inicial()

