from claseSabor import Sabor
import csv

class manejador2:
    
    def __init__(self):
        self.__listaManejador2 = []
        
    def agregar(self, nuevo):
        self.__listaManejador2.append(nuevo)
    def getLista(self):
        return self.__listaManejador2
        
    def lecArchivo(self):
        archivo = open('sabores.csv')
        reader = csv.reader(archivo, delimiter=',')
        
        for fila in reader:
            nuevoObjeto = Sabor(fila[0], fila[1], fila[2])
            self.agregar(nuevoObjeto)
    def imprimirS(self):
        for i in range(len(self.getLista())):
            print(f"{self.__listaManejador2[i].__str__()}")
    def buscaSabor(self, id, gramos):
        i=0
        centinela = True
        sab = None
        while i < len(self.getLista()) and centinela:
            if self.getLista()[i].getIdSabor() == id:
                sab = self.getLista()[i] ##GUARDA EL OBJETO DEL SABOR PARA DESPUES RETORNARLO
                self.getLista()[i].setContador() ##SUMA EN EL CONTADOR CADA VEZ QUE SE VENDE UN SABOR
                self.getLista()[i].setGramosV(gramos) ##SUMA LOS GRAMOS CADA VEZ QUE SE VENDE UN SABOR
                print(f"{self.getLista()[i].getSabor()} agregado") ##INDICA CUAL FUE EL SABOR AGREGADO
                centinela = False
            i+=1
        if centinela:
            print("No se encontro el sabor buscado ")
        else:
            return sab
    def mejoresSabores(self):
        lista = self.getLista()  ##copiamos la lista de sabores a una variable llamada lista para no modificar la original
        k=1
        cota= len(lista) - 1
        while k != -1:
            k=-1
            for i in range(len(lista)-1):
                if lista[i+1].getContador() > lista[i].getContador():
                    aux = lista[i+1]
                    lista[i+1]=lista[i]
                    lista[i]=aux
                    k=i
            cota=k
        print("Los 5 sabores mas pedidos son: ")
        for i in range(5):
            print(lista[i].getSabor())
            
    def gramosVendidos(self):
        id=int(input("Ingrese el id del sabor que quiere conocer la cantidad de gramos vendidos: "))
        i=0
        centinela=True
        while i < len(self.getLista()) and centinela:
            if id == self.getLista()[i].getIdSabor():
                print(f"La cantidad de gramos vendidos para {self.getLista()[i].getSabor()} es: {self.getLista()[i].getGramosV()}")
                centinela = False
            i+=1
            if centinela:
                print("No se encontro el id indicado.... ")
    
                
                    
        