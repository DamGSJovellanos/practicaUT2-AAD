import envyte
import libsql

db_url = envyte.get("DB_URL")
api_token = envyte.get("API_TOKEN")

conn = libsql.connect("juego", sync_url=db_url, auth_token=api_token)

cursor = conn.cursor()
# Crear la tabla personaje si no existe
# en este apartado crear todas las tablas necesarias para el juego
""" cursor.execute('''
               CREATE TABLE IF NOT EXISTS personaje (
               id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                clase TEXT NOT NULL
               )'''
               ) """
conn.close()