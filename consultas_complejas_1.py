from crud_objetos import obtener_objetos
from crud_enemigos import obtener_enemigos
from bd_conn import ejecutar_query



# Consultas complejas, una ordena por rareza , la otra en un rango de niveles y la ultima los objetos de un enemigo

def objetos_por_rareza(rareza):
    query = "SELECT * FROM objetos WHERE rareza=? ORDER BY nombre"
    return ejecutar_query(query, [rareza], True)

def enemigos_por_nivel(min_nivel, max_nivel):
    query = "SELECT * FROM enemigos WHERE nivel BETWEEN ? AND ? ORDER BY nivel DESC"
    return  ejecutar_query(query, [min_nivel,max_nivel], True)

def objetos_dropeados_por_enemigo(id_enemigo):
    query = """
    SELECT o.id_objeto, o.nombre, eo.probabilidad
    FROM objetos o
    JOIN enemigo_objeto eo ON o.id_objeto = eo.id_objeto
    WHERE eo.id_enemigo=?
    """
    return ejecutar_query(query, [id_enemigo], True)
