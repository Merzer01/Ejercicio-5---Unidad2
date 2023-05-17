import csv
from classPlandeAhorro import planahorro

class manejador:
    __lista = []
    def __init__(self):
        self.__lista = []
    def readarchivo(self):
        with open("planes.csv") as archivo:
            lector = csv.reader(archivo, delimiter=';')

            for row in lector:
                cod = row[0]    #CODIGO DE PLAN
                mod = row[1]    #MODELO
                ver = row[2]    #VERSION
                val = row[3]    #VALOR DE VEHICULO
                c = row[4]      #CUOTAS
                #cl = row[5]     #CUOTAS A LICITAR
                p = planahorro(cod, mod, ver, val, c)
                self.__lista.append(p)
    
    def opcion1(self):
        print("---------->MODIFICAR VALOR DE VEHICULO<----------")
        for i in range(len(self.__lista)):
            print(self.__lista[i])
            nv = int(input("Ingrese nuevo valor del vehiculo: "))
            self.__lista[i].changevalorV(nv)    #CAMBIA EL VALOR DE VEHICULO DE CADA PLAN
    
    def opcion2(self):
        print("---------->COMPARAR VALORES DE CUOTA<----------")
        dato = int(input("Ingrese valor a comparar: "))
        for i in range(len(self.__lista)):
            imp = int(self.__lista[i].getvalorV())   #IMPORTE DEL VEHICULO
            cuota = int(self.__lista[i].getcuotas()) #CUOTAS
            valc = float((imp/cuota) + imp*0.10)       #CALCULA VALOR DE LA CUOTA
            if dato > valc:
                print(self.__lista[i])          #IMPRIME DATOS DE LOS PLANES CON MENOR CUOTA QUE EL VALOR INGRESADO
    
    def opcion3(self):
        print("---------->VALOR TOTAL A LICITAR<----------")
        for i in range(len(self.__lista)):
            lic = int(self.__lista[i].getcuolic())   #CUOTAS A LICITAR
            imp = int(self.__lista[i].getvalorV())   #IMPORTE DEL VEHICULO
            cuota = int(self.__lista[i].getcuotas()) #CUOTAS        
            valc = round((imp/cuota) + imp*0.10, 2)     #CALCULA VALOR DE CUOTA
            print(self.__lista[i])
            print("Licitacion de ${}".format(valc*lic))     #IMPRIME VALOR TOTAL DE LA LICITACION
    
    def opcion4(self):
        print("---------->MODIFICAR CUOTAS A LICITAR<----------")
        nv = int(input("Ingrese valor nuevo de cuotas a licitar para todos los planes: "))
        planahorro.changelic(nv)
        for i in range(len(self.__lista)):
            print(self.__lista[i])
            print("Cuotas a licitar -> {}".format(self.__lista[i].getcuolic()))