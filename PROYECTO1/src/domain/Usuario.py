class Usuario():
    def __init__(self, nombre, user_id):
        self.nombre: nombre
        self.id: user_id
        self.libro_prestado: []

    def pedir_libro(self, libro):
        if len(self._libro_prestado)>=3:
            print(f"{self.nombre} ha sobrepasado el limite de libros prestados")
            if not libro.disponible:
                print(f" {self.titulo} no disponible")
                return libro.disponible = False
self.libros_prestados .append.(libro)
print (f"{self.nombre} ha llevado{self.titulo}")

def devolver_libro(self.libro):
    if libro in self._libros_prestados:

        sefl._libros_prestados.remove(libro)
        libro.disponible = True
        print(f"{self.nombre}ha sido devuelto '{self.titulo}'.")
    else:
        print(f"{self.titulo} no tiene ese libro prestado '{}")