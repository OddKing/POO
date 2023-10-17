class Cualquierclase2:
    primero=0
    segundo=0
    respuesta=0

    def __init__(self,p,s):
        self.primero=p
        self.segundo=s

    def suma(self):
        print("primer numero = "+ str(self.primero))
        print("Segundo numero = "+str(self.segundo))
        print("Suma de los 2 numeros = "+str(self.respuesta))

    def calcular(self):
        self.respuesta=self.primero+self.segundo

obj = Cualquierclase2(1000,2000)
obj.calcular()
obj.suma()