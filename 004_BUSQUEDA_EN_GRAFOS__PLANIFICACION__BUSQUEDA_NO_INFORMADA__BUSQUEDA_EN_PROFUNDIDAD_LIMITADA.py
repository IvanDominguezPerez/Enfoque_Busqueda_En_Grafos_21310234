class Grafo:
    def __init__(self):
        self.grafo = {}  # Inicializa el grafo como un diccionario vacío

    def agregar_arista(self, u, v):
        if u not in self.grafo:
            self.grafo[u] = []  # Crea una lista vacía para los vecinos del nodo u si no existe
        self.grafo[u].append(v)  # Agrega una arista al grafo desde el nodo u al nodo v

    def ldfs(self, inicio, objetivo, profundidad_max, visitado=None):
        if visitado is None:
            visitado = set()  # Inicializa el conjunto de nodos visitados en la primera llamada a la función

        if inicio == objetivo:  # Verifica si el nodo actual es el objetivo
            return [inicio]  # Retorna el camino con el nodo objetivo

        if profundidad_max <= 0:  # Verifica si se alcanzó la profundidad máxima
            return None  # Retorna None indicando que no se encontró el objetivo dentro de la profundidad máxima

        visitado.add(inicio)  # Marca el nodo actual como visitado

        for vecino in self.grafo.get(inicio, []):  # Recorre los vecinos del nodo actual
            if vecino not in visitado:
                # Realiza LDFS desde el vecino con una profundidad reducida
                camino = self.ldfs(vecino, objetivo, profundidad_max - 1, visitado)
                if camino is not None:  # Si se encontró un camino al objetivo desde el vecino
                    return [inicio] + camino  # Retorna el camino desde el nodo actual hasta el objetivo

        return None  # Retorna None si no se encontró el objetivo desde el nodo actual

# Ejemplo de uso
g = Grafo()
g.agregar_arista(0, 1)
g.agregar_arista(0, 2)
g.agregar_arista(1, 3)
g.agregar_arista(2, 4)
g.agregar_arista(2, 5)
g.agregar_arista(3, 6)
g.agregar_arista(3, 7)

inicio = 0
objetivo = 7
profundidad_max = 3

camino = g.ldfs(inicio, objetivo, profundidad_max)

if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino dentro de la profundidad máxima")
