from biblioteca import Biblioteca
from detalle_libro import DetalleLibro
from editorial import Editorial
from libro import Libro
from pretamo import Prestamo
from usuario import Usuario


def menu():
    opc = int(input("""
                    Ingrese una opción:
                    1. Biblioteca
                    2. Detalle libro
                    3. Editorial
                    4. Libro
                    5. Prestamo
                    6. Usuario
                    Opcion: """))
    
    if opc==1:
        obj_biblioteca = Biblioteca("Biblioteca","Luis Durand",111111)
        opc_menu = int(input("""
                Ingrese una opción
                  1. Listar biblioteca
                 Opcion: """))
        if opc_menu ==1:
            obj_biblioteca.traer_biblioteca()

    elif opc==2:
        obj_detalle_libro = DetalleLibro("Aventura", 500, "Gatito")
        opc_menu = int(input("""
                Ingrese una opción
                1. Detalles del libro
                Opción: """))

    elif opc==3:
        obj_editorial = Editorial("2222","Cactus",156535)
        opc_menu = int(input("""
                Ingrese una opción
                1. Informacion de editorial
                """))
        if opc_menu ==1:
            obj_editorial.mostrar_editorial()
    elif opc==4:
        obj_mostrarlibro = Libro(5555,"Miau","Conito","500","Aventura",500,"nose")
        opc_menu = int(input("""
                Ingrese una opción
                1. Mostrar detalles del libro
                """))
        if opc_menu ==1:
            obj_mostrarlibro.mostrar_libro()
    elif opc==5:
        obj_crear_prestamo = Prestamo("9 de julio","-","Constanza","9 de junio","Activo")
        opc_menu = int(input("""
                Ingrese una opción
                1. Mostrar prestamos
                """))
        if opc_menu ==1:
            obj_crear_prestamo.crear_prestamo()
    elif opc==6:
        obj_usuario = Usuario("Constamza","111-1","coni@gmail.com",41525,"Activo")
        opc_menu = int(input("""
                Ingrese una opción
                1. Mostrar datos de contacto
                2. Mostrar estado de usuario
                3. Mostrar datos personales
                """))
        if opc_menu ==1:
            obj_usuario.datos_personales() 
        if opc_menu ==2:
            obj_usuario.estado_usuario()
        if opc_menu ==3:
            obj_usuario.datos_personales()


menu()