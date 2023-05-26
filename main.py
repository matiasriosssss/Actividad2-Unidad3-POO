from mSabores import manejador2 as manSabores
from mHelados import manejador1 as manHelados


if __name__ == '__main__':
    mS = manSabores()
    mH = manHelados()
    mS.lecArchivo()
    o = 1
    while o != 0:
        print("""
    ----MENU----
    1_ Registrar helados
    2_ Mostrar el nombre de los sabores mas pedidos
    3_ Estimar la cantidad de gramos vendidos de un sabor
    4_ Mostrar los sabores mas vendidos en un tipo de helado
    5_ Importe total recaudado por cada tipo de helado
    0_FIN
          """)
        o=int(input("Ingrese opcion deseada: "))
       
        if o == 1:
            mH.agregarHelado(mS)
        elif o == 2:
            mS.mejoresSabores()
        elif o == 3:
            mS.gramosVendidos() 
        elif o==4 or o==5:
            print("No los hice debido a que era mucha perdida de tiempo...")
        elif o==0:
            print("FIN...")
        else:
            print("Opcion mal ingresada")

    