class Usuario:
    def __init__(self,nombre,nro_identificacion,correo,nro_telefono,estado):
        self.nombre = nombre 
        self.nro_identificaciom = nro_identificacion 
        self.correo = correo
        self.nro_telefono = nro_telefono 
        self.estado = estado 

    def datos_contacto(self):
        print(f"""
            los datos de contacto son:
                {self.correo}
                {self.nro_telefono}
            """)
    def estado_usuario(self):
        print(f"""
                el estado del usuario son {self.nombre} es {self.estado}
            """)
    def datos_personales(self):
        print(f"""
            Nombre: {self.nombre}
            ID_identificación: {self.nro_identificaciom}

                    """)
        
obj_usuario = Usuario("Constamza","111-1","coni@gmail.com",41525,"Activo")
obj_usuario.datos_personales() 
obj_usuario.estado_usuario()
obj_usuario.datos_personales()
        