class planahorro:
    __codigo = 0
    __modelo = ''
    __version = ''
    __valorV = 0
    __cuotas = 0
    __cuotas_licitar = 15
    def __init__(self, cod, mod, ver, val, c):
        self.__codigo = cod
        self.__modelo = mod
        self.__version = ver
        self.__valorV = val
        self.__cuotas = c
        #self.__cuotas_licitar = cl
    def __str__(self):  #para el item b
        return("Cod Plan: {} | Modelo: {} - Version: {}".format(self.__codigo, self.__modelo, self.__version))
    def changevalorV(self, valor):
        self.__valorV = valor
        print("Valor actualizado")
    def getvalorV(self):
        return self.__valorV
    def getcuotas(self):
        return self.__cuotas
    def getcuolic(self):
        return self.__cuotas_licitar
    def getcod(self):
        return self.__codigo
    @classmethod
    def changelic(cls, nv):
        cls.__cuotas_licitar = nv