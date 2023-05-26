from claseHelado import Helado
import csv

class manejador1:
    
    def __init__(self):
        self.__heladosVendidos = []
        
    def agregar(self, nuevo):
        self.__heladosVendidos.append(nuevo)
        
    def agregarHelado(self, mS):
        precio = float(input("Ingrese el precio del helado vendido: "))
        while precio != 0:
            gramos = int(input("Ingrese cantidad de gramos del helado (100, 150, 250, 500, 1000): "))
            listaSabores = []
            sabor = int(input("Ingrese el id del sabor deseado: "))
            while sabor != 0:
                listaSabores.append(mS.buscaSabor(sabor, gramos))
                sabor = int(input("Ingrese el id del sabor deseado, finalice con 0: "))
            nuevoHelado = Helado(gramos, precio, listaSabores)
            self.agregar(nuevoHelado)
            precio = float(input("Ingrese el precio del nuevo helado vendido, finaliza con 0: "))
    
        
            