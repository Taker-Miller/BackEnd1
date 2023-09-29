class Transporte:
    COSTODESPACHOBASE = 4000

    def calcularDespacho(self, peso, valor_por_kg):
        return self.COSTODESPACHOBASE + (peso * valor_por_kg)
