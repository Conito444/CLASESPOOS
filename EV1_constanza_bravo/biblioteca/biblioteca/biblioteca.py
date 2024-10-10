class Biblioteca:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    
    def traer_biblioteca(self):
        print(f"""
                Información Biblioteca: {self.nombre} {self.direccion} {self.telefono}
                """)
#obj_biblioteca = Biblioteca("Biblioteca","Luis Durand",111111)
#obj_biblioteca.traer_biblioteca()