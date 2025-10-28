from bd_conn import ejecutar_query

# CRUD UBICACIONES

def crear_ubicacion(nombre, descripcion, tipo=None):
    query = "INSERT INTO ubicaciones (nombre, descripcion, tipo) VALUES (?, ?, ?)"
    return ejecutar_query(query, [nombre, descripcion, tipo])

def obtener_ubicaciones():
    query = "SELECT * FROM ubicaciones"
    return ejecutar_query(query, [], True)

def actualizar_ubicacion(id_ubicacion, nombre=None, descripcion=None, tipo=None):
    updates = []
    params = []
    if nombre:
        updates.append("nombre=?")
        params.append(nombre)
    if descripcion:
        updates.append("descripcion=?")
        params.append(descripcion)
    if tipo:
        updates.append("tipo=?")
        params.append(tipo)
    params.append(id_ubicacion)
    query = f"UPDATE ubicaciones SET {', '.join(updates)} WHERE id_ubicacion=?"
    return ejecutar_query(query, params)

def eliminar_ubicacion(id_ubicacion):
    query = "DELETE FROM ubicaciones WHERE id_ubicacion=?"
    return ejecutar_query(query, [id_ubicacion])
