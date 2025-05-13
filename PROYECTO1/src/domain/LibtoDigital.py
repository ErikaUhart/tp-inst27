class LibroDigital(Libro):
    def _init(self, nombre, autor, isbn, mb_tamaño):
        super()._init_(titulo, autor, isbn) self.mb_tamaño=mb_tamaño

        def Descargar(self):
            return f"Descargando '{self.titulo} ({self.mb_tamaño})MB..."