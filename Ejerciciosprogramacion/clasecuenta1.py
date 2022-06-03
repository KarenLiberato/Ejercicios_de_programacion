
class Cuenta:
# Variable clase

    numero="1542"
fecha="01/03/22"
apertura="abril"
saldo="2.000.000"

 
def __init__(self,_numero,_fecha,_apertura,_saldo):
    #Variable de instancia
    self.__numero=_numero
    self.__fecha=_fecha
    self.__apertura=_apertura
    self.__saldo=_saldo
    
    #getters
    
    #def setnumero(self,numero):
    # self.__numero=numero
    def getNumero(self):
        return self.numero
    #def setfecha(self,fecha):
    # self.__fecha=fecha
    def getFecha(self):
        return self.fecha
    #def setapertura(self,apertura):
    # self.__apertura=apertura
    def getApertura(self):
        return self.apertura
    #def setsaldo(self,saldo):
    # self.__saldo=saldo
    def getSaldo(self):
        return self.saldo

cuenta=("01","abril","1542")
print(cuenta.get_Numero())
cuenta.set_numero(1542)
print(cuenta.get_saldo())
cuenta.set_saldo(2000000)
print(cuenta.get_saldo())


