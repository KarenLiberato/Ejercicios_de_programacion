class Coche:
    """ color="Rojo"
    marca="Ferari"
    modelo="Aventador"
    velocidad=300
    caballaje=500
    motor=2600"""
    #método constructor
    def _init_(self,color,marca,modelo,velocidad,caballaje,motor):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.motor=motor
    
    
#métodos
    #def setColor(self,color):
    #    self.color=color
    def getColor(self):
        return self.color 
   # def setMarca(self,marca):
       # self.marca=marca
    def getMarca(self):
        return self.marca
   # def setModelo(self,modelo):
      #  self.modelo=modelo
    def getModelo(self):
        return self.modelo
    def acelerar(self):  
      …
      