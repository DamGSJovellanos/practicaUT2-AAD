from bd_conn import ejecutar_query

# CRUD ENEMIGOS

def crear_enemigo(nombre, descripcion, nivel=1, id_ubicacion=None, drop_objetos=False):
    """Crea un nuevo enemigo en la base de datos"""
    query = """
    INSERT INTO enemigos (nombre, descripcion, nivel, id_ubicacion, drop_objetos)
    VALUES (?, ?, ?, ?, ?)
    """
    return ejecutar_query(query, [nombre, descripcion, nivel, id_ubicacion, drop_objetos])


def obtener_enemigos():
    """Obtiene todos los enemigos de la base de datos"""
    query = "SELECT * FROM enemigos"
    return ejecutar_query(query, fetch=True)


def obtener_enemigo_por_id(id_enemigo):
    """Obtiene un enemigo especifico por su ID"""
    query = "SELECT * FROM enemigos WHERE id_enemigo=?"
    return ejecutar_query(query, [id_enemigo], fetch=True)


def actualizar_enemigo(id_enemigo, nombre=None, descripcion=None, nivel=None, drop_objetos=None):
    """Actualiza los campos de un enemigo existente"""
    updates = []
    params = []
    
    if nombre:
        updates.append("nombre=?")
        params.append(nombre)
    if descripcion:
        updates.append("descripcion=?")
        params.append(descripcion)
    if nivel is not None:
        updates.append("nivel=?")
        params.append(nivel)
    if drop_objetos is not None:
        updates.append("drop_objetos=?")
        params.append(drop_objetos)
    
    if not updates:
        print("No hay campos para actualizar")
        return None
    
    params.append(id_enemigo)
    query = f"UPDATE enemigos SET {', '.join(updates)} WHERE id_enemigo=?"
    return ejecutar_query(query, params)


def eliminar_enemigo(id_enemigo):
    """Elimina un enemigo de la base de datos"""
    query = "DELETE FROM enemigos WHERE id_enemigo=?"
    return ejecutar_query(query, [id_enemigo])

