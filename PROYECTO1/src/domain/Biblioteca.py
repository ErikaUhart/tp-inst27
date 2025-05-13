class Biblioteca:
    def _init_(self):
    self.libro=[]
    self.usuario={}
 
    def registrar_usuario(self, usuario):
        if usuario.user_id in self.usuario:
            print("usuario ya registrado.")
        else:
            self.usuario[usuario.user_id]=usuario
            print (f"{self.usuario}registrado con exito")

            def agregar_libro(self, libro):
                self.libro.append(libro)
                print(f"libro {self.titulo} ha sido agregado al sistema")

            def buscar_libro(self, clave):
                resultado=[libro for libro in self.libro
                           if clave.lower()in libro.titulo.lower()
                           or clave.lower() in libro.autor.lower()]
                if resultado:
                    for libro in resultado:
                        print(libro)
                    else:
                        print("no se ha encontrado libro")