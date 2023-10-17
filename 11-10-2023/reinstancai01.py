class Pelicula:
    #constructor de la clase, que crea instancia.
    def __init__(self,titulo,categoria,año):
        self.titulo=titulo
        self.categoria=categoria
        self.a=año
        print('Se ha creado la pelicula ',titulo,self.a)

    #destructor de la clase, borrar la instancia :(
    def __del__(self):
        print('se destrue la pelicula ',self.titulo)
    
    def __str__(self):
        return "{} lanzada en {} categoria {} ".format(self.titulo,self.a,self.categoria)


p= Pelicula('Ready player one', 2018,'Ciencia Ficcion')
print(p)
