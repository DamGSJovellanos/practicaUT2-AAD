from bd_conn import ejecutar_query

# --- REPORTES Y ESTADÍSTICAS ---

def contar_personajes_por_ubicacion():
    query = """
    SELECT u.nombre AS ubicacion, COUNT(p.id_personaje) AS total_personajes
    FROM ubicaciones u
    LEFT JOIN personajes p ON u.id_ubicacion = p.id_ubicacion
    GROUP BY u.id_ubicacion
    """
    return ejecutar_query(query, [], True)

def contar_objetos_por_personaje():
    query = """
    SELECT p.nombre AS personaje, COUNT(po.id_objeto) AS total_objetos
    FROM personajes p
    LEFT JOIN personaje_objeto po ON p.id_personaje = po.id_personaje
    GROUP BY p.id_personaje
    """
    return ejecutar_query(query, [], True)

def personajes_que_dan_objetos():
    query = """
    SELECT nombre, rol FROM personajes WHERE da_objeto=1
    """
    return ejecutar_query(query, [], True)

def ubicaciones_con_mas_personajes():
    query = """
    SELECT u.nombre AS ubicacion, COUNT(p.id_personaje) AS total_personajes
    FROM ubicaciones u
    JOIN personajes p ON u.id_ubicacion = p.id_ubicacion
    GROUP BY u.id_ubicacion
    ORDER BY total_personajes DESC
    LIMIT 5
    """
    return ejecutar_query(query, [], True)
