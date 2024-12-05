# The class `Libro` defines a book object with attributes for title and ISBN, and includes methods for
# string representation and equality comparison.
## ejr,1
"""class Libro:
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
    def __str__(self):
        return f"Titulo: {self.titulo},{sel.isbn}"
    
    def __eq__(self,other):
        return self.titulo==other.titulo and self.isbn==other.isbn
libro1=Libro("harry potter","1234")
libro2=Libro("harry potter","1234")
print(libro1==libro2) """

### Herencia
#ejer.1

class Guitar:
    def __init__(self, marca, cuerdas=6):
        self.marca = marca
        self.cuerdas = cuerdas
    
    def tocar(self):
        print("vrmmm,vrmmm,vrmmm")
        
class Electrica(Guitar):
    def __init__(self, marca, cuerdas=6,color="negro"):
        super().__init__(marca, cuerdas)
        self.color=color
    
class bajo(Guitar):
    def __init__(self, marca, cuerdas=4,color="rojo"):
        super().__init__(marca, cuerdas)
        self.color=color
    def tocar (self):
        print("bajooooooo")
        
class Band:
    def __init__(self,instrumentos):
        self.instrumentos=instrumentos
    def tocar(self):
        for i in self.instrumentos:
            i.tocar()
    
instrumento1=[Electrica("Fender"),Electrica("Gibson",6,"negro"),bajo("Fender",4,"rojo")]
b=Band(instrumento1)
b.tocar()