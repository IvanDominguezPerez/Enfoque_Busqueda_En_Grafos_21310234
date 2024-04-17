class ValorInformacion:
    def __init__(self, utilidad_inicial, utilidad_posterior):
        self.utilidad_inicial = utilidad_inicial  # Utilidad esperada antes de obtener la información
        self.utilidad_posterior = utilidad_posterior  # Utilidad esperada después de obtener la información

    def calcular_valor(self):
        return self.utilidad_posterior - self.utilidad_inicial  # Calcula la diferencia de utilidad

# Ejemplo de uso
utilidad_inicial = 1000  # Utilidad esperada antes de obtener la información
utilidad_posterior = 1200  # Utilidad esperada después de obtener la información

valor_informacion = ValorInformacion(utilidad_inicial, utilidad_posterior)
valor = valor_informacion.calcular_valor()

print("Valor de la información:", valor)
