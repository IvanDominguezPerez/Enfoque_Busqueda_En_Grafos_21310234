class BusquedaOnline:
    def __init__(self, grafo):
        self.grafo = grafo  # Grafo sobre el que se realiza la búsqueda

    def buscar(self, estado_inicial, objetivo):
        estado_actual = estado_inicial  # Estado inicial de la búsqueda
        while estado_actual != objetivo:
            acciones_disponibles = self.grafo[estado_actual]  # Obtiene las acciones disponibles desde el estado actual
            accion_elegida = self.seleccionar_accion(acciones_disponibles)  # Selecciona una acción para avanzar
            estado_siguiente = self.aplicar_accion(estado_actual, accion_elegida)  # Avanza al siguiente estado
            estado_actual = estado_siguiente  # Actualiza el estado actual
        return estado_actual  # Devuelve el estado objetivo encontrado

    def seleccionar_accion(self, acciones_disponibles):
        # Esta función selecciona una acción entre las disponibles.
        # En este ejemplo, se elige la primera acción disponible.
        return acciones_disponibles[0]

    def aplicar_accion(self, estado_actual, accion):
        # Esta función aplica una acción al estado actual y devuelve el siguiente estado.
        # En este ejemplo, se asume que el grafo es un diccionario donde las claves son los estados y los valores son listas de acciones posibles.
        return accion

# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': [],
    'H': []
}

busqueda = BusquedaOnline(grafo)
estado_final = busqueda.buscar('A', 'H')
print("Estado final encontrado:", estado_final)
