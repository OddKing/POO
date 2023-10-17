class Galleta():
    chocolate=False

    def __init__(self):
        print('Se acaba de crear una galleta')

    def chocolatear(self):
        self.chocolate=True
    
    def tiene_chocolate(self):
        if(self.chocolate):
            print('Soy una galleta con chocolate :)')
        else:
            print('Soy una galleta sin chocolate :( ')

g=Galleta()

g.tiene_chocolate()
g.chocolatear()
g.tiene_chocolate()

print(Galleta.chocolate)