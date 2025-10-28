import libsql
import envyte

# Conexion global
db_url = envyte.get("TURSO_URL")
api_token = envyte.get("TURSO_TOKEN")
conn = libsql.connect("juego", sync_url=db_url, auth_token=api_token)

def ejecutar_query(query, params=None, fetch=False):
   
    # Verificar que la conexion existe
    if conn is None:
        print("Error: No hay conexion a la base de datos")
        return None
    
    # Si no tiene parametros pone una lista vacia
    if params is None:
        params = []
    
    try:
        if params:
            result = conn.execute(query, params) 
        else:
            result = conn.execute(query)
        conn.commit()
        conn.sync()
        
        if fetch:
            return result.fetchall()
        return result
        
    except Exception as e:
        print(f"Error al ejecutar query: {e}")
        return None

def cerrar_conexion():
    global conn
    try:
        if conn:
            conn.close()
            conn = None
            print("Conexion cerrada correctamente.")
    except Exception as e:
        print(f"Error al cerrar la conexion: {e}")
