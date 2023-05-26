

class Sabor:
    def __init__(self, in1, in2, in3):
        self.__idSabor = int(in1)
        self.__sabor = in2
        self.__ingredientes = in3
        self.__contador = 0
        self.__gramosVendidos = 0
        
    def __str__(self):
        return "Id: " + self.__idSabor + " - " + "Sabor: " + self.__sabor + " - " + "Ingredientes: " + self.__ingredientes
    def getIdSabor(self):
        return self.__idSabor
    
    def getSabor (self):
        return self.__sabor
    
    def getIngredientes(self):
        return self.__ingredientes
    def setContador(self):
        self.__contador += 1
    def getContador(self):
        return self.__contador
    def setGramosV(self, gramos):
        self.__gramosVendidos += (gramos / 4)
    def getGramosV(self):
        return self.__gramosVendidos