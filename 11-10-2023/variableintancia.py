class Cualquierclase:
    def __init__(self,var=1):
        self.__primero= var
    
    def set_segundo(self,var=2):
        self.__segundo=var
    


cualquier_objeto_1=Cualquierclase()
cualquier_objeto_2=Cualquierclase(2)
cualquier_objeto_2.set_segundo(3)

cualquier_objeto_3=Cualquierclase(4)
cualquier_objeto_3.__tercero =5

print(cualquier_objeto_1.__dict__)
print(cualquier_objeto_2.__dict__)
print(cualquier_objeto_3.__dict__)
