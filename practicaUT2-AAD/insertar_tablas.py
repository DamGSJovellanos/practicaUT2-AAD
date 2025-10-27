import sqlite3
from pathlib import Path
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

RUTA_BD = os.getenv("LOCAL_DB", "juego.db")  # Ruta de la base de datos

schema_sql = Path("esquema.sql").read_text()  # Leer el esquema SQL

# Inserciones iniciales, separadas por tipo y propósito
insertar_ubicaciones = """
INSERT INTO ubicaciones(id_ubicacion, nombre, descripcion, tipo) VALUES
(1, 'Villa Alba', 'Pueblo tranquilo al norte', 'ciudad'),
(2, 'Caverna Sombría', 'Mazmorra con goblins', 'mazmorra'),
(3, 'Bosque Esmeralda', 'Bosque antiguo', 'mundo');
"""

insertar_personajes = """
INSERT INTO personajes(id_personaje, nombre, descripcion, id_ubicacion, da_objeto, rol) VALUES
(1, 'Marin', 'Mercader del pueblo', 1, 1, 'mercader'),
(2, 'Ayla', 'Cazadora errante', 3, 0, 'aliado'),
(3, 'Viejo Sabio', 'Guía de la historia', NULL, 0, 'NPC');
"""

insertar_enemigos = """
INSERT INTO enemigos(id_enemigo, nombre, descripcion, nivel, id_ubicacion, drop_objetos) VALUES
(1, 'Goblin', 'Pequeño enemigo', 2, 2, 1),
(2, 'Lobo', 'Depredador del bosque', 3, 3, 1),
(3, 'Bandido', 'Ladrón de caminos', 2, 1, 1);
"""

insertar_objetos = """
INSERT INTO objetos(id_objeto, nombre, descripcion, rareza, id_ubicacion) VALUES
(1, 'Poción pequeña', 'Recupera 20 HP', 'comun', 1),
(2, 'Espada de hierro', 'Ataque básico', 'comun', 2),
(3, 'Amuleto de fuego', 'Aumenta daño de fuego', 'raro', NULL),
(4, 'Poción mayor', 'Recupera 100 HP', 'raro', NULL),
(5, 'Pergamino antiguo', 'Contiene una misión', 'epico', 3);
"""

insertar_personaje_objeto = """
INSERT INTO personaje_objeto(id_personaje, id_objeto, cantidad) VALUES
(1,1,5),
(2,3,1);
"""

insertar_enemigo_objeto = """
INSERT INTO enemigo_objeto(id_enemigo, id_objeto, probabilidad) VALUES
(1,1,0.8),
(2,2,0.5);
"""

def main():
    # Conexión y ejecución de los comandos
    conexion = sqlite3.connect(RUTA_BD)
    try:
        cursor = conexion.cursor()
        # Crear las tablas según el esquema
        cursor.executescript(schema_sql)
        # Insertar ubicaciones
        cursor.executescript(insertar_ubicaciones)
        # Insertar personajes
        cursor.executescript(insertar_personajes)
        # Insertar enemigos
        cursor.executescript(insertar_enemigos)
        # Insertar objetos
        cursor.executescript(insertar_objetos)
        # Relación personaje-objeto
        cursor.executescript(insertar_personaje_objeto)
        # Relación enemigo-objeto
        cursor.executescript(insertar_enemigo_objeto)
        # Guardar cambios
        conexion.commit()
    finally:
        conexion.close()

if __name__ == "__main__":
    main()
