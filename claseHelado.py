

class Helado:
    def __init__(self, in1, in2, listaSabores):
        self.__gramos = in1
        self.__precio = in2
        self.__sabores = listaSabores
       
    def getGramos(self):
        return self.__gramos
    
    def getPrecio (self):
        return self.__precio
    def getListaSab(self):
        return self.__sabores
    
    
    