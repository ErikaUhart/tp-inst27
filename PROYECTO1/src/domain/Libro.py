class Libro():
    def __init__(self, titulo, autor, isbn):
        self.titulo: titulo
        self.autor: autor
        self.isbn: isbn
        self.disponible: True

        def _str_(self):
            estado="Disponible" if self.disponible else "Prestado" return f"{self.titulo}-{self.autor}({estado})

    