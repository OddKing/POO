class Pelicula:
    #constructor de la clase, que crea instancia.
    def __init__(self,titulo,categoria,año):
        self.titulo=titulo
        self.categoria=categoria
        self.a=año
        print('Se ha creado la pelicula ',titulo,self.a)
    
    def __str__(self):
        return '{}  ({}) '.format(self.titulo,self.a)


class Catalogo:
    peliculas=[]
    def __init__(self,peliculas=[]):
        self.peliculas=peliculas
    
    def agregar(self,p):
        self.peliculas.append(p)
    
    def mostrar(self):
        print(p)


p= Pelicula('->El Exorcista','Terror',1973)

c= Catalogo([p])

c.mostrar()