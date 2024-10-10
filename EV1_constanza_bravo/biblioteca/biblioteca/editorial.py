class Editorial:
    def __init__(self,id, nombre, telefono) -> None:
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        
    def mostrar_editorial(self):
        print(f""" 
            Datos Editorial
            ID: {self.id}
            Nombre: {self.nombre}
            Telefono: {self.telefono}
                    """)
obj_editorial = Editorial("2222","Cactus",156535)
obj_editorial.mostrar_editorial()