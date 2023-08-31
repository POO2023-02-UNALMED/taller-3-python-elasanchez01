class Control:

    tv = TV(self, marca, estado)

    def turnON(self):
        self.tv.turnOn()

    def turnOff(self):
        self.tv.turnOff()
    
    def canalUp(self):
        self.tv.canalUp()

    def canalDown(self):
        self.tv.canalDown()

    def setCanal(self):
        return self.tv.canal

    def setVolumen(self):
        return self.tv.volumen
    
    def enlazar(self, tv):
        self.tv = tv

    def setTv(self, tv):
        self.tv = tv

    def getTv(self):
        return self.tv
