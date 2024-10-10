class Prestamo:
    def __init__(self, fecha_entrega, isbn, usuario, fecha_prestamo, estado):
        self.fecha_entrega = fecha_entrega
        self.isbn = isbn 
        self.usuario = usuario
        self.fecha_pretamo = fecha_prestamo
        self.estado = estado
        
    def crear_prestamo(self):
        print(f"""
            Detalles Prestamo
            Fecha de entrega: {self.fecha_entrega}
            Identificador: {self.isbn}
            Usuario: {self.usuario}
            Fecha de prestamo: {self.fecha_pretamo}
            Estado: {self.estado}
""")
obj_crear_prestamo = Prestamo("9 de julio","-","Constanza","9 de junio","Activo")
obj_crear_prestamo.crear_prestamo()
        
