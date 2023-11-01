class TransporteUrbano:
    def __init__(self, tipo, marca, modelo):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo

    def presentar_informacion(self):
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}\n----------")

class Carro(TransporteUrbano):
    def __init__(self, marca, modelo):
        super().__init__("Carro", marca, modelo)

class Bicicleta(TransporteUrbano):
    def __init__(self, marca, modelo):
        super().__init__("Bicicleta", marca, modelo)

class Autobus(TransporteUrbano):
    def __init__(self, marca, modelo):
        super().__init__("Autobus", marca, modelo)

class Moto(TransporteUrbano):
    def __init__(self, marca, modelo):
        super().__init__("Moto", marca, modelo)

class PatinetaElectrica(TransporteUrbano):
    def __init__(self, marca, modelo):
        super().__init__("Patineta Eléctrica", marca, modelo)

class Triciclo(TransporteUrbano):
    def __init__(self, marca, modelo):
        super().__init__("Triciclo", marca, modelo)

class Monopatin(TransporteUrbano):
    def __init__(self, marca, modelo):
        super().__init__("Monopatín", marca, modelo)
#instancias
carro1 = Carro("Toyota", "Corolla")
bicicleta1 = Bicicleta("Giant", "Talon")
autobus1 = Autobus("Mercedes-Benz", "Sprinter")
moto1 = Moto("Honda", "CBR500R")
patineta1 = PatinetaElectrica("Boosted", "Stealth")
triciclo1 = Triciclo("Schwinn", "Meridian")
monopatin1 = Monopatin("Bird", "One")
#lista de instancias 
transportes=[carro1,bicicleta1,autobus1,moto1,patineta1,monopatin1]
def obtener_informacion_de_transportes(transportes):
    for transporte in transportes:
        transporte.presentar_informacion()

obtener_informacion_de_transportes(transportes)