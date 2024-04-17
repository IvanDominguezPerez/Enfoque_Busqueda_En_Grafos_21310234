class BusquedaTabu:
    def __init__(self, estado_inicial, funcion_evaluacion, generar_vecinos, tamano_lista_tabu, max_iter=100):
        self.estado_actual = estado_inicial  # Estado inicial de la búsqueda
        self.funcion_evaluacion = funcion_evaluacion  # Función de evaluación para determinar la calidad de un estado
        self.generar_vecinos = generar_vecinos  # Función para generar los vecinos de un estado
        self.tamano_lista_tabu = tamano_lista_tabu  # Tamaño de la lista tabú
        self.max_iter = max_iter  # Número máximo de iteraciones permitidas
        self.lista_tabu = []  # Lista tabú para almacenar movimientos prohibidos

    def buscar(self):
        iteracion = 0
        while iteracion < self.max_iter:
            vecinos = self.generar_vecinos(self.estado_actual)  # Genera los vecinos del estado actual
            vecino_mejor = None
            valor_mejor = float('-inf')  # Valor de referencia para la función de evaluación
            for vecino in vecinos:
                if vecino not in self.lista_tabu:  # Verifica si el vecino no está en la lista tabú
                    valor_vecino = self.funcion_evaluacion(vecino)  # Evalúa el vecino actual
                    if valor_vecino > valor_mejor:
                        vecino_mejor = vecino
                        valor_mejor = valor_vecino
            if vecino_mejor is None:
                break  # Si no se encuentra un vecino que no esté en la lista tabú, termina la búsqueda
            self.estado_actual = vecino_mejor  # Actualiza el estado actual con el vecino mejor
            self.lista_tabu.append(vecino_mejor)  # Agrega el movimiento a la lista tabú
            if len(self.lista_tabu) > self.tamano_lista_tabu:
                self.lista_tabu.pop(0)  # Elimina el movimiento más antiguo de la lista tabú
            iteracion += 1
        return self.estado_actual

# Función de evaluación de ejemplo
def funcion_evaluacion_ejemplo(estado):
    # Esta función de evaluación devuelve la suma de los elementos del estado
    return sum(estado)

# Función para generar vecinos de ejemplo
def generar_vecinos_ejemplo(estado):
    # Esta función genera vecinos cambiando un solo elemento del estado
    vecinos = []
    for i in range(len(estado)):
        vecino = list(estado)
        vecino[i] += 1
        vecinos.append(tuple(vecino))
    return vecinos

# Ejemplo de uso
estado_inicial = (0, 0, 0)  # Estado inicial arbitrario
tamano_lista_tabu = 5  # Tamaño de la lista tabú
busqueda_tabu = BusquedaTabu(estado_inicial, funcion_evaluacion_ejemplo, generar_vecinos_ejemplo, tamano_lista_tabu)
estado_optimo = busqueda_tabu.buscar()

print("Estado óptimo encontrado:", estado_optimo)
