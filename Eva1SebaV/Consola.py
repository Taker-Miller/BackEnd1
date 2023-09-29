from Tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self, nombreConsola, version, marca, voltaje, eficiencia, precio):
        super().__init__(marca, voltaje, eficiencia, precio)
        self._nombreConsola = nombreConsola
        self._version = version

    def get_nombreConsola(self):
        return self._nombreConsola

    def get_version(self):
        return self._version

    def set_nombreConsola(self, nombreConsola):
        self._nombreConsola = nombreConsola

    def set_version(self, version):
        self._version = version

    def calcularDescuento(self):
        descuento = super().calcularDescuento()
        if self._version == "Lite":
            descuento += 0.05
        return descuento

    def mostrarInfo(self):
        descuento = self.calcularDescuento()
        precio_final = self._precio * (1 - descuento)
        print(f"Nombre: {self._nombreConsola}\nVersión: {self._version}\nMarca: {self._marca}\nVoltaje: {self._voltaje}\nEficiencia: {self._eficiencia}\nPrecio Original: ${int(self._precio):d}\nDescuento: {int(descuento*100):d}%\nPrecio Final: ${int(precio_final):d}")
