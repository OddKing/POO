class Galleta():
    chocolate=False

    def __init__(self,sabor=None,forma=None):
        self.sabor= sabor
        self.forma= forma
        if sabor is not None and forma is not None:
            print('Se acaba de crear una galleta {} y {}'.format(sabor,forma))

    def __del__(self):
        print('Se ha destruido la galleta ',self.sabor,self.forma)

g=Galleta('Dulce','Redonda')
g=Galleta(input('Ingrese Sabor: '),input('Ingrese forma: '))
g=Galleta()