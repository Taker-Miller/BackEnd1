from Tecnologia import Tecnologia
from Transporte import Transporte

class Scooter(Tecnologia, Transporte):
    def __init__(self, marca, voltaje, eficiencia, precio, aro, velocidad, peso):
      
        Tecnologia.__init__(self, marca, voltaje, eficiencia, precio)
        
        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso  

    def get_aro(self):
        return self.__aro

    def set_aro(self, aro):
        self.__aro = aro

    def get_velocidad(self):
        return self.__velocidad

    def set_velocidad(self, velocidad):
        self.__velocidad = velocidad

    def calcularCostoDespacho(self):
        valor_por_kg = 300  
        return super().calcularDespacho(self.__peso, valor_por_kg)

    def calcularDescuento(self):
        eficiencia = self.get_eficiencia()
        if eficiencia in ['A', 'B']:
            return 0.5
        elif eficiencia in ['C', 'D']:
            return 0.3
        elif eficiencia in ['E', 'F']:
            return 0.1
        else:
            return 0.0

    def mostrarInfo(self):
        descuento = self.calcularDescuento()
        costo_despacho = self.calcularCostoDespacho()
        precio_final = self.get_precio() * (1 - descuento) + costo_despacho
        print(f"Marca: {self.get_marca()}\nVoltaje: {self.get_voltaje()}\nEficiencia: {self.get_eficiencia()}\nPrecio Original: ${int(self.get_precio()):d}\nDescuento: {int(descuento * 100):d}%\nCosto de Despacho: ${int(costo_despacho):d}\nPrecio Final: ${int(precio_final):d}\nAro: {int(self.__aro):d}\nVelocidad Máxima: {int(self.__velocidad)} km/h\nPeso: {int(self.__peso)} kg")
