# Importacion de los cruds
from crud_objetos import crear_objeto, obtener_objetos, actualizar_objeto, eliminar_objeto
from crud_enemigos import crear_enemigo, obtener_enemigos, actualizar_enemigo, eliminar_enemigo
from crud_personajes import crear_personaje, obtener_personajes, actualizar_personaje, eliminar_personaje
from crud_ubicaciones import crear_ubicacion, obtener_ubicaciones, actualizar_ubicacion, eliminar_ubicacion
# Importamos las consultas "dificiles"
from consultas_complejas_1 import objetos_por_rareza, enemigos_por_nivel, objetos_dropeados_por_enemigo
# El primero es para la ingesta inicial de datos y el segundo para cerrar la conexion
from insercion_inicial import ingesta_inicial
from bd_conn import cerrar_conexion

def menu():
    ingesta_inicial()
    
    
    opcion = ""
    while opcion != "0":
        print(" MENU PRINCIPAL ")
        print("1. Listar objetos")
        print("2. Crear objeto")
        print("3. Actualizar objeto")
        print("4. Eliminar objeto")
        print("5. Listar enemigos")
        print("6. Crear enemigo")
        print("7. Actualizar enemigo")
        print("8. Eliminar enemigo")
        print("9. Listar personajes")
        print("10. Crear personaje")
        print("11. Actualizar personaje")
        print("12. Eliminar personaje")
        print("13. Listar ubicaciones")
        print("14. Crear ubicacion")
        print("15. Actualizar ubicacion")
        print("16. Eliminar ubicacion")
        print("17. Consultas avanzadas 1")
        print("18. Consultas avanzadas 2")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            print("Lista de objetos")
            for e in obtener_objetos(): 
                print(e)
        elif opcion == "2":
            nombre = input("Nombre: ")
            descripcion = input("Descripcion: ")
            rareza = input("Rareza: ")
            crear_objeto(nombre, descripcion, rareza)
        elif opcion == "3":
            id_obj = int(input("ID del objeto: "))
            nombre = input("Nuevo nombre (enter para omitir): ") 
            descripcion = input("Nueva descripcion (enter para omitir): ") 
            rareza = input("Nueva rareza (enter para omitir): ") 
            actualizar_objeto(id_obj, nombre, descripcion, rareza)
        elif opcion == "4":
            id_obj = int(input("ID del objeto: "))
            eliminar_objeto(id_obj)
        elif opcion == "5":
            print("Lista de enemigos")
            for e in obtener_enemigos(): 
                print(e)
        elif opcion == "6":
            nombre = input("Nombre: ")
            descripcion = input("Descripcion: ")
            nivel = int(input("Nivel: "))
            crear_enemigo(nombre, descripcion, nivel)
        elif opcion == "7":
            id_enem = int(input("ID del enemigo: "))
            nombre = input("Nuevo nombre (enter para omitir): ") 
            descripcion = input("Nueva descripcion (enter para omitir): ") 
            nivel = input("Nuevo nivel (enter para omitir): ")
            nivel = int(nivel) if nivel else None
            actualizar_enemigo(id_enem, nombre, descripcion, nivel)
        elif opcion == "8":
            id_enem = int(input("ID del enemigo: "))
            eliminar_enemigo(id_enem)
        elif opcion == "9":
            print("Lista de personajes")
            for e in obtener_personajes(): 
                print(e)
        elif opcion == "10":
            nombre = input("Nombre: ")
            descripcion = input("Descripcion: ")
            id_ubicacion = input("ID Ubicacion (enter para omitir): ")
            id_ubicacion = int(id_ubicacion) if id_ubicacion else None
            da_objeto = input("¿Da objeto? (si/no): ").lower() == "si"
            rol = input("Rol (enter para omitir): ") 
            crear_personaje(nombre, descripcion, id_ubicacion, da_objeto, rol)
        elif opcion == "11":
            id_personaje = int(input("ID del personaje: "))
            nombre = input("Nuevo nombre (enter para omitir): ") 
            descripcion = input("Nueva descripcion (enter para omitir): ") 
            id_ubicacion = input("Nueva ID Ubicacion (enter para omitir): ")
            id_ubicacion = int(id_ubicacion) if id_ubicacion else None
            da_objeto_input = input("¿Da objeto? (si/no/enter para omitir): ").lower()
            da_objeto = True if da_objeto_input == "si" else False if da_objeto_input == "no" else None
            rol = input("Nuevo rol (enter para omitir): ") 
            actualizar_personaje(id_personaje, nombre, descripcion, id_ubicacion, da_objeto, rol)
        elif opcion == "12":
            id_personaje = int(input("ID del personaje: "))
            eliminar_personaje(id_personaje)
        elif opcion == "13":
            print ("Obtener ubicaciones")
            for e in obtener_ubicaciones(): 
                print(e)
        elif opcion == "14":
            nombre = input("Nombre: ")
            descripcion = input("Descripcion: ")
            tipo = input("Tipo (enter para omitir): ") 
            crear_ubicacion(nombre, descripcion, tipo)
        elif opcion == "15":
            id_ubicacion = int(input("ID de la ubicacion: "))
            nombre = input("Nuevo nombre (enter para omitir): ") 
            descripcion = input("Nueva descripcion (enter para omitir): ") 
            tipo = input("Nuevo tipo (enter para omitir): ") 
            actualizar_ubicacion(id_ubicacion, nombre, descripcion, tipo)
        elif opcion == "16":
            id_ubicacion = int(input("ID de la ubicacion: "))
            eliminar_ubicacion(id_ubicacion)
        elif opcion == "17":
            print("Para filtrar los objetos por rareza escribe un nivel de rareza")
            rareza = input("Filtrar objetos por rareza: ")
            for objeto in objetos_por_rareza(rareza):
                print(objeto)
            
            print("Ahora escribe el nivel minimo y maximo de los enemigos que quieres ver")
            min_n = int(input("Nivel minimo enemigo: "))
            max_n = int(input("Nivel maximo enemigo: "))
            for enemigo in enemigos_por_nivel(min_n, max_n):
                print(enemigo)
            
            print("Ahora escribe el id de un enemigo para saber que dropea")
            id = input("Dropeados por: ")
            for objeto in objetos_dropeados_por_enemigo(id):
                print(objeto)
        elif opcion == "18":
            
            print("Personajes por ubicacion:")
            for resultado in contar_personajes_por_ubicacion():
                print(resultado)
            
            print("Objetos por personaje:")
            for resultado in contar_objetos_por_personaje():
                print(resultado)
            
            print("Personajes que dan objetos:")
            for personaje in personajes_que_dan_objetos():
                print(personaje)
            
            print("Top 5 ubicaciones con mas personajes:")
            for ubicacion in ubicaciones_con_mas_personajes():
                print(ubicacion)
        elif opcion == "0":
            print("Saliendo...")
        else:
            print("Opcion no valida")
    cerrar_conexion()

if __name__ == "__main__":
    try:
        menu()
    except:
        print("Error durante la ejecucion")
    finally:
        cerrar_conexion()