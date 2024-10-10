class DetalleLibro:
    def __init__(self, categoria, n_paginas, editorial):
        self.categoria = categoria
        self.n_paginas = n_paginas
        self.editorial = editorial

    def traer_detalle_libro(self):
        print(f"""
            Detalle Libro
            Categoria: {self.categoria}
            Numero de paginas: {self.n_paginas}
            Editorial: {self.editorial}
                """)
obj_detalle_libro = DetalleLibro("Aventura", 500, "Gatito")
obj_detalle_libro.traer_detalle_libro()
      
      
    
        
        