class Tecnologia:
    def __init__(self, marca, voltaje, eficiencia, precio):
        self._marca = marca
        self._voltaje = voltaje
        self._eficiencia = eficiencia
        self._precio = precio

   
    def get_marca(self):
        return self._marca

    def get_voltaje(self):
        return self._voltaje

    def get_eficiencia(self):
        return self._eficiencia

    def get_precio(self):
        return self._precio

 
    def set_marca(self, marca):
        self._marca = marca

    def set_voltaje(self, voltaje):
        self._voltaje = voltaje

    def set_eficiencia(self, eficiencia):
        self._eficiencia = eficiencia

    def set_precio(self, precio):
        self._precio = precio

    def calcularDescuento(self):
        if self._eficiencia in ['A', 'B']:
            return 0.5
        elif self._eficiencia in ['C', 'D']:
            return 0.3
        elif self._eficiencia in ['E', 'F']:
            return 0.1
        else:
            return 0
