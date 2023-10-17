class Clasecualqueira:
    counter=0

    def __init__(self,var=1):
        self.__primero= var
        Clasecualqueira.counter+=1


objeto_cualquiera_1=Clasecualqueira()
objeto_cualquiera_2=Clasecualqueira(1)
objeto_cualquiera_3=Clasecualqueira(4)

print(objeto_cualquiera_1.__dict__,objeto_cualquiera_1.counter)
print(objeto_cualquiera_2.__dict__,objeto_cualquiera_2.counter)
print(objeto_cualquiera_3.__dict__,objeto_cualquiera_3.counter)
