class FuncionUtilidad:
    def __init__(self, pesos):
        self.pesos = pesos  # Pesos asignados a cada resultado

    def calcular_utilidad(self, resultados):
        if len(resultados) != len(self.pesos):
            raise ValueError("La longitud de los resultados debe ser igual a la longitud de los pesos.")
        
        utilidad = 0
        for resultado, peso in zip(resultados, self.pesos):
            utilidad += resultado * peso  # Suma ponderada de los resultados y los pesos
        
        return utilidad

# Ejemplo de uso
pesos = [0.3, 0.5, 0.2]  # Pesos asignados a cada resultado
funcion_utilidad = FuncionUtilidad(pesos)

resultados = [100, 50, 20]  # Resultados de una acción
utilidad = funcion_utilidad.calcular_utilidad(resultados)

print("Utilidad de la acción:", utilidad)
