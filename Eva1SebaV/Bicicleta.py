from Transporte import Transporte

class Bicicleta(Transporte):
    def __init__(self, aro, peso, precio, marca):
        self._aro = aro
        self._peso = peso
        self._precio = precio
        self._marca = marca

    def get_aro(self):
        return self._aro

    def get_peso(self):
        return self._peso

    def get_precio(self):
        return self._precio

    def get_marca(self):
        return self._marca

    def set_aro(self, aro):
        self._aro = aro

    def set_peso(self, peso):
        self._peso = peso

    def set_precio(self, precio):
        self._precio = precio

    def set_marca(self, marca):
        self._marca = marca

    def calcularCostoDespacho(self):
        costo_base_despacho = 4000
        costo_por_kg = 400  
        costo_despacho = costo_base_despacho + (self._peso * costo_por_kg)
        return costo_despacho

    def mostrarInfo(self):
        costo_despacho = self.calcularCostoDespacho()
        precio_final = self._precio + costo_despacho
        print(f"Marca: {self._marca}\nAro: {int(self._aro):d}\nPeso: {int(self._peso):d} kg\nPrecio Original: ${int(self._precio):d}\nCosto de Despacho: ${int(costo_despacho):d}\nPrecio Final: ${int(precio_final):d}")
