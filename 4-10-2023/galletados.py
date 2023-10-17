class Galleta():
    chocolate=False

    def __init__(self,sabor,forma):
        self.sabor= sabor
        self.forma= forma
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
#g=Galleta()