from bd_conn import ejecutar_query

# CRUD OBJETOS

def crear_objeto(nombre, descripcion, rareza="comun", id_ubicacion=None, id_personaje_dropea=None, id_enemigo_dropea=None):
    """Crea un nuevo objeto en la base de datos"""
    query = """
    INSERT INTO objetos (nombre, descripcion, rareza, id_ubicacion, id_personaje_dropea, id_enemigo_dropea)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    return ejecutar_query(query, [nombre, descripcion, rareza, id_ubicacion, id_personaje_dropea, id_enemigo_dropea])


def obtener_objetos():
    """Obtiene todos los objetos de la base de datos"""
    query = "SELECT * FROM objetos"
    return ejecutar_query(query, fetch=True)


def obtener_objeto_por_id(id_objeto):
    """Obtiene un objeto especifico por su ID"""
    query = "SELECT * FROM objetos WHERE id_objeto=?"
    return ejecutar_query(query, [id_objeto], fetch=True)


def actualizar_objeto(id_objeto, nombre=None, descripcion=None, rareza=None):
    """Actualiza los campos de un objeto existente"""
    updates = []
    params = []
    
    if nombre:
        updates.append("nombre=?")
        params.append(nombre)
    if descripcion:
        updates.append("descripcion=?")
        params.append(descripcion)
    if rareza:
        updates.append("rareza=?")
        params.append(rareza)
    
    if not updates:
        print("No hay campos para actualizar")
        return None
    
    params.append(id_objeto)
    query = f"UPDATE objetos SET {', '.join(updates)} WHERE id_objeto=?"
    return ejecutar_query(query, params)


def eliminar_objeto(id_objeto):
    """Elimina un objeto de la base de datos"""
    query = "DELETE FROM objetos WHERE id_objeto=?"
    return ejecutar_query(query, [id_objeto])

