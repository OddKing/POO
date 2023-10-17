class Animal:
    nombre=None
    peso=None

    def __init__(self,nombre,peso):
        self.nombre=nombre
        self.peso=peso
    
    def hace_algo(self):
        return 'se comio toda la comida'
    def __del__(self):
        print('Se elimina a',format(self.nombre))

perro= Animal('chocolo',15)
gato= Animal('hades',30)