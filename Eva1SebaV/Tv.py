from Tecnologia import Tecnologia

class Tv(Tecnologia):
    def __init__(self, marca, voltaje, eficiencia, precio, tamano):
        super().__init__(marca, voltaje, eficiencia, precio)
        self._tamano = tamano

  
    def get_tamano(self):
        return self._tamano

   
    def set_tamano(self, tamano):
        self._tamano = tamano

    def mostrarInfo(self):
        descuento = self.calcularDescuento()
        precio_descuento = self._precio * descuento
        precio_final = self._precio - precio_descuento
        print(f"Marca: {self._marca}\nVoltaje: {self._voltaje}\nEficiencia: {self._eficiencia}\nTamaño: {int(self._tamano)} pulgadas\nPrecio Original: ${int(self._precio):d}\nDescuento: ${int(precio_descuento):d} ({int(descuento*100):d}%)\nPrecio Final: ${int(precio_final):d}")
