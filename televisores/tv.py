class TV:

    numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = None
        TV.numTV = TV.numTV + 1
    
    def setNumTV(cls, num):
        cls.numTV = num

    def getNumTV(self):
        return self.numTV

    def getEstado(self):
        return self.estado

    def setMarca(self, brand):
        self.marca = brand

    def getMarca(self):
        return self.marca

    def setCanal(self, chanel):
        self.canal = chanel

    def getCanal(self):
        return self.canal

    def setPrecio(self, price):
        self.precio = price

    def getPrecio(self):
        return self.precio

    def setVolumen(self, vol):
        self.volumen = vol

    def getVolumen(self):
        return self.volumen

    def setControl(self, new):
        self.control = new

    def getControl(self):
        return self.control
    
    def turnOn(self):
        if self.estado == False:
            self.estado = True
        
    def turnOff(self):
        if self.estado == True:
            self.estado = False

    def setEstado(self):
        return self.estado
    
    def canalDown(self):
        if self.estado and 1 < self.control <= 120:
            self.canal -= 1

    def canalUp(self):
        if self.estado and 1 <= self.control < 120:
            self.canal += 1

    def volumenDown(self):
        if self.estado and 0 < self.volumen <= 7:
            self.volumen -= 1

    def volumenUp(self):
        if self.estado and 0 <= self.volumen < 7:
            self.volumen += 1
