class BusquedaAscensoColinas:
    def __init__(self, estado_inicial, funcion_evaluacion, max_iter=100):
        self.estado_actual = estado_inicial  # Estado inicial de la búsqueda
        self.funcion_evaluacion = funcion_evaluacion  # Función de evaluación para determinar la calidad de un estado
        self.max_iter = max_iter  # Número máximo de iteraciones permitidas

    def buscar(self):
        iteracion = 0
        while iteracion < self.max_iter:
            vecino_mejor = None
            valor_mejor = self.funcion_evaluacion(self.estado_actual)  # Evalúa el estado actual
            for vecino in self.generar_vecinos(self.estado_actual):
                valor_vecino = self.funcion_evaluacion(vecino)  # Evalúa el vecino actual
                if valor_vecino > valor_mejor:  # Si el vecino es mejor que el estado actual
                    vecino_mejor = vecino
                    valor_mejor = valor_vecino
            if vecino_mejor is None:
                break  # Si no se encuentra un vecino mejor, termina la búsqueda
            self.estado_actual = vecino_mejor  # Actualiza el estado actual con el vecino mejor
            iteracion += 1
        return self.estado_actual

    def generar_vecinos(self, estado):
        # Esta función genera todos los vecinos posibles de un estado dado
        # En este ejemplo, se pueden implementar diferentes operadores de vecindad según el problema
        # Por ejemplo, para un problema de optimización, se pueden probar diferentes cambios en el estado
        # como intercambiar valores, agregar o eliminar elementos, etc.
        # Aquí se asume una implementación ficticia que simplemente agrega 1 a cada componente del estado
        for i in range(len(estado)):
            vecino = list(estado)
            vecino[i] += 1
            yield tuple(vecino)

# Función de evaluación de ejemplo
def funcion_evaluacion_ejemplo(estado):
    # Esta función de evaluación devuelve la suma de los elementos del estado
    return sum(estado)

# Ejemplo de uso
estado_inicial = (0, 0, 0)  # Estado inicial arbitrario
busqueda_ascenso_colinas = BusquedaAscensoColinas(estado_inicial, funcion_evaluacion_ejemplo)
estado_optimo = busqueda_ascenso_colinas.buscar()

print("Estado óptimo encontrado:", estado_optimo)
