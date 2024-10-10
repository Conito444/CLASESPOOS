class Libro:
    def __init__(self,isbd, titulo, autor, n_copias,categoria,n_paginas,editorial):
        self.isbn = isbd
        self.titulo = titulo
        self.autor = autor
        self.n_copias = n_copias
        self.categoria = categoria
        self.n_paginas = n_paginas
        self.editorial = editorial


    def mostrar_libro(self):
        print(f"""
            Detalles del libro
            Identificador: {self.isbn}
            Titulo: {self.titulo}
            Autor: {self.autor}
            Numero de copias: {self.n_copias}
            Categoria: {self.categoria}
            Numero de paginas: {self.n_paginas}
            Editorial: {self.editorial}
            """)
obj_mostrarlibro = Libro(5555,"Miau","Conito","500","Aventura",500,"nose")
obj_mostrarlibro.mostrar_libro()

        
    