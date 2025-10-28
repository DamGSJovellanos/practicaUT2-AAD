from bd_conn import ejecutar_query

# CRUD PERSONAJES

def crear_personaje(nombre, descripcion, id_ubicacion=None, da_objeto=False, rol=None):
    query = """
    INSERT INTO personajes (nombre, descripcion, id_ubicacion, da_objeto, rol)
    VALUES (?, ?, ?, ?, ?)
    """
    return ejecutar_query(query, [nombre, descripcion, id_ubicacion, da_objeto, rol])

def obtener_personajes():
    query = "SELECT * FROM personajes"
    return ejecutar_query(query,[],True)

def actualizar_personaje(id_personaje, nombre=None, descripcion=None, id_ubicacion=None, da_objeto=None, rol=None):
    updates = []
    params = []
    if nombre:
        updates.append("nombre=?")
        params.append(nombre)
    if descripcion:
        updates.append("descripcion=?")
        params.append(descripcion)
    if id_ubicacion is not None:
        updates.append("id_ubicacion=?")
        params.append(id_ubicacion)
    if da_objeto is not None:
        updates.append("da_objeto=?")
        params.append(da_objeto)
    if rol:
        updates.append("rol=?")
        params.append(rol)
    params.append(id_personaje)
    query = f"UPDATE personajes SET {', '.join(updates)} WHERE id_personaje=?"
    return ejecutar_query(query, params)

def eliminar_personaje(id_personaje):
    query = "DELETE FROM personajes WHERE id_personaje=?"
    return ejecutar_query(query, [id_personaje])
