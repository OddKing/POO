class Galleta():
    chocolate=False

    def __init__(self,sabor=None ,forma= None):
        self.sabor= sabor
        self.forma= forma
        if sabor is not None and forma is not None:
            print('Se acaba de crear una galleta {} y {}'.format(sabor,forma))

    def chocolatear(self):
        self.chocolate=True
    
    def tiene_chocolate(self):
        if(self.chocolate):
            print('Soy una galleta con chocolate :)')
        else:
            print('Soy una galleta sin chocolate :( ')

g=Galleta('Dulce','Redonda')
g=Galleta(input('Ingrese Sabor: '),input('Ingrese forma: '))
g=Galleta()

